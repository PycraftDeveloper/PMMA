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

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

base_path = _up(_up(__file__))

python_source_code_path = path_builder(base_path, "python_src")
documentation_path = path_builder(base_path, "docs")
temporary_documentation_path = path_builder(base_path, "documentation_autobuilder", "temp_docs")

files = glob.glob(python_source_code_path + os.sep + "*.py")

index_start = """Library Breakdown
=========

The full breakdown of what everything does!

.. toctree::
    :maxdepth: 2

"""

with open(path_builder(temporary_documentation_path, "index.rst"), "w") as open_file:
    open_file.write(index_start)

for file in files:
    #print(file)
    filename = os.path.basename(file).split(".")[0]
    doc_file = filename + ".rst"
    doc_component_file = path_builder(temporary_documentation_path, filename+".rst")
    open(doc_component_file, "w").close()
    with open(path_builder(temporary_documentation_path, "index.rst"), "a") as open_file:
        open_file.write("    " + doc_file + "\n")

    with open(file, "r") as open_file:
        content = open_file.readlines()

    in_class = False
    written_methods_data = False
    capture_docstring = False
    initial_capture_docstring = False
    docstring = ""
    class_name = ""
    function_name = ""
    for line in content:
        if (initial_capture_docstring and ('"""' in line or "'''" in line)) or (capture_docstring and not initial_capture_docstring):
            docstring += line.strip() + "\n    "
            if ('"""' in line or "'''" in line) and initial_capture_docstring is False:
                capture_docstring = False
                docstring = docstring.replace('"""', '').replace("'''", '')
                docstring = docstring[:-7]
                with open(doc_component_file, "a") as file:
                    file.write(docstring)
                docstring = ""
            initial_capture_docstring = False

        if "class " in line and ":" in line:
            class_name = line.split(" ")[1].split(":")[0]
            class_name = class_name.strip()
            formatted_class_name = ""

            for index in range(len(class_name)):
                if class_name[index] in alphabet and formatted_class_name != "":
                    formatted_class_name += " "

                formatted_class_name += class_name[index]

            formatted_class_name = formatted_class_name.replace("Open G L ", "OpenGL ")

            in_class = True
            written_methods_data = False
            #print("class: ", class_name)
            capture_docstring = True
            initial_capture_docstring = True

###################################################################
            class_data = f"""
{formatted_class_name} (``pmma.{class_name}``)
=======

Object
++++++
.. py:class:: {class_name}
"""
###################################################################

            with open(doc_component_file, "a") as open_file:
                open_file.write(class_data)

        if "def " in line:
            function_name = line.split("def ")[1].split(":")[0]
            if function_name[:2] == "__":
                continue
            indent_level = line.split("def")[0]
            indent_level_count = len(indent_level) // 4
            function = function_name.strip()
            function_name = function_name.split("(")[0]
            function_arguments = []
            if "(" in line and "):" in line:
                arg = ""
                open_brackets = 0
                useful_data = line.split("(", maxsplit=1)[-1]
                for character in useful_data:
                    if character == "(" or character == "[":
                        open_brackets += 1
                    if character == ")" or character == "]":
                        open_brackets -= 1
                    if (open_brackets == 0 and character == ","):
                        function_arguments.append(arg.strip())
                        arg = ""
                    else:
                        arg += character

                function_arguments.append(arg.strip())

                for index in range(len(function_arguments)):
                    function_arguments[index] = function_arguments[index].strip()

                function_arguments[-1] = function_arguments[-1][:-2]

            else:
                at_point = False
                caught = False
                for new_line in content:
                    if new_line == line:
                        at_point = True

                    if at_point:
                        if "(" in new_line and not caught:
                            caught = True
                            line_data = new_line.split("(")[-1].strip()
                            if line_data != "":
                                function_arguments.append(line_data[:-1])
                        elif ")" in new_line and not "," in new_line:
                            line_data = new_line.split(")")[0].strip() + ")"
                            if line_data != "":
                                function_arguments.append(line_data[:-1])
                            break
                        else:
                            function_arguments.append(new_line.strip()[:-1])

            if function_arguments != [] and function_arguments[0] == "self":
                function_arguments.pop(0)

            #print(function_arguments)

            ###
            refined_function_arguments = ""
            for arg in function_arguments:
                ### IN LINE BELOW ADD TYPES BY DOCSTRING INTERENCE - BUT WRITE DOCSTRING FIRST!!!
                refined_function_arguments += f"{arg}, "
            refined_function_arguments = refined_function_arguments[:-2]
            ###

            capture_docstring = True
            initial_capture_docstring = True
            if not written_methods_data:
###################################################################
                methods_header = """
Methods
++++++"""
###################################################################

                with open(doc_component_file, "a") as open_file:
                    open_file.write(methods_header)

                written_methods_data = True

            if in_class and indent_level_count == 1:
###################################################################
                methods_data = f"""
.. py:method:: {class_name}.{function_name}({refined_function_arguments}) -> NYD:
"""
###################################################################

                with open(doc_component_file, "a") as open_file:
                    open_file.write(methods_data)
                #print("method: ", function_name)
            else:
###################################################################
                methods_data = f"""
.. py:method:: {function_name}({refined_function_arguments}) -> NYD:
"""
###################################################################

                with open(doc_component_file, "a") as open_file:
                    open_file.write(methods_data)
