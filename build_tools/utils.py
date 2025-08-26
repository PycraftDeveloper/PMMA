# type: ignore

import subprocess
from collections import deque
import os
import threading

cwd = os.path.dirname(os.path.dirname(__file__))
pmma_dir = os.path.join(cwd, "pmma")
temp_dir = os.path.join(cwd, "temporary")
cmake_temp_dir = os.path.join(temp_dir, "cmake")
extern_dir = os.path.join(pmma_dir, "extern")
temporary_logging_dir = os.path.join(temp_dir, "cmake - logs")

os.makedirs(cmake_temp_dir, exist_ok=True)
os.makedirs(extern_dir, exist_ok=True)
os.makedirs(temporary_logging_dir, exist_ok=True)
os.makedirs(os.path.join(temporary_logging_dir, "dependencies"), exist_ok=True)

print_lock = threading.Lock()

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
            print(f"❌ Error configuring {component}: {error}")
            print("🔍 Output before crash:")
            print(error.output)

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
                print(f"❌ Error building {component}: {error}")
                print("🔍 Output before crash:")
                print(error.output)

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

            # Clean finished threads
            threads = [t for t in threads if t.is_alive()]

        print("🎉 All dependencies built successfully.")

def build_pmma():
    folder = os.path.join(cwd, "build_tools/cmake", "pmma")

    # Configure PMMA ---------------------------------------------------
    with print_lock:
        print("⚙️ Configuring PMMA...")

    config_log_file = os.path.join(temporary_logging_dir, f"pmma-config.log")
    try:
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

    with open(config_log_file, "w") as f:
        f.write("Configuration log:\n")
        f.write(configure_result.stdout)

    # Build PMMA -------------------------------------------------------
    with print_lock:
        print("⚙️ Configuring PMMA complete...")
        print("🔨 Building PMMA...")

    build_log_file = os.path.join(temporary_logging_dir, f"pmma-build.log")

    try:
        build_result = subprocess.run(
            [
                "cmake", "--build", f"build/pmma", "--config", "Release"
            ], check=True, cwd=cmake_temp_dir, stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True)
    except subprocess.CalledProcessError as error:
        print(f"❌ Error building pmma: {error}")
        print("🔍 Output before crash:")
        print(error.output)

    with open(build_log_file, "w") as f:
        f.write("Build log:\n")
        f.write(build_result.stdout)

    with print_lock:
        print("✅ Finished PMMA")