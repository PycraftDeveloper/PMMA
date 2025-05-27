import subprocess
import sys
import os
import shutil

cwd = os.path.dirname(__file__)

build_dir = os.path.join(cwd, "pmma_dev", "build")
temp_dir = os.path.join(cwd, "pmma_dev", "temporary")

subprocess.check_output([
    sys.executable,
    os.path.join(cwd, "setup.py"),
    "build_ext",
    "--build-lib",
    build_dir,
    "--build-temp",
    temp_dir])

sys.path.insert(0, build_dir)

from pmma_dev.mywrapper import *