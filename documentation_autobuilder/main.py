import os
import glob

def _up(path: str) -> str:
    return path[::-1].split(os.sep, 1)[-1][::-1]

def path_builder(*args):
    result = ""
    for arg in args:
        result += arg
        result += os.sep
    result = result[:-1]
    return result

base_path = _up(_up(__file__))

python_source_code_path = path_builder(base_path, "python_src")
documentation_path = path_builder(base_path, "docs")
temporary_documentation_path = path_builder(base_path, "temp_docs")

files = glob.glob(python_source_code_path + os.sep + "*.py")

index_start = """
Library Breakdown
=========

The full breakdown of what everything does!

.. toctree::
    :maxdepth: 2

"""

with open(path_builder(temporary_documentation_path, "index.rst"), "w") as open_file:
    open_file.write(index_start)

for file in files:
    print(file)
    filename = os.path.basename(file).split(".")[0]
    open(path_builder(temporary_documentation_path, filename+".rst"), "w").close()
    #with open(path_builder(temporary_documentation_path, "index.rst"), "a") as open_file:

    with open(file, "r") as open_file:
        content = open_file.readlines()

    in_class = False
    for line in content:
        if "class " in line and ":" in line:
            class_name = line.split(" ")[1].split(":")[0]
            class_name = class_name.strip()
            in_class = True
            print("class: ", class_name)

        if "def " in line and ":" in line:
            function_name = line.split("def ")[1].split(":")[0]
            indent_level = line.split("def")[0]
            indent_level_count = len(indent_level) // 4
            function_name = function_name.strip()
            if in_class and indent_level_count == 1:
                print("method: ", function_name)
            else:
                print("function: ", function_name)