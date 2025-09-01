# type: ignore

import subprocess, sys, sysconfig, platform, argparse

from pmma_utils import *
from utils import *

os.makedirs(cmake_temp_dir, exist_ok=True)
os.makedirs(extern_dir, exist_ok=True)
os.makedirs(temporary_logging_dir, exist_ok=True)
os.makedirs(join_path(temporary_logging_dir, "dependencies"), exist_ok=True)
os.makedirs(pmma_lib_dir, exist_ok=True)

def build_pmma(build_debug, build_for_python):
    folder = join_path(cwd, "build_tools", "cmake", "pmma")

    # Configure PMMA ---------------------------------------------------
    ts_print("Configuring PMMA...")

    config_log_file = join_path(temporary_logging_dir, f"pmma-config.log")
    if build_debug:
        if build_for_python:
            python_executable_path = sys.executable

            ts_print(f"Using '{python_executable_path}'")
            run(
                [
                    "cmake", "-S", folder, "-B", f"build/pmma",
                    f"-DWORKING_DIR={cwd}", "-DCMAKE_BUILD_TYPE=Debug",
                    f"-DPython3_EXECUTABLE={python_executable_path}",
                    "-DUSE_PYTHON=ON",
                    f"-DCMAKE_INSTALL_PREFIX={pmma_lib_dir}"
                ],
                cmake_temp_dir,
                config_log_file,
                in_github_workflow
            )
        else:
            run(
                [
                    "cmake", "-S", folder, "-B", f"build/pmma",
                    f"-DWORKING_DIR={cwd}", "-DCMAKE_BUILD_TYPE=Debug",
                    f"-DCMAKE_INSTALL_PREFIX={pmma_lib_dir}"
                ],
                cmake_temp_dir,
                config_log_file,
                in_github_workflow
            )
    else:
        if build_for_python:
            python_executable_path = sys.executable

            ts_print(f"Using '{python_executable_path}'")
            run(
                [
                    "cmake", "-S", folder, "-B", f"build/pmma",
                    f"-DWORKING_DIR={cwd}", "-DCMAKE_BUILD_TYPE=Release",
                    f"-DPython3_EXECUTABLE={python_executable_path}",
                    "-DUSE_PYTHON=ON",
                    f"-DCMAKE_INSTALL_PREFIX={pmma_lib_dir}"
                ],
                cmake_temp_dir,
                config_log_file,
                in_github_workflow
            )
        else:
            run(
                [
                    "cmake", "-S", folder, "-B", f"build/pmma",
                    f"-DWORKING_DIR={cwd}", "-DCMAKE_BUILD_TYPE=Release",
                    f"-DCMAKE_INSTALL_PREFIX={pmma_lib_dir}"
                ],
                cmake_temp_dir,
                config_log_file,
                in_github_workflow
            )

    # Build PMMA -------------------------------------------------------
    ts_print("Configuring PMMA complete...")
    ts_print("Building PMMA...")

    build_join_path(temporary_logging_dir, f"pmma-build.log")

    if build_debug:
        run(
            [
                "cmake", "--build", f"build/pmma", "--config", "Debug",
                "--parallel"
            ], cmake_temp_dir, build_log_file, in_github_workflow)
    else:
        run(
            [
                "cmake", "--build", f"build/pmma", "--config", "Release",
                "--parallel"
            ], cmake_temp_dir, build_log_file, in_github_workflow
        )

    ts_print("Finished PMMA C++ compilation")

def run_setup(in_github_workflow):
    ts_print("Started running Setup.py")

    setup_log_file = join_path(temporary_logging_dir, f"setup.log")

    if in_github_workflow:
        run(
            [
            sys.executable, "setup.py", "build_ext", "--build-lib",
            "pmma/build", "--build-temp", "temporary", "sdist",
            "bdist_wheel"
            ],
            cwd, setup_log_file, in_github_workflow
        )
    else:
        run(
            [
            sys.executable, "setup.py", "build_ext", "--build-lib",
            "pmma/build", "--build-temp", "temporary", "sdist",
            "bdist_wheel", "--no-parallel", "--annotate_build"
            ],
            cwd, setup_log_file, in_github_workflow
        )

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

if not in_github_workflow:
    response = input(
        "Do you want to automatically refresh the currently installed \
version of PMMA? [y/n] (Recommended: y): ")

    if response == "" or response[0].lower() == "y":
        ts_print("Refreshing the installed version of PMMA.")
        installation_log_file = join_path(
            temporary_logging_dir,
            f"installation.log")

        ts_print("Uninstalling PMMA...")
        run(
            [
            sys.executable, "-m", "pip", "uninstall", "pmma", "-y"
            ], cmake_temp_dir, installation_log_file, in_github_workflow
        )

        ts_print("Reinstalling PMMA...")
        wheel_path = join_path(cwd, "dist")
        for file in os.listdir(wheel_path):
            if file.endswith(".whl"):
                wheel_file = join_path(wheel_path, file)
                break

        run(
            [
            sys.executable, "-m", "pip", "install", wheel_file
            ], cmake_temp_dir, installation_log_file, in_github_workflow
        )

        ts_print("Finished refreshing the installed version of PMMA.")
        ts_print("Finished automated build process!")