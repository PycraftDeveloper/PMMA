#type: ignore

import os, threading

cwd = os.path.dirname(os.path.dirname(__file__))
pmma_dir = os.path.join(cwd, "pmma")
pmma_lib_dir = os.path.join(pmma_dir, "lib")
temp_dir = os.path.join(cwd, "temporary")
cmake_temp_dir = os.path.join(temp_dir, "cmake")
extern_dir = os.path.join(pmma_dir, "extern")
temporary_logging_dir = os.path.join(temp_dir, "cmake - logs")
cmake_dir = os.path.join(cwd, "build_tools", "cmake")
build_cache_dir = os.path.join(cwd, "build_cache")

print_lock = threading.Lock()
abort = False

def ts_print(content):
    with print_lock:
        print(content)