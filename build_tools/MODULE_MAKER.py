#type: ignore

# Additional dependencies: pkgconf-pkg-config zlib-devel libpng-devel bzip2-devel brotli-devel?


import shutil
import os
import site
import subprocess
import sys
import platform
from typing import Iterable
import multiprocessing

cwd = os.path.dirname(os.path.dirname(__file__))

build_dir = os.path.join(cwd, "pmma", "build")
lib_dir = os.path.join(cwd, "pmma", "lib")
extern_dir = os.path.join(cwd, "pmma", "extern")
temp_dir = os.path.join(cwd, "temporary")
include_dir = os.path.join(cwd, "pmma", "core", "hpp_src")
pyx_dir = os.path.join(cwd, "pmma", "core", "pyx_src")
cmake_temp_dir = os.path.join(temp_dir, "cmake")
build_tools_dir = os.path.join(cwd, "build_tools")
perm_extern_dir = os.path.join(build_tools_dir, "extern")
cmake_dir = os.path.join(build_tools_dir, "cmake")

TERMINAL_SIZE = shutil.get_terminal_size().columns

########################## CLEAN UP  OLD DEPS ##########################

def clean_deps():
    print("Cleaning dependencies...")
    if os.path.exists(extern_dir):
        def should_keep(path):
            return f'include{os.sep}glm' in path or f'include{os.sep}glad' in path

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

print("=" * TERMINAL_SIZE)

result = ""
while result not in ["y", "n"]:
    result = input("Do you want to clean up PMMA's dependencies (not recommended, longer compile times)? (y/n): ").lower()
    if result == "":
        result = "n"

build_deps = result == "y"

if result == "y":
    clean_deps()
    print("Dependencies cleaned.")

########################## CLEAN UP  OLD CORE ##########################
def selective_removal(directory, keep_items: Iterable[str]):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)

        if os.path.isfile(item_path):  # Check if it's a file
            delete = True
            for keep_item in keep_items:
                if item.endswith(keep_item):
                    delete = False
                    break
            if delete:
                print("Deleting file:", item_path)
                os.remove(item_path)  # Delete the file

        elif os.path.isdir(item_path) and not item_path.endswith(".mypy_cache"):  # Check if it's a directory
            print("Deleting directory:", item_path)
            try:
                os.remove(item_path)  # Delete the directory
            except:
                print("Could not delete directory:", item_path)

def clean_old_core():
    print("Cleaning old build directories...")
    if os.path.exists(build_dir):
        selective_removal(build_dir, [".pyi"])

    if os.path.exists(pyx_dir):
        selective_removal(pyx_dir, [".pyx", ".pxd"])

    if os.path.exists(lib_dir):
        shutil.rmtree(lib_dir, ignore_errors=False)

print("=" * TERMINAL_SIZE)

result = ""
while result not in ["y", "n"]:
    result = input("Do you want to clean up old PMMA Core? (y/n): ").lower()
    if result == "":
        result = "y"

if result == "y":
    clean_old_core()
    print("Old PMMA Core cleaned.")

########################## CLEAN CMAKE TEMP ############################

print("=" * TERMINAL_SIZE)

result = ""
while result not in ["y", "n"]:
    result = input("Do you want to clean up the old build cache? (y/n): ").lower()
    if result == "":
        result = "y"

if result == "y":
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir, ignore_errors=True)

print("=" * TERMINAL_SIZE)

########################### BUILD PMMA CORE ############################

def flatten_dir(parent_dir):
    for subdir in os.listdir(parent_dir):
        subdir_path = os.path.join(parent_dir, subdir)

        # Ensure it's a directory before proceeding
        if os.path.isdir(subdir_path):
            for item in os.listdir(subdir_path):
                item_path = os.path.join(subdir_path, item)
                new_location = os.path.join(parent_dir, item)

                # Move file or directory to the parent directory
                shutil.move(item_path, new_location)

            # Optionally remove the now-empty subdirectory
            os.rmdir(subdir_path)

def build_shared_lib():
    # Create the build directory if it doesn't exist
    os.makedirs(cmake_temp_dir, exist_ok=True)

    print("📦 Running CMake configuration...")
    if build_deps:
        deps_flag = "-DBUILD_DEPS=ON"
    else:
        deps_flag = "-DBUILD_DEPS=OFF"

    subprocess.run(["cmake", "-DCMAKE_POLICY_VERSION_MINIMUM=3.5", cmake_dir, deps_flag], cwd=cmake_temp_dir, check=True)

    print("🔨 Building PMMA_Core...")
    build_command = ["cmake", "--build", "."]
    if platform.system() == "Windows":
        build_command += ["--config", "Release", "--", "/m"]
    else:
        build_command += ["--", f"-j{multiprocessing.cpu_count()}"]
    subprocess.run(build_command, cwd=cmake_temp_dir, check=True)

    flatten_dir(lib_dir)

    print("✅ Build complete. Output should be in pmma/lib/")

print("Building PMMA Core...")

build_shared_lib()

print("=" * TERMINAL_SIZE)

########################################################################
print("Building PMMA...")

command = [ # if error occurs, run command manually :) "python setup.py build_ext" should do ALSO MAKE SURE NO IDLE/CODE INSTANCES ARE RUNNING
    sys.executable,
    os.path.join(cwd, "setup.py"),
    "build_ext",
    "--build-lib",
    build_dir,
    "--build-temp",
    temp_dir]

print("\n>>> " + " ".join(command))
print("="*30)
subprocess.run(command, check=True)

print()

print("=" * TERMINAL_SIZE)

if not sys.platform.startswith("win"):
    result = input("The remainder of this script will attempt to update the pmma module on your computer. Do you wish to continue? (y/n): ")

    while result.lower() not in ["y", "n"]:
        result = input("Please enter 'y' or 'n': ")

    if result.lower() == "n":
        print("Remember to run this script again and select 'y' for the update to take effect FOR ANY PLATFORM.")
        print("Exiting...")
        sys.exit(0)

SITE_PACKAGE_DIR = site.getsitepackages()[-1]

print("Removing old version of PMMA...")
if os.path.exists(os.path.join(SITE_PACKAGE_DIR, 'pmma')):
    shutil.rmtree(os.path.join(SITE_PACKAGE_DIR, 'pmma'))

print("=" * TERMINAL_SIZE)

print("Copying new version of PMMA...")
def ignore_temp_dirs(directory, contents):
    return [item for item in contents if 'temporary' in os.path.join(directory, item)]

shutil.copytree(
    os.path.join(cwd, 'pmma'),
    os.path.join(SITE_PACKAGE_DIR, 'pmma'),
    ignore=ignore_temp_dirs
)

print("=" * TERMINAL_SIZE)