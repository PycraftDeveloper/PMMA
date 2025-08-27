# type: ignore

import time
import shutil

from utils import *

if __name__ == "__main__":
    program_start = time.perf_counter()

    in_github_workflow = os.environ.get("GITHUB_ACTIONS") == "true"
    build_debug = False
    rebuild_needed = True # True

    if not in_github_workflow:
        os.system('cls' if os.name == 'nt' else 'clear')

        response = user_input(
        "Do you want to build a DEBUG version of PMMA? [y/N]: ",
        "n",
        5)

        build_debug = response[0].lower() == "y"

    if rebuild_needed:
        print("🗑️ Removing old build and configuration...")
        shutil.rmtree(cmake_temp_dir, ignore_errors=True)
        shutil.rmtree(os.path.join(extern_dir, "lib"), ignore_errors=True)
        shutil.rmtree(os.path.join(extern_dir, "bin"), ignore_errors=True)
        shutil.rmtree(os.path.join(extern_dir, "share"), ignore_errors=True)
        shutil.rmtree(pmma_lib_dir)
        shutil.rmtree(os.path.join(cwd, "dist"), ignore_errors=True)
        shutil.rmtree(os.path.join(cwd, "build"), ignore_errors=True)
        shutil.rmtree(os.path.join(cwd, "pmma.egg-info"), ignore_errors=True)
        selectively_clean_extern()

    print("🗑️ Removing old logs...")
    shutil.rmtree(temporary_logging_dir, ignore_errors=True)

    os.makedirs(cmake_temp_dir, exist_ok=True)
    os.makedirs(extern_dir, exist_ok=True)
    os.makedirs(temporary_logging_dir, exist_ok=True)
    os.makedirs(os.path.join(temporary_logging_dir, "dependencies"), exist_ok=True)
    os.makedirs(pmma_lib_dir, exist_ok=True)

    bm = DependencyBuildManager()

    bm.add_component("zlib")
    bm.add_component("harfbuzz")
    bm.add_component("libpng", dependencies=["zlib"])
    bm.add_component("glfw")
    bm.add_component("freetype", dependencies=["zlib", "libpng", "harfbuzz"])
    bm.add_component("bgfx")

    bm.build()

    end = time.perf_counter()
    print(f"🕒 Dependency Build took {end - program_start:.2f} seconds")

    start = time.perf_counter()

    build_pmma(build_debug)

    end = time.perf_counter()

    print(f"🕒 PMMA Build took {end - start:.2f} seconds")

    start = time.perf_counter()

    run_setup(in_github_workflow)

    program_end = time.perf_counter()
    print(f"🕒 Running Setup.py took {program_end - start:.2f} seconds")
    print(f"🕒 Total Build took {program_end - program_start:.2f} seconds")