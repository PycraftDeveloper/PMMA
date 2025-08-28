# type: ignore

import subprocess
from collections import deque
import os
import threading
import sys
from pathlib import Path
import shutil
import time
import json
import hashlib

cwd = os.path.dirname(os.path.dirname(__file__))
pmma_dir = os.path.join(cwd, "pmma")
pmma_lib_dir = os.path.join(pmma_dir, "lib")
temp_dir = os.path.join(cwd, "temporary")
cmake_temp_dir = os.path.join(temp_dir, "cmake")
extern_dir = os.path.join(pmma_dir, "extern")
temporary_logging_dir = os.path.join(temp_dir, "cmake - logs")
cmake_dir = os.path.join(cwd, "build_tools", "cmake")

print_lock = threading.Lock()
abort = False
components = []
previous_hashes = {}
rebuild_control = {}
hash_path = os.path.join(cwd, "build_tools", "hashes.json")
if os.path.exists(hash_path):
    with open(hash_path, "r") as file:
        previous_hashes = json.load(file)

def hash_component(name):
    build_tools_dir = os.path.join(cwd, "build_tools")
    data = ""

    #with open(os.path.join(build_tools_dir, "main.py"), "r", encoding="utf-8") as file:
        #data += file.read()

    with open(os.path.join(build_tools_dir, "utils.py"), "r", encoding="utf-8") as file:
        data += file.read()

    with open(os.path.join(cmake_dir, "dependencies", name, "CMakeLists.txt"), "r", encoding="utf-8") as file:
        data += file.read()

    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def merge_all_subdirs(src_root, dest_root):
    src_root = Path(src_root)
    dest_root = Path(dest_root)

    if not src_root.exists():
        print(f"Source directory {src_root} does not exist.")
        return

    for src_subdir in src_root.iterdir():
        if not src_subdir.is_dir():
            continue  # Skip files at the root level

        dest_subdir = dest_root / src_subdir.name
        dest_subdir.mkdir(parents=True, exist_ok=True)

        for item in src_subdir.rglob('*'):
            relative_path = item.relative_to(src_subdir)
            dest_item = dest_subdir / relative_path

            if item.is_dir():
                dest_item.mkdir(parents=True, exist_ok=True)
            else:
                dest_item.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, dest_item)

        print(f"↪️ Merged {src_subdir} → {dest_subdir}")

def get_execution_time(function, *args, **kwargs):
    start_time = time.perf_counter()
    result = function(*args, **kwargs)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return execution_time, result

def ts_print(content):
    with print_lock:
        print(content)

def user_input(prompt, default, timeout):
    result = [default]

    def ask():
        user_response = input(prompt)
        result[0] = user_response

    thread = threading.Thread(target=ask)
    thread.daemon = True
    thread.start()
    thread.join(timeout)
    print("\n", end="")

    return result[0]

def selectively_clean_extern():
    if os.path.exists(extern_dir):
        def should_keep(path):
            return (f'include{os.sep}glm' in path or
                    f'include{os.sep}glad' in path or
                    f'include{os.sep}FlatHashMap' in path or
                    f'include{os.sep}STB' in path)

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
                    ts_print(f"Could not delete directory: {item_path} - {e}")

class DependencyBuildManager:
    def __init__(self, base_dir="build_tools/cmake/dependencies"):
        self.base_dir = base_dir
        self.components = {}
        self.configured = {}

    def add_component(self, name, dependencies=None):
        if dependencies is None:
            dependencies = []

        global components
        components.append(name)

        rebuild = False

        if not os.path.exists(os.path.join(cmake_dir, 'dependencies', name, 'build')):
            rebuild = True

        if previous_hashes == {}:
            rebuild = True

        if not rebuild:
            for dependant in dependencies:
                rebuild |= rebuild_control[dependant]
                if rebuild:
                    ts_print(f"♻️ {name} needs rebuild because {dependant} was rebuilt.")
                    break

            if name in previous_hashes:
                if hash_component(name) == previous_hashes[name]:
                    ts_print(f"✅ Skipping {name}, no changes detected.")
                    merge_all_subdirs(
                        os.path.join(cmake_dir, 'dependencies', name, 'build'),
                        extern_dir)
                    rebuild_control[name] = False
                    return

        shutil.rmtree(os.path.join(cmake_dir, 'dependencies', name, 'build'), ignore_errors=True)

        rebuild_control[name] = True

        self.components[name] = dependencies

        configure_thread = threading.Thread(target=self.configure, args=(name,))
        self.configured[name] = configure_thread
        configure_thread.start()

    def configure(self, component):
        global abort
        folder = os.path.join(cwd, self.base_dir, component)
        ts_print(f"⚙️ Configuring {component}...")

        config_log_file = os.path.join(temporary_logging_dir, f"dependencies/{component}-config.log")

        try:
            configure_result = subprocess.run(
                [
                    "cmake", "-S", folder, "-B", f"build/{component}",
                    f"-DOUTPUT_DIR='{os.path.join(cmake_dir, 'dependencies', component, 'build')}'",
                    "-DCMAKE_BUILD_TYPE=Release",
                    f"-DINSTALL_DIR={extern_dir}"
                ], check=True, cwd=cmake_temp_dir, stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True)
        except subprocess.CalledProcessError as error:
            abort = True
            ts_print(f"❌ Error configuring {component}: {error}")
            ts_print("🔍 Output before crash:")
            ts_print(error.output)
            return

        with open(config_log_file, "w") as f:
            f.write("Configuration log:\n")
            f.write(configure_result.stdout)

        ts_print(f"⚙️ Configured {component}")

    def detect_cycles(self):
        """Detect circular dependencies using DFS."""
        visited = {}
        cycle = []

        def dfs(node, stack):
            if node in stack:
                cycle.extend(stack[stack.index(node):])
                return True
            if node in visited:
                return False

            stack.append(node)
            visited[node] = True
            for dep in self.components.get(node, []):
                if dfs(dep, stack):
                    return True
            stack.pop()
            return False

        for comp in self.components:
            if dfs(comp, []):
                return cycle
        return None

    def build(self):
        # Check for cycles first
        cycle = self.detect_cycles()
        if cycle:
            ts_print(f"⚠️ Circular dependency detected: {' -> '.join(cycle)}")
            return

        # Build reverse dependency graph (who depends on me)
        indegree = {comp: len(deps) for comp, deps in self.components.items()}
        ready = deque([c for c, d in indegree.items() if d == 0])

        built = set()
        lock = threading.Lock()

        def run_build(component):
            global abort
            folder = os.path.join(cwd, self.base_dir, component)
            if self.configured[component].is_alive():
                ts_print(f"⏳ Waiting for {component} to finish configuring...")
                self.configured[component].join()

            ts_print(f"🔨 Building {component} in {folder}...")

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
                ts_print(f"❌ Error building {component}: {error}")
                ts_print("🔍 Output before crash:")
                ts_print(error.output)
                return

            with open(build_log_file, "w") as f:
                f.write("Build log:\n")
                f.write(build_result.stdout)

            merge_all_subdirs(
                os.path.join(cmake_dir, 'dependencies', component, 'build'),
                extern_dir)

            ts_print(f"✅ Finished {component}")

            # Mark as built and unlock dependents
            with lock:
                built.add(component)
                for dep, deps in self.components.items():
                    if component in deps:
                        indegree[dep] -= 1
                        if indegree[dep] == 0:
                            ready.append(dep)

        threads = []
        while ready or any(t.is_alive() for t in threads):
            while ready:
                comp = ready.popleft()
                t = threading.Thread(target=run_build, args=(comp,))
                t.start()
                threads.append(t)

            if abort:
                ts_print("❌ Aborting build due to errors.")
                break

            # Clean finished threads
            threads = [t for t in threads if t.is_alive()]

        if not abort:
            ts_print("🎉 All dependencies built successfully.")

def build_pmma(build_debug):
    if abort:
        ts_print("❌ Aborting PMMA build due to previous errors.")
        return

    folder = os.path.join(cwd, "build_tools/cmake", "pmma")

    # Configure PMMA ---------------------------------------------------
    ts_print("⚙️ Configuring PMMA...")

    config_log_file = os.path.join(temporary_logging_dir, f"pmma-config.log")
    try:
        if build_debug:
            configure_result = subprocess.run(
                [
                    "cmake", "-S", folder, "-B", f"build/pmma",
                    f"-DWORKING_DIR='{cwd}'", "-DCMAKE_BUILD_TYPE=Debug"
                ], check=True, cwd=cmake_temp_dir, stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True)
        else:
            configure_result = subprocess.run(
                [
                    "cmake", "-S", folder, "-B", f"build/pmma",
                    f"-DWORKING_DIR='{cwd}'", "-DCMAKE_BUILD_TYPE=Release"
                ], check=True, cwd=cmake_temp_dir, stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True)
    except subprocess.CalledProcessError as error:
        ts_print(f"❌ Error configuring pmma: {error}")
        ts_print("🔍 Output before crash:")
        ts_print(error.output)
        return

    with open(config_log_file, "w") as f:
        f.write("Configuration log:\n")
        f.write(configure_result.stdout)

    # Build PMMA -------------------------------------------------------
    ts_print("⚙️ Configuring PMMA complete...")
    ts_print("🔨 Building PMMA...")

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
        ts_print(f"❌ Error building pmma: {error}")
        ts_print("🔍 Output before crash:")
        ts_print(error.output)
        return

    with open(build_log_file, "w") as f:
        f.write("Build log:\n")
        f.write(build_result.stdout)

    ts_print("🎉 Finished PMMA")

def run_setup(in_github_workflow):
    if abort:
        ts_print("❌ Aborting Setup.py due to previous errors.")
        return

    ts_print("⏳ Started running Setup.py")

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
        ts_print(f"❌ Error building cython component: {error}")
        ts_print("🔍 Output before crash:")
        ts_print(error.output)
        return

    with open(setup_log_file, "w") as f:
        f.write("Setup.py log:\n")
        f.write(result.stdout)

    ts_print("✅ Finished running Setup.py")
    ts_print("🎉 Finished automated setup process!")