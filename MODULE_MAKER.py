import shutil
import os
import site
import subprocess
import sys

cwd = os.path.dirname(__file__)

build_dir = os.path.join(cwd, "pmma", "build")
temp_dir = os.path.join(cwd, "pmma", "temporary")

print("Building PMMA Core...")

command = [ # if error occurs, run command manually :) "python setup.py build_ext" should do ALSO MAKE SURE NO IDLE/CODE INSTANCES ARE RUNNING
    sys.executable,
    os.path.join(cwd, "core_setup.py"),
    "build_ext",
    "--build-lib",
    build_dir,
    "--build-temp",
    temp_dir]

if sys.platform.startswith("win"):
    vcvars_path = "C:/Program Files/Microsoft Visual Studio/2022/Community/VC/Auxiliary/Build/vcvars64.bat"

    if not os.path.exists(vcvars_path):
        raise RuntimeError(f"Cannot find vcvars64.bat at: {vcvars_path}")

    full_command = f'"{vcvars_path}" && ' + " ".join(command)
    print("\n>>> Running in MSVC environment:")
    print("cmd.exe /c", full_command)
    print("="*30)

    result = subprocess.run(f'cmd.exe /c "{full_command}"', capture_output=True, text=True, shell=True)

    if result.returncode != 0:
        print(result.stderr)
        raise RuntimeError("Build failed")
    else:
        print(result.stdout)
else:
    # Non-Windows builds
    print("\n>>> " + " ".join(command))
    print("="*30)
    print(subprocess.check_output(command).decode("utf-8").strip())
print("="*30)

print()

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
print(subprocess.check_output(command).decode("utf-8").strip())
print("="*30)

print()

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

current_dir = os.path.dirname(os.path.abspath(__file__))

print("Copying new version of PMMA...")
shutil.copytree(os.path.join(current_dir, 'pmma'), os.path.join(SITE_PACKAGE_DIR, 'pmma'))