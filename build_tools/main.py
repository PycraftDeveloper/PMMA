#type: ignore

import os, platform, shutil, site, subprocess, multiprocessing, sys
import random

operating_system_type = platform.system()

if operating_system_type == "Windows":
    os.system("cls")
elif operating_system_type == "Linux":
    os.system("clear")

cwd = os.path.dirname(os.path.dirname(__file__))

pmma_dir = os.path.join(cwd, "pmma")

pmma_core_dir = os.path.join(pmma_dir, "core")
pyx_src_dir = os.path.join(pmma_core_dir, "pyx_src")
hpp_src_dir = os.path.join(pmma_core_dir, "hpp_src")
cpp_src_dir = os.path.join(pmma_core_dir, "cpp_src")
py_src_dir = os.path.join(pmma_core_dir, "py_src")

pmma_core_lib_dir = os.path.join(pmma_dir, "lib")

build_dir = os.path.join(pmma_dir, "build")

extern_dir = os.path.join(pmma_dir, "extern")
extern_bin_dir = os.path.join(extern_dir, "bin")
extern_include_dir = os.path.join(extern_dir, "include")
extern_lib_dir = os.path.join(extern_dir, "lib")

temp_dir = os.path.join(cwd, "temporary")
temp_cache_dir = os.path.join(temp_dir, "cache")
temp_platform_cache_dir = os.path.join(temp_cache_dir, operating_system_type)
temp_platform_opposite_build_type_cache_dir = os.path.join(temp_cache_dir, operating_system_type + " - DEBUG")

build_tools_dir = os.path.join(cwd, "build_tools")
cmake_dir = os.path.join(build_tools_dir, "cmake")

cmake_temp_dir = os.path.join(temp_dir, "cmake")

BUILD_CORE = "build core"
BUILD_CYTHON = "build cython"
BUILD_DEPENDENCIES = "build dependencies"
to_do = []

SITE_PACKAGE_DIRS = site.getsitepackages()

os.makedirs(cmake_temp_dir, exist_ok=True)
os.makedirs(pmma_core_lib_dir, exist_ok=True)

def clean_deps():
    if os.path.exists(extern_dir):
        def should_keep(path):
            return f'include{os.sep}glm' in path or f'include{os.sep}glad' in path or f'include{os.sep}FlatHashMap' in path

        for dirpath, dirnames, filenames in os.walk(extern_dir, topdown=False):
            full_dirpath = os.path.abspath(dirpath)
            # Remove files not in keep paths
            for filename in filenames:
                full_path = os.path.join(full_dirpath, filename)
                if not should_keep(full_path):
                    os.remove(full_path)

            # Remove directories if they're empty and not part of keep paths
            for dirname in dirnames:
                full_subdir = os.path.join(full_dirpath, dirname)
                if not should_keep(full_subdir) and not os.listdir(full_subdir):
                    os.rmdir(full_subdir)

        # Optionally remove directories that became empty after cleaning
        if not should_keep(extern_dir) and not os.listdir(extern_dir):
            os.rmdir(extern_dir)

def selective_removal(directory, keep_items):
    # Use a list as a queue to process directories iteratively
    dirs_to_process = [directory]

    while dirs_to_process:
        current_dir = dirs_to_process.pop(0)

        for item in os.listdir(current_dir):
            item_path = os.path.join(current_dir, item)

            if os.path.isfile(item_path):
                # Check if the file should be deleted
                if not any(item.endswith(keep) for keep in keep_items):
                    os.remove(item_path)

            elif os.path.isdir(item_path):
                # Add subdirectory to the queue for later processing
                if not item_path.endswith(".mypy_cache"):
                    dirs_to_process.append(item_path)

        # After processing, try to remove empty directories
        for item in os.listdir(current_dir):
            item_path = os.path.join(current_dir, item)
            if os.path.isdir(item_path) and not os.listdir(item_path):
                try:
                    os.rmdir(item_path)
                except Exception as e:
                    print("Could not delete directory:", item_path, "-", e)

def scan_files_for_changes(dir, component, ignore=[]):
    if component in to_do:
        return

    if not os.path.exists(dir):
        raise FileNotFoundError(f"Directory not found: {dir}")

    for dirpath, dirnames, filenames in os.walk(dir):
        full_dirpath = os.path.abspath(dirpath)
        # Remove files not in keep paths
        for filename in filenames:
            full_path = os.path.join(full_dirpath, filename)
            cache_path = full_path.replace(cwd, temp_platform_cache_dir)

            if any(full_path.endswith(ending) for ending in ignore):
                continue

            if not os.path.exists(cache_path):
                print(f"File {full_path} not found in cache.")
                to_do.append(component)
                return

            with open(full_path, "rb") as f:
                new_data = f.read()

            with open(cache_path, "rb") as f:
                old_data = f.read()

            if new_data != old_data:
                print(f"File {full_path} has been modified.")
                to_do.append(component)
                return

def cache_files(dir):
    if not os.path.exists(dir):
        raise FileNotFoundError(f"Directory not found: {dir}")

    for dirpath, dirnames, filenames in os.walk(dir):
        full_dirpath = os.path.abspath(dirpath)
        # Remove files not in keep paths
        for filename in filenames:
            full_path = os.path.join(full_dirpath, filename)
            cache_path = full_path.replace(cwd, temp_platform_cache_dir)

            with open(full_path, "rb") as f:
                data = f.read()

            os.makedirs(os.path.dirname(cache_path), exist_ok=True)
            with open(cache_path, "wb") as f:
                f.write(data)

if not os.path.exists(temp_platform_cache_dir):
    print("Cache not found, building from scratch. This will take a while.")
    if os.path.exists(temp_dir):
        if os.path.exists(temp_dir):
            for dirpath, dirnames, filenames in os.walk(temp_cache_dir):
                for dirname in dirnames:
                    full_path = os.path.join(dirpath, dirname)
                    # Skip deletion if this is the excluded path
                    if os.path.abspath(full_path) == os.path.abspath(temp_platform_opposite_build_type_cache_dir):
                        continue
                    shutil.rmtree(full_path)

    os.makedirs(temp_platform_cache_dir)
    if os.path.exists(build_dir):
        selective_removal(build_dir, [".pyi"])
    to_do = [BUILD_CORE, BUILD_CYTHON, BUILD_DEPENDENCIES]
else:
    print("Looking for PYX changes.")
    scan_files_for_changes(pyx_src_dir, BUILD_CYTHON, ignore=[".cpp", ".html"])

    if not BUILD_CYTHON in to_do:
        raw_files = []
        for dirpath, dirnames, filenames in os.walk(pyx_src_dir):
            full_dirpath = os.path.abspath(dirpath)
            # Remove files not in keep paths
            for filename in filenames:
                if not ".pyx" in filename:
                    raw_files.append(filename)

        built_files = os.listdir(build_dir)

        for raw_file in raw_files:
            found = False
            for built_file in built_files:
                split_built_file = built_file.split(".")
                if (not "pyi" in split_built_file[-1]) and split_built_file[0] == raw_file.split(".")[0]:
                    found = True
                    break
            if not found:
                to_do.append(BUILD_CYTHON)
                break

    print("Looking for CPP changes.")
    scan_files_for_changes(hpp_src_dir, BUILD_CORE)
    scan_files_for_changes(cpp_src_dir, BUILD_CORE)

    print("Looking for PMMA_Core.")
    found_built_core = False
    for file in os.listdir(pmma_core_lib_dir):
        if "PMMA_Core" in file:
            found_built_core = True
            break

    if not found_built_core:
        to_do.append(BUILD_CORE)

    print("Looking for external libraries.")
    if not os.path.exists(extern_lib_dir):
        to_do.append(BUILD_DEPENDENCIES)
    else:
        if operating_system_type == "Windows":
            targets = {"freetype": False, "glfw3": False, "harfbuzz": False, "libpng16": False, "zlib": False}
        else:
            targets = {"freetype": False, "glfw3": False, "harfbuzz": False, "libpng16": False, "libz": False}

        for file in os.listdir(extern_lib_dir):
            for target in targets.keys():
                if target in file:
                    targets[target] = True

        for target, found in targets.items():
            if not found:
                to_do.append(BUILD_DEPENDENCIES)
                break

    if not BUILD_DEPENDENCIES in to_do:
        if not os.path.exists(extern_include_dir):
            to_do.append(BUILD_DEPENDENCIES)
        else:
            print("Looking for external include files.")
            targets = {"freetype2": False, "glad": False, "GLFW": False, "glm": False, "harfbuzz": False, "libpng16": False, "zlib": False, "png.h": False}

            for file in os.listdir(extern_include_dir):
                for target in targets.keys():
                    if target in file:
                        targets[target] = True

            for target, found in targets.items():
                if not found:
                    to_do.append(BUILD_DEPENDENCIES)
                    break

    if not BUILD_DEPENDENCIES in to_do:
        print("Looking for build configuration changes.")
        scan_files_for_changes(cmake_dir, BUILD_DEPENDENCIES)

if to_do == []:
    print("No changes detected.")
else:
    shutil.rmtree(temp_platform_cache_dir)

    cache_files(hpp_src_dir)
    cache_files(cpp_src_dir)
    cache_files(cmake_dir)
    cache_files(pyx_src_dir)

    if random.randint(0, 7) == 0:
        print("Attempting to refresh cython code.")
        to_do.append(BUILD_CYTHON)
        if os.path.exists(build_dir):
            selective_removal(build_dir, [".pyi"])

    if BUILD_CORE in to_do and not BUILD_DEPENDENCIES in to_do:
        print("Configuring PMMA Core.")

        if os.path.exists(pmma_core_lib_dir):
            shutil.rmtree(pmma_core_lib_dir, ignore_errors=False)

        if os.path.exists(cmake_temp_dir):
            shutil.rmtree(cmake_temp_dir, ignore_errors=True)

        os.makedirs(cmake_temp_dir, exist_ok=True)

        subprocess.run(["cmake", "-DCMAKE_POLICY_VERSION_MINIMUM=3.5", cmake_dir, "-DBUILD_DEPS=OFF"], cwd=cmake_temp_dir, check=True)

    elif BUILD_DEPENDENCIES in to_do:
        print("Configuring dependencies & PMMA Core")

        if os.path.exists(pmma_core_lib_dir):
            shutil.rmtree(pmma_core_lib_dir, ignore_errors=False)

        if os.path.exists(cmake_temp_dir):
            shutil.rmtree(cmake_temp_dir, ignore_errors=True)

        os.makedirs(cmake_temp_dir, exist_ok=True)

        clean_deps()

        subprocess.run(["cmake", "-DCMAKE_POLICY_VERSION_MINIMUM=3.5", cmake_dir, "-DBUILD_DEPS=ON"], cwd=cmake_temp_dir, check=True)

    if BUILD_CORE in to_do or BUILD_DEPENDENCIES in to_do:
        print("Building.")

        build_command = ["cmake", "--build", ".", "--parallel", str(multiprocessing.cpu_count())]
        if operating_system_type == "Windows":
            build_command += ["--config", "Release"]
        subprocess.run(build_command, cwd=cmake_temp_dir, check=True)

    if BUILD_CYTHON in to_do:
        print("Building Cython.")

        #if os.path.exists(build_dir):
            #selective_removal(build_dir, [".pyi"])

        if os.path.exists(pyx_src_dir):
            selective_removal(pyx_src_dir, [".pyx", ".pxd"])

        command = [
            sys.executable,
            os.path.join(cwd, "setup.py"),
            "build_ext",
            "--build-lib",
            build_dir,
            "--build-temp",
            temp_dir]

        subprocess.run(command, check=True)

print("Refreshing installed version of PMMA.")

installed = False
while not installed:
    for dir in SITE_PACKAGE_DIRS:
        try:
            if not installed:
                print(f"Trying location: {dir}")
                if os.path.exists(os.path.join(dir, 'pmma')):
                    shutil.rmtree(os.path.join(dir, 'pmma'))

                shutil.copytree(
                    pmma_dir,
                    os.path.join(dir, 'pmma'),
                )
                installed = True
                print(f"PMMA has been installed to: {dir}")
            else:
                print(f"Cleaning up any old versions of PMMA in: {dir}")
        except Exception as error:
            print(f"Cannot install PMMA here because: {error}")

    if not installed:
        response = input("Try again? (y/n): ")
        if response.lower() == "n":
            break

print("Scanning for missing stubs...")
content = os.listdir(build_dir) + os.listdir(py_src_dir)
src_files = []
pyi_files = []
for file in content:
    if file.endswith(".pyd") or file.endswith(".py"):
        src_files.append(file.split(".")[0])
    if file.endswith(".pyi"):
        pyi_files.append(file.split(".")[0])

for file in src_files:
    if file not in ["Utility"]:
        found = False
        for stub in pyi_files:
            if file == stub:
                found = True
                break

        if not found:
            print(f"Warning: {file}.pyd is missing a corresponding .pyi file.")

print("Done!")