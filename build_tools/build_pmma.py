# type: ignore

import subprocess, sys, sysconfig, platform, argparse

from pmma_utils import *
from utils import *

def build_pmma(build_debug, build_for_python):
    global abort
    if abort:
        ts_print("Aborting PMMA build due to previous errors.")
        return

    folder = os.path.join(cwd, "build_tools", "cmake", "pmma")

    # Configure PMMA ---------------------------------------------------
    ts_print("Configuring PMMA...")

    config_log_file = os.path.join(temporary_logging_dir, f"pmma-config.log")
    try:
        if build_debug:
            if build_for_python:
                python_executable_path = sys.executable

                ts_print(f"Using '{python_executable_path}'")
                configure_result = subprocess.run(
                    [
                        "cmake", "-S", folder, "-B", f"build/pmma",
                        f"-DWORKING_DIR={cwd}", "-DCMAKE_BUILD_TYPE=Debug",
                        f"-DPython3_EXECUTABLE={python_executable_path}",
                        #f'-DPython3_INCLUDE_DIR="{python_include}"',
                        #f'-DPython3_LIBRARY="{python_library}"',
                        "-DUSE_PYTHON=ON",
                        f"-DCMAKE_INSTALL_PREFIX={pmma_lib_dir}"
                    ], check=True, cwd=cmake_temp_dir, stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True)
            else:
                configure_result = subprocess.run(
                    [
                        "cmake", "-S", folder, "-B", f"build/pmma",
                        f"-DWORKING_DIR={cwd}", "-DCMAKE_BUILD_TYPE=Debug",
                        f"-DCMAKE_INSTALL_PREFIX={pmma_lib_dir}"
                    ], check=True, cwd=cmake_temp_dir, stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True)
        else:
            if build_for_python:
                python_executable_path = sys.executable

                ts_print(f"Using '{python_executable_path}'")
                configure_result = subprocess.run(
                    [
                        "cmake", "-S", folder, "-B", f"build/pmma",
                        f"-DWORKING_DIR={cwd}", "-DCMAKE_BUILD_TYPE=Release",
                        f"-DPython3_EXECUTABLE={python_executable_path}",
                        "-DUSE_PYTHON=ON",
                        f"-DCMAKE_INSTALL_PREFIX={pmma_lib_dir}"
                    ], check=True, cwd=cmake_temp_dir, stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True)
            else:
                configure_result = subprocess.run(
                    [
                        "cmake", "-S", folder, "-B", f"build/pmma",
                        f"-DWORKING_DIR={cwd}", "-DCMAKE_BUILD_TYPE=Release",
                        f"-DCMAKE_INSTALL_PREFIX={pmma_lib_dir}"
                    ], check=True, cwd=cmake_temp_dir, stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True)
    except subprocess.CalledProcessError as error:
        ts_print(f"Error configuring pmma: {error}")
        ts_print("Output before crash:")
        ts_print(error.output)
        abort = True
        return

    with open(config_log_file, "w") as f:
        f.write("Configuration log:\n")
        f.write(configure_result.stdout)

    # Build PMMA -------------------------------------------------------
    ts_print("Configuring PMMA complete...")
    ts_print("Building PMMA...")

    build_log_file = os.path.join(temporary_logging_dir, f"pmma-build.log")

    try:
        if build_debug:

            build_result = subprocess.run(
                [
                    "cmake", "--build", f"build/pmma", "--config", "Debug",
                    "--parallel"
                ], check=True, cwd=cmake_temp_dir, stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True)
        else:
            build_result = subprocess.run(
                [
                    "cmake", "--build", f"build/pmma", "--config", "Release",
                    "--parallel"
                ], check=True, cwd=cmake_temp_dir, stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True)
    except subprocess.CalledProcessError as error:
        ts_print(f"Error building pmma: {error}")
        ts_print("Output before crash:")
        ts_print(error.output)
        abort = True
        return

    with open(build_log_file, "w") as f:
        f.write("Build log:\n")
        f.write(build_result.stdout)

    ts_print("Finished PMMA C++ compilation")

def run_setup(in_github_workflow):
    global abort
    if abort:
        ts_print("Aborting Setup.py due to previous errors.")
        return

    ts_print("Started running Setup.py")

    setup_log_file = os.path.join(temporary_logging_dir, f"setup.log")

    try:
        if in_github_workflow:
            result = subprocess.run(
            [
                sys.executable, "setup.py", "build_ext", "--build-lib",
                "pmma/build", "--build-temp", "temporary", "sdist",
                "bdist_wheel"
            ], check=True, cwd=cmake_temp_dir, stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True)
        else:
            result = subprocess.run(
                [
                    sys.executable, "setup.py", "build_ext", "--build-lib",
                    "pmma/build", "--build-temp", "temporary", "sdist",
                    "bdist_wheel", "--no-parallel", "--annotate_build"
                ], check=True, cwd=cwd, stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True)
    except subprocess.CalledProcessError as error:
        ts_print(f"Error building cython component: {error}")
        ts_print("Output before crash:")
        ts_print(error.output)
        abort = True
        return

    with open(setup_log_file, "w") as f:
        f.write("Setup.py log:\n")
        f.write(result.stdout)

    ts_print("Finished running Setup.py")
    ts_print("Finished automated setup process!")

parser = argparse.ArgumentParser(description="Run in GitHub workflow mode")
parser.add_argument('-in_github_workflow', action='store_true', help='Run in GitHub workflow mode')
args = parser.parse_args()
in_github_workflow = args.in_github_workflow

build_debug = False
build_for_python = True

if not in_github_workflow:
    response = input(
        "Do you want to build a DEBUG version of PMMA? [y/n] \
(Recommended: n): ")
    if response == "":
        build_debug = False
    else:
        build_debug = response[0].lower() == "y"

if not in_github_workflow:
    response = input(
        "Do you want to build a C++ only version of PMMA (No Python \
interactions) [y/n] (Recommended: n): ")

    if response == "":
        build_for_python = True
    else:
        build_for_python = response[0].lower() == "n"

total_time = get_execution_time(build_pmma, build_debug, build_for_python)[0]
print(f"PMMA Build took {total_time:.2f} seconds")

total_time = get_execution_time(run_setup, in_github_workflow)[0]
print(f"Running Setup.py took {total_time:.2f} seconds")

if not in_github_workflow and not abort:
    response = input(
        "Do you want to automatically refresh the currently installed \
version of PMMA? [y/n] (Recommended: y): ")

    if response == "" or response[0].lower() == "y":
        ts_print("Refreshing the installed version of PMMA.")
        installation_log_file = os.path.join(
            temporary_logging_dir,
            f"installation.log")

        try:
            ts_print("Uninstalling PMMA...")
            uninstallation_result = subprocess.run(
            [
                sys.executable, "-m", "pip", "uninstall", "pmma", "-y"
            ], check=True, cwd=cmake_temp_dir, stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True)

            ts_print("Reinstalling PMMA...")
            wheel_path = os.path.join(cwd, "dist")
            for file in os.listdir(wheel_path):
                if file.endswith(".whl"):
                    wheel_file = os.path.join(wheel_path, file)
                    break

            installation_result = subprocess.run(
            [
                sys.executable, "-m", "pip", "install", wheel_file
            ], check=True, cwd=cmake_temp_dir, stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True)
        except subprocess.CalledProcessError as error:
            ts_print(f"Error installing pmma: {error}")
            ts_print("Output before crash:")
            ts_print(error.output)
        else:
            with open(installation_log_file, "w") as f:
                f.write("Installation log:\n")
                f.write(uninstallation_result.stdout)
                f.write(installation_result.stdout)

                ts_print("Finished refreshing the installed version of PMMA.")
                ts_print("Finished automated build process!")