# type: ignore

import subprocess, multiprocessing
import os
from utils import *
from deps_utils import *

def configure(self, component):
    folder = join_path(cwd, self.base_dir, component)
    ts_print(f"Internally setting up build environment for: '{component}'...")

    config_log_file = join_path(temporary_logging_dir, f"dependencies/{component}-config.log")

    cmake_dependency_component_build_dir = join_path(cmake_dir, 'dependencies', component, 'build')

    run(
        [
            "cmake", "-S", folder, "-B", f"build/{component}",
            f"-DOUTPUT_DIR='{cmake_dependency_component_build_dir}'",
            "-DCMAKE_BUILD_TYPE=Release",
            f"-DINSTALL_DIR={extern_dir}",
            "-DCMAKE_UNITY_BUILD=ON",
            f"-DCMAKE_BUILD_PARALLEL_LEVEL={multiprocessing.cpu_count}"
        ], cmake_temp_dir, config_log_file
    )

    ts_print(f"Internally setup build environment for: '{component}'")

def run_build(self, component, built, lock, indegree, ready):
    folder = join_path(cwd, self.base_dir, component)
    if self.configured[component].is_alive():
        ts_print(f"Waiting for {component} to finish configuring...")
        self.configured[component].join()

    ts_print(f"Building '{component}' in '{folder}'...")

    build_log_file = join_path(temporary_logging_dir, f"dependencies/{component}-build.log")

    run(
        [
            "cmake", "--build", f"build/{component}", "--config", "Release"
        ], cmake_temp_dir, build_log_file
    )

    merge_all_subdirs(
        join_path(cmake_dir, 'dependencies', component, 'build'),
        extern_dir)

    ts_print(f"Finished '{component}'")

    # Mark as built and unlock dependents
    with lock:
        built.add(component)
        for dep, deps in self.components.items():
            if component in deps:
                indegree[dep] -= 1
                if indegree[dep] == 0:
                    ready.append(dep)