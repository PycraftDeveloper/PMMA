# type: ignore

from utils import *
import json

if __name__ == "__main__":
    program_start = time.perf_counter()

    in_github_workflow = os.environ.get("GITHUB_ACTIONS") == "true"
    build_debug = False

    if not in_github_workflow:
        os.system('cls' if os.name == 'nt' else 'clear')

        response = user_input(
        "Do you want to build a DEBUG version of PMMA? [y/N]: ",
        "n",
        5)

        build_debug = response[0].lower() == "y"

    ts_print("🗑️ Removing old build and configuration...")
    shutil.rmtree(cmake_temp_dir, ignore_errors=True)
    shutil.rmtree(os.path.join(extern_dir, "lib"), ignore_errors=True)
    shutil.rmtree(os.path.join(extern_dir, "bin"), ignore_errors=True)
    shutil.rmtree(os.path.join(extern_dir, "share"), ignore_errors=True)
    shutil.rmtree(pmma_lib_dir)
    shutil.rmtree(os.path.join(cwd, "dist"), ignore_errors=True)
    shutil.rmtree(os.path.join(cwd, "build"), ignore_errors=True)
    shutil.rmtree(os.path.join(cwd, "pmma.egg-info"), ignore_errors=True)
    selectively_clean_extern()

    ts_print("🗑️ Removing old logs...")
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
    ts_print(f"🕒 Dependency Build took {end - program_start:.2f} seconds")
    total_time = get_execution_time(build_pmma, build_debug)[0]
    ts_print(f"🕒 PMMA Build took {total_time:.2f} seconds")

    total_time = get_execution_time(run_setup, in_github_workflow)[0]
    ts_print(f"🕒 Running Setup.py took {total_time:.2f} seconds")

    ts_print("✏️ Writing dependency hashes...")
    hashed_data = {}
    for component in components:
        hashed_data[component] = hash_component(component)

    with open(os.path.join(cwd, "build_tools", "hashes.json"), "w") as file:
        json.dump(hashed_data, file, indent=4)

    program_end = time.perf_counter()
    ts_print(f"🕒 Total Build took {program_end - program_start:.2f} seconds")