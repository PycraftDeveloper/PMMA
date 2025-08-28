# type: ignore

from utils import *

in_github_workflow = os.environ.get("GITHUB_ACTIONS") == "true"
build_debug = False

if not in_github_workflow:
    os.system('cls' if os.name == 'nt' else 'clear')

    response = user_input(
    "Do you want to build a DEBUG version of PMMA? [y/N]: ",
    "n",
    5)

    build_debug = response[0].lower() == "y"

total_time = get_execution_time(build_pmma, build_debug)[0]
print(f"🕒 PMMA Build took {total_time:.2f} seconds")

total_time = get_execution_time(run_setup, in_github_workflow)[0]
print(f"🕒 Running Setup.py took {total_time:.2f} seconds")