import shutil
import os
import site
import subprocess
import sys

cwd = os.path.dirname(__file__)

build_dir = os.path.join(cwd, "pmma", "build")
temp_dir = os.path.join(cwd, "pmma", "temporary")

print("Building PMMA...")
subprocess.check_output([
    sys.executable,
    os.path.join(cwd, "setup.py"),
    "build_ext",
    "--build-lib",
    build_dir,
    "--build-temp",
    temp_dir])

SITE_PACKAGE_DIR = site.getsitepackages()[-1]

print("Removing old version of PMMA...")
shutil.rmtree(os.path.join(SITE_PACKAGE_DIR, 'pmma'))

current_dir = os.path.dirname(os.path.abspath(__file__))

print("Copying new version of PMMA...")
shutil.copytree(os.path.join(current_dir, 'pmma'), os.path.join(SITE_PACKAGE_DIR, 'pmma'))

print("Copying __init__.py...")
shutil.copy(os.path.join(current_dir, '__init__.py'), os.path.join(SITE_PACKAGE_DIR, 'pmma', '__init__.py'))