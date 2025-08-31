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
        run(
            ["git", "config", "--global", "--add", "safe.directory", cwd],
            build_cache_dir, None, in_github_workflow
        )

        try:
            subprocess.run(
                ["git", "clone", "-b", branch_name, "--single-branch", ".", "build_cache"],
                check=True, cwd=cwd, stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT, text=True)
        except subprocess.CalledProcessError:
            run(
                ["git", "checkout", "--orphan", branch_name],
                cwd, None, in_github_workflow
            )
            run(
                ["git", "rm", "-rf", "."],
                cwd, None, in_github_workflow
            )
            run(
                ["git", "commit", "--allow-empty", "-m", "Initial commit"],
                cwd, None, in_github_workflow
            )
            run(
                ["git", "push", "-u", "origin", branch_name]
            )
            run(
                ["git", "checkout", "main"],
                cwd, None, in_github_workflow
            )
            run(
                ["git", "clone", "-b", branch_name, "--single-branch", ".", "build_cache"],
                cwd, None, in_github_workflow)
    else:
        shutil.rmtree(build_cache_dir, ignore_errors=True)
        shutil.copytree(build_tools_dir, build_cache_dir)

def update_cache_branch(in_github_workflow): # done
    if in_github_workflow:
        shutil.rmtree(build_cache_dir, ignore_errors=True)
        shutil.copytree(build_tools_dir, build_cache_dir)
        run(
            ["git", "config", "user.email", "github-actions@github.com"],
            build_cache_dir, None, in_github_workflow
        )
        run(
            ["git", "config", "user.name", "GitHub Actions"],
            build_cache_dir, None, in_github_workflow
        )
        run(
            ["git", "add", "."],
            build_cache_dir, None, in_github_workflow
        )
        run(
            [
                "git", "commit", "-m",
                f"Update build cache for {platform.system()} {platform.machine()}"],
            build_cache_dir, None, in_github_workflow
        )
        run(
            ["git", "push", "-u", "origin", branch_name],
            build_cache_dir, None, in_github_workflow
        )
    else:
        shutil.rmtree(build_cache_dir, ignore_errors=True)
        shutil.copytree(build_tools_dir, build_cache_dir)