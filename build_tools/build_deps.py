# type: ignore

import json, time

from utils import *
from deps_utils import *
from deps_build_manager import *
from git_utils import *

program_start = time.perf_counter()

os.system('cls' if os.name == 'nt' else 'clear')

in_github_workflow = os.environ.get("GITHUB_ACTIONS") == "true"

ts_print("🗑️ Removing old build and configuration...")
shutil.rmtree(cmake_temp_dir, ignore_errors=True)
shutil.rmtree(os.path.join(extern_dir, "lib"), ignore_errors=True)
shutil.rmtree(os.path.join(extern_dir, "bin"), ignore_errors=True)
shutil.rmtree(os.path.join(extern_dir, "share"), ignore_errors=True)
shutil.rmtree(pmma_lib_dir, ignore_errors=True)
shutil.rmtree(os.path.join(cwd, "dist"), ignore_errors=True)
shutil.rmtree(os.path.join(cwd, "build"), ignore_errors=True)
shutil.rmtree(os.path.join(cwd, "pmma.egg-info"), ignore_errors=True)
selectively_clean_extern()
fetch_cache_branch(in_github_workflow)

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

ts_print("✏️ Writing dependency hashes...")
hashed_data = {}
for component in components:
    hashed_data[component] = hash_component(component)

with open(os.path.join(cwd, "build_tools", "hashes.json"), "w") as file:
    json.dump(hashed_data, file, indent=4)

update_cache_branch(in_github_workflow)

program_end = time.perf_counter()
ts_print(f"🕒 Total dependency build took {program_end - program_start:.2f} seconds")

if not in_github_workflow and not abort:
    ts_print("🤖 Automatically moving on to building PMMA.")
    import build_pmma # would be called for each version of python in the github workflow