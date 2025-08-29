# type: ignore
import subprocess
import os
import shutil
import platform

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
        try:
            subprocess.run(
                [
                    "git", "worktree", "add", "../build_cache", branch_name
                ], check=True, cwd=cwd, stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True)
        except subprocess.CalledProcessError as error:
            print(f"❌ Error building {component}: {error}")
            print("🔍 Output before crash:")
            print(error.output)
            return
    else:
        shutil.rmtree(build_cache_dir, ignore_errors=True)
        shutil.copytree(build_tools_dir, build_cache_dir)

def update_cache_branch(in_github_workflow): # done
    if in_github_workflow:
        shutil.rmtree(build_cache_dir, ignore_errors=True)
        shutil.copy2(build_tools_dir, build_cache_dir)
        try:
            subprocess.run(
                [
                    "git", "add", "."
                ], check=True, cwd=build_cache_dir, stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True)
            subprocess.run(
                [
                    "git", "commit", "-m", f"Update build cache for {platform.system()} {platform.machine()}"
                ], check=True, cwd=build_cache_dir, stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True)
            subprocess.run(
                [
                    "git", "push", "origin", branch_name
                ], check=True, cwd=build_cache_dir, stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True)
        except subprocess.CalledProcessError as error:
            print(f"❌ Error updating branch: {error}")
            print("🔍 Output before crash:")
            print(error.output)
            return
    else:
        shutil.rmtree(build_cache_dir, ignore_errors=True)
        shutil.copytree(build_tools_dir, build_cache_dir)