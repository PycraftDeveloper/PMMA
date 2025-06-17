#type: ignore

import shutil
import os
import site
import subprocess
import sys
import platform
from typing import Iterable

cwd = os.path.dirname(__file__)

build_dir = os.path.join(cwd, "pmma", "build")
lib_dir = os.path.join(cwd, "pmma", "lib")
temp_dir = os.path.join(cwd, "pmma", "temporary")
include_dir = os.path.join(cwd, "pmma", "core", "hpp_src")
pyx_dir = os.path.join(cwd, "pmma", "core", "pyx_src")
cmake_temp_dir = os.path.join(temp_dir, "cmake")
build_tools_dir = os.path.join(cwd, "build_tools")
vcpkg_dir = os.path.join(build_tools_dir, "vcpkg")

vcpkg_cmake = os.path.join(vcpkg_dir, "scripts", "buildsystems", "vcpkg.cmake")

TERMINAL_SIZE = shutil.get_terminal_size().columns

########################## CLEAN UP OLD BUILD ##########################
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

def clean_old_build():
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
    result = input("Do you want to clean up old build directories? (y/n): ").lower()

if result == "y":
    clean_old_build()

print("=" * TERMINAL_SIZE)

result = ""
while result not in ["y", "n"]:
    result = input("Do you want to clean up the last build cache (not generally recommended unless changing environments)? (y/n): ").lower()

if result == "y":
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir, ignore_errors=True)

print("=" * TERMINAL_SIZE)

####################### INSTALLING  DEPENDENCIES #######################

if platform.system() == "Windows":
    print("📦 Installing dependencies...")
    if not os.path.exists(vcpkg_dir):
        print("📦 Cloning vcpkg...")
        subprocess.run(["git", "clone", "https://github.com/microsoft/vcpkg.git", vcpkg_dir], check=True)

    subprocess.run(["cmd", "/c", "bootstrap-vcpkg.bat"], cwd=vcpkg_dir, check=True)
    #subprocess.run(["cmd", "/c", "vcpkg install glfw3"], cwd=vcpkg_dir, check=True)
    subprocess.run(["cmd", "/c", "vcpkg integrate install"], cwd=vcpkg_dir, check=True)

    print("✅ Dependencies installed.")

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
    if platform.system() == "Windows":
        subprocess.run(["cmake", cwd, f"-DCMAKE_TOOLCHAIN_FILE={vcpkg_cmake}"], cwd=cmake_temp_dir, check=True)
    else:
        subprocess.run(["cmake", cwd], cwd=cmake_temp_dir, check=True)

    print("🔨 Building PMMA_Core...")
    build_command = ["cmake", "--build", "."]
    if platform.system() == "Windows":
        build_command += ["--config", "Release"]
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
shutil.rmtree(os.path.join(SITE_PACKAGE_DIR, 'pmma'))

print("=" * TERMINAL_SIZE)

current_dir = os.path.dirname(os.path.abspath(__file__))

print("Copying new version of PMMA...")
def ignore_temporary(dir, contents):
    return ['temporary'] if dir == os.path.join(current_dir, 'pmma') else []

shutil.copytree(
    os.path.join(current_dir, 'pmma'),
    os.path.join(SITE_PACKAGE_DIR, 'pmma'),
    ignore=ignore_temporary
)

print("=" * TERMINAL_SIZE)