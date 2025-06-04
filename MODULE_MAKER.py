import shutil
import os
import site
import subprocess
import sys
import platform
import glob

cwd = os.path.dirname(__file__)

build_dir = os.path.join(cwd, "pmma", "build")
lib_dir = os.path.join(cwd, "pmma", "lib")
temp_dir = os.path.join(cwd, "pmma", "temporary")
include_dir = os.path.join(cwd, "pmma", "core", "hpp_src")

glfw_include = "H:/Downloads/CPMMA/extern/glfw-3.4.bin.WIN64/include"
glfw_lib = "H:/Downloads/CPMMA/extern/glfw-3.4.bin.WIN64/lib-vc2022/glfw3.lib"
########################### BUILD PMMA CORE ############################

def build_shared_lib():
    cpp_file = os.path.join(cwd, "pmma", "core", "cpp_src", "libshared.cpp")
    output_dir = os.path.abspath(lib_dir)
    os.makedirs(output_dir, exist_ok=True)

    libname = "libshared"
    system = platform.system()

    if system == "Windows":
        output_lib = os.path.join(output_dir, f"{libname}.dll")
        build_windows_shared_lib(cpp_file, include_dir, output_lib)

    elif system == "Darwin":
        output_lib = os.path.join(output_dir, f"lib{libname}.dylib")
        cmd = [
            "g++", "-dynamiclib", "-std=c++17", "-fPIC",
            cpp_file, "-I", include_dir, "-I", glfw_include,
            "-o", output_lib, "-L", glfw_lib, "-lglfw"
        ]
        subprocess.run(cmd, check=True)

    elif system == "Linux":
        output_lib = os.path.join(output_dir, f"lib{libname}.so")
        cmd = [
            "g++", "-shared", "-std=c++17", "-fPIC",
            cpp_file, "-I", include_dir, "-I", glfw_include,
            "-o", output_lib, "-L", glfw_lib, "-lglfw"
        ]
        subprocess.run(cmd, check=True)

    else:
        raise RuntimeError(f"Unsupported platform: {system}")

    print(f"✅ Built shared library: {output_lib}")
    return output_lib

def is_python_64bit():
    return platform.architecture()[0] == '64bit'

def build_windows_shared_lib(cpp_file, include_dir, output_lib):
    arch = 'amd64' if is_python_64bit() else 'x86'

    # Path to vcvarsall.bat
    vs_install_dir = r"C:\Program Files\Microsoft Visual Studio\2022\Community"
    vcvarsall_path = os.path.join(vs_install_dir, "VC", "Auxiliary", "Build", "vcvarsall.bat")

    if not os.path.exists(vcvarsall_path):
        raise FileNotFoundError(f"vcvarsall.bat not found at {vcvarsall_path}")

    cmd = (
        f'cmd.exe /C "'
        f'call "{vcvarsall_path}" {arch} && '
        f'cl /LD "{cpp_file}" '
        f'/DBUILDING_LIBSHARED '
        f'/I "{include_dir}" /I "{glfw_include}" '
        f'/Fe:"{output_lib}" '
        f'/link "{glfw_lib}"'
        f'"'
    )

    print(cmd)
    subprocess.run(cmd, check=True, stderr=subprocess.STDOUT)

def find_vsdevcmd():
    candidates = glob.glob(
        r"C:\Program Files\Microsoft Visual Studio\2022\*\Common7\Tools\VsDevCmd.bat"
    )
    if not candidates:
        raise FileNotFoundError("Could not find VsDevCmd.bat.")
    return candidates[0]

print("Building PMMA Core...")

build_shared_lib()

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