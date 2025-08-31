# type: ignore
import subprocess
import os, shutil, platform

from utils import *

# get the cache branch (or make it if it doesnt exist)
# ---
# compare cache to current configuration
# update build
# ---
# clear previous build cache
# write new build cache
# commit the build cache

cwd = os.path.dirname(os.path.dirname(__file__))
build_tools_dir = os.path.join(cwd, "build_tools")
build_cache_dir = os.path.join(cwd, "build_cache")

branch_name = f"{platform.system().lower()}_{platform.machine().lower()}_build_cache"

def fetch_cache_branch(in_github_workflow):
    if in_github_workflow:
        pass # defined in the github workflow
    else:
        shutil.rmtree(build_cache_dir, ignore_errors=True)
        shutil.copytree(build_tools_dir, build_cache_dir)

def update_cache_branch(in_github_workflow): # done
    if in_github_workflow:
        pass # defined in the github workflow
    else:
        shutil.rmtree(build_cache_dir, ignore_errors=True)
        shutil.copytree(build_tools_dir, build_cache_dir)