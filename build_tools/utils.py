#type: ignore

import os, threading
import subprocess, sys, shutil, pathlib

def join_path(cwd, *components):
    print(pathlib.Path(cwd, *components).as_posix())
    return pathlib.Path(cwd, *components).as_posix()

cwd = os.path.dirname(os.path.dirname(__file__))
pmma_dir = join_path(cwd, "pmma")
pmma_lib_dir = join_path(pmma_dir, "lib")
temp_dir = join_path(cwd, "temporary")
cmake_temp_dir = join_path(temp_dir, "cmake")
extern_dir = join_path(pmma_dir, "extern")
temporary_logging_dir = join_path(temp_dir, "cmake - logs")
cmake_dir = join_path(cwd, "build_tools", "cmake")
build_cache_dir = join_path(cwd, "build_cache")

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

def copy_top_level(src_dir, dst_dir):
    for item in os.listdir(src_dir):
        src_path = join_path(src_dir, item)
        dst_path = join_path(dst_dir, item)

        if os.path.isfile(src_path):
            shutil.copy2(src_path, dst_path)
        elif os.path.isdir(src_path):
            # Copy the entire subdirectory (recursively)
            shutil.copytree(src_path, dst_path, dirs_exist_ok=True)