# type: ignore

import subprocess
import os
from utils import *
from deps_utils import *

def configure(self, component):
    global abort
    folder = os.path.join(cwd, self.base_dir, component)
    ts_print(f"Configuring {component}...")

    config_log_file = os.path.join(temporary_logging_dir, f"dependencies/{component}-config.log")

    try:
        cmake_dependency_component_build_dir = os.path.join(cmake_dir, 'dependencies', component, 'build')
        configure_result = subprocess.run(
            [
                "cmake", "-S", folder, "-B", f"build/{component}",
                f"-DOUTPUT_DIR='{cmake_dependency_component_build_dir}'",
                "-DCMAKE_BUILD_TYPE=Release",
                f"-DINSTALL_DIR={extern_dir}"
            ], check=True, cwd=cmake_temp_dir, stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True)
    except subprocess.CalledProcessError as error:
        abort = True
        ts_print(f"Error configuring {component}: {error}")
        ts_print("Output before crash:")
        ts_print(error.output)
        return

    with open(config_log_file, "w") as f:
        f.write("Configuration log:\n")
        f.write(configure_result.stdout)

    ts_print(f"Configured {component}")

def run_build(self, component, built, lock, indegree, ready):
    global abort
    folder = os.path.join(cwd, self.base_dir, component)
    if self.configured[component].is_alive():
        ts_print(f"Waiting for {component} to finish configuring...")
        self.configured[component].join()

    ts_print(f"Building {component} in {folder}...")

    build_log_file = os.path.join(temporary_logging_dir, f"dependencies/{component}-build.log")

    try:
        build_result = subprocess.run(
            [
                "cmake", "--build", f"build/{component}", "--config", "Release"
            ], check=True, cwd=cmake_temp_dir, stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True)
    except subprocess.CalledProcessError as error:
        abort = True
        ts_print(f"Error building {component}: {error}")
        ts_print("Output before crash:")
        ts_print(error.output)
        return

    with open(build_log_file, "w") as f:
        f.write("Build log:\n")
        f.write(build_result.stdout)

    merge_all_subdirs(
        os.path.join(cmake_dir, 'dependencies', component, 'build'),
        extern_dir)

    ts_print(f"Finished {component}")

    # Mark as built and unlock dependents
    with lock:
        built.add(component)
        for dep, deps in self.components.items():
            if component in deps:
                indegree[dep] -= 1
                if indegree[dep] == 0:
                    ready.append(dep)