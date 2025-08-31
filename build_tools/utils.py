#type: ignore

import os, threading
import subprocess, sys

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

def ts_print(content):
    with print_lock:
        print(content)

def run(command, cwd, log_file, in_github_workflow):
    try:
        result = subprocess.run(
            [*command], check=True, cwd=cwd, stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True)
    except subprocess.CalledProcessError as error:
        ts_print(f"Error running {command}: {error}")
        ts_print("Output before crash:")
        ts_print(error.output)
        sys.exit(-1)

    if in_github_workflow:
        ts_print(result.stdout)
    else:
        joined_command = " ".join(command)

        with open(log_file, "a") as f:
            f.write(f"{joined_command} log:\n")
            f.write(result.stdout)