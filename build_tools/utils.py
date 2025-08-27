# type: ignore

import subprocess
from collections import deque
import os
import threading
import sys

cwd = os.path.dirname(os.path.dirname(__file__))
pmma_dir = os.path.join(cwd, "pmma")
pmma_lib_dir = os.path.join(pmma_dir, "lib")
temp_dir = os.path.join(cwd, "temporary")
cmake_temp_dir = os.path.join(temp_dir, "cmake")
extern_dir = os.path.join(pmma_dir, "extern")
temporary_logging_dir = os.path.join(temp_dir, "cmake - logs")

print_lock = threading.Lock()
abort = False

def user_input(prompt, default, timeout):
    result = [default]

    def ask():
        user_response = input(prompt)
        result[0] = user_response

    thread = threading.Thread(target=ask)
    thread.daemon = True
    thread.start()
    thread.join(timeout)

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
                    print("Could not delete directory:", item_path, "-", e)

class DependencyBuildManager:
    def __init__(self, base_dir="build_tools/cmake/dependencies"):
        self.base_dir = base_dir
        self.components = {}
        self.configured = {}

    def add_component(self, name, dependencies=None):
        if dependencies is None:
            dependencies = []
        self.components[name] = dependencies

        configure_thread = threading.Thread(target=self.configure, args=(name,))
        self.configured[name] = configure_thread
        configure_thread.start()

    def configure(self, component):
        global abort
        folder = os.path.join(cwd, self.base_dir, component)
        with print_lock:
            print(f"⚙️ Configuring {component}...")

        config_log_file = os.path.join(temporary_logging_dir, f"dependencies/{component}-config.log")

        try:
            configure_result = subprocess.run(
                [
                    "cmake", "-S", folder, "-B", f"build/{component}",
                    f"-DOUTPUT_DIR='{extern_dir}'", "-DCMAKE_BUILD_TYPE=Release"
                ], check=True, cwd=cmake_temp_dir, stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True)
        except subprocess.CalledProcessError as error:
            abort = True
            print(f"❌ Error configuring {component}: {error}")
            print("🔍 Output before crash:")
            print(error.output)
            return

        with open(config_log_file, "w") as f:
            f.write("Configuration log:\n")
            f.write(configure_result.stdout)

        with print_lock:
            print(f"⚙️ Configured {component}")

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
            print(f"⚠️ Circular dependency detected: {' -> '.join(cycle)}")
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
                with print_lock:
                    print(f"⏳ Waiting for {component} to finish configuring...")
                self.configured[component].join()

            with print_lock:
                print(f"🔨 Building {component} in {folder}...")

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
                print(f"❌ Error building {component}: {error}")
                print("🔍 Output before crash:")
                print(error.output)
                return

            with open(build_log_file, "w") as f:
                f.write("Build log:\n")
                f.write(build_result.stdout)

            with print_lock:
                print(f"✅ Finished {component}")

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
                print("❌ Aborting build due to errors.")
                break

            # Clean finished threads
            threads = [t for t in threads if t.is_alive()]

        if not abort:
            with print_lock:
                print("🎉 All dependencies built successfully.")

def build_pmma(build_debug):
    if abort:
        print("❌ Aborting PMMA build due to previous errors.")
        return

    folder = os.path.join(cwd, "build_tools/cmake", "pmma")

    # Configure PMMA ---------------------------------------------------
    with print_lock:
        print("⚙️ Configuring PMMA...")

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
        print(f"❌ Error configuring pmma: {error}")
        print("🔍 Output before crash:")
        print(error.output)
        return

    with open(config_log_file, "w") as f:
        f.write("Configuration log:\n")
        f.write(configure_result.stdout)

    # Build PMMA -------------------------------------------------------
    with print_lock:
        print("⚙️ Configuring PMMA complete...")
        print("🔨 Building PMMA...")

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
        print(f"❌ Error building pmma: {error}")
        print("🔍 Output before crash:")
        print(error.output)
        return

    with open(build_log_file, "w") as f:
        f.write("Build log:\n")
        f.write(build_result.stdout)

    with print_lock:
        print("🎉 Finished PMMA")

def run_setup(in_github_workflow):
    if abort:
        print("❌ Aborting Setup.py due to previous errors.")
        return

    with print_lock:
        print("⏳ Started running Setup.py")

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
        print(f"❌ Error building cython component: {error}")
        print("🔍 Output before crash:")
        print(error.output)
        return

    with open(setup_log_file, "w") as f:
        f.write("Setup.py log:\n")
        f.write(result.stdout)

    with print_lock:
        print("✅ Finished running Setup.py")
        print("🎉 Finished automated setup process!")