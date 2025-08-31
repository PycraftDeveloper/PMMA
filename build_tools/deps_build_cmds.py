# type: ignore

import subprocess
import os
from utils import *
from deps_utils import *

def configure(self, component, in_github_workflow):
    folder = os.path.join(cwd, self.base_dir, component)
    ts_print(f"Configuring {component}...")

    config_log_file = os.path.join(temporary_logging_dir, f"dependencies/{component}-config.log")

    cmake_dependency_component_build_dir = os.path.join(cmake_dir, 'dependencies', component, 'build')

    run(
        [
            "cmake", "-S", folder, "-B", f"build/{component}",
            f"-DOUTPUT_DIR='{cmake_dependency_component_build_dir}'",
            "-DCMAKE_BUILD_TYPE=Release",
            f"-DINSTALL_DIR={extern_dir}"
        ], cmake_temp_dir, config_log_file, in_github_workflow
    )

    ts_print(f"Configured {component}")

def run_build(self, component, built, lock, indegree, ready, in_github_workflow):
    folder = os.path.join(cwd, self.base_dir, component)
    if self.configured[component].is_alive():
        ts_print(f"Waiting for {component} to finish configuring...")
        self.configured[component].join()

    ts_print(f"Building {component} in {folder}...")

    build_log_file = os.path.join(temporary_logging_dir, f"dependencies/{component}-build.log")

    run(
        [
            "cmake", "--build", f"build/{component}", "--config", "Release"
        ], cmake_temp_dir, build_log_file, in_github_workflow
    )

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