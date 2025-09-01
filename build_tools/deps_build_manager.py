# type: ignore

from collections import deque

from deps_utils import *
from deps_build_cmds import *
from utils import *

class DependencyBuildManager:
    def __init__(self, in_github_workflow, base_dir="build_tools/cmake/dependencies"):
        self.base_dir = base_dir
        self.components = {}
        self.configured = {}
        self.in_github_workflow = in_github_workflow

    def add_component(self, name, dependencies=None):
        if dependencies is None:
            dependencies = []

        global components
        components.append(name)

        rebuild = False

        if not os.path.exists(join_path(cmake_build_cache_dir, 'dependencies', name, 'build')):
            rebuild = True
            ts_print(f"{name} needs rebuild because it has no existing build cached build.")

        if not rebuild and previous_hashes == {}:
            rebuild = True
            ts_print(f"{name} needs rebuild because there is no previous hash data.")

        if not rebuild:
            copied_dependencies = dependencies
            dependencies = []
            for dependant in copied_dependencies:
                if rebuild_control[dependant]:
                    rebuild = True
                    dependencies.append(dependant)

            if rebuild:
                ts_print(f"{name} needs rebuild because {dependant} was rebuilt.")

        if not rebuild and name in previous_hashes:
            if hash_component(name) == previous_hashes[name]:
                ts_print(f"Skipping {name}, no changes detected.")
                merge_all_subdirs(
                    join_path(build_cache_dir, 'cmake', 'dependencies', name, 'build'),
                    extern_dir)
                rebuild_control[name] = False
                return

        shutil.rmtree(join_path(cmake_dir, 'dependencies', name, 'build'), ignore_errors=True)

        rebuild_control[name] = True

        self.components[name] = dependencies

        configure_thread = threading.Thread(
            target=configure,
            args=(self, name, self.in_github_workflow,))

        configure_thread.start()
        self.configured[name] = configure_thread

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
            ts_print(f"Circular dependency detected: {' -> '.join(cycle)}")
            return

        # Build reverse dependency graph (who depends on me)
        indegree = {comp: len(deps) for comp, deps in self.components.items()}
        ready = deque([c for c, d in indegree.items() if d == 0])

        built = set()
        lock = threading.Lock()

        threads = []
        while ready or any(t.is_alive() for t in threads):
            while ready:
                comp = ready.popleft()
                t = threading.Thread(
                    target=run_build,
                    args=(self, comp, built, lock, indegree, ready, self.in_github_workflow))
                t.start()
                threads.append(t)

            # Clean finished threads
            threads = [t for t in threads if t.is_alive()]

        ts_print("All dependencies built successfully.")