# type: ignore

import json, time, argparse

from utils import *
from deps_utils import *
from deps_build_manager import *

program_start = time.perf_counter()

parser = argparse.ArgumentParser(description="Run in GitHub workflow mode")
parser.add_argument("-in_github_workflow", action="store_true", help="Run in GitHub workflow mode")
args = parser.parse_args()

Context.in_github_workflow = args.in_github_workflow
Context.build_deps_context_exists = True

if not Context.in_github_workflow:
    os.system('cls' if os.name == 'nt' else 'clear')

if not Context.in_github_workflow:
    response = input(
        "Do you want to build a DEBUG version of PMMA? [y/n] \
(Recommended: n): ")
    if response == "":
        Context.build_debug = False
    else:
        Context.build_debug = response[0].lower() == "y"

ts_print("Removing old build and configuration...")
threads = []
paths = [
    cmake_temp_dir,
    join_path(extern_dir, "lib"),
    join_path(extern_dir, "bin"),
    join_path(extern_dir, "share"),
    pmma_lib_dir,
    join_path(cwd, "dist"),
    join_path(cwd, "build"),
    join_path(cwd, "pmma.egg-info"),
    temporary_logging_dir
]
for path in paths:
    thread = CustomThreading(target=ts_rmtree, args=(path,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
CustomThreading(target=ts_rmtree, args=(cmake_temp_dir))

selectively_clean_extern()

if not Context.in_github_workflow:
    shutil.rmtree(build_cache_dir, ignore_errors=True)
    shutil.copytree(build_tools_dir, build_cache_dir)

os.makedirs(cmake_temp_dir, exist_ok=True)
os.makedirs(extern_dir, exist_ok=True)
os.makedirs(temporary_logging_dir, exist_ok=True)
os.makedirs(join_path(temporary_logging_dir, "dependencies"), exist_ok=True)
os.makedirs(pmma_lib_dir, exist_ok=True)

bm = DependencyBuildManager()

bm.add_component("zlib")
bm.add_component("harfbuzz")
bm.add_component("libpng", dependencies=["zlib"])
bm.add_component("glfw")
bm.add_component("freetype", dependencies=["zlib", "libpng", "harfbuzz"])

if Context.build_debug:
    bm.add_component("bgfx - debug")
else:
    bm.add_component("bgfx")

bm.build()

end = time.perf_counter()
ts_print(f"Dependency Build took {end - program_start:.2f} seconds")

ts_print("Writing dependency hashes...")
previous_components = {}
if os.path.exists(join_path(cwd, "build_tools", "hashes.json")):
    with open(join_path(cwd, "build_tools", "hashes.json"), "r") as file:
        previous_components = json.load(file)

hashed_data = {}
for component in previous_components:
    if component not in components:
        hashed_data[component] = previous_components[component]

for component in components:
    hashed_data[component] = hash_component(component)

with open(join_path(cwd, "build_tools", "hashes.json"), "w") as file:
    json.dump(hashed_data, file, indent=4)

if not Context.in_github_workflow:
    shutil.rmtree(build_cache_dir, ignore_errors=True)
    shutil.copytree(build_tools_dir, build_cache_dir)

program_end = time.perf_counter()
ts_print(f"Total dependency build took {program_end - program_start:.2f} seconds")