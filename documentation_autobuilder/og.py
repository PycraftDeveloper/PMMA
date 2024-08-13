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

def capture_docstring(name, content, is_class=False):
    if is_class:
        look_for = f"class {name}"
    else:
        look_for = f"def {name}"

    docstring = ""
    is_docstring = False
    read_docstring = False
    for line in content:
        if is_docstring and read_docstring is False:
            if ('"""' in line or "'''" in line):
                read_docstring = True

        if is_docstring and read_docstring:
            docstring += line
            if ('"""' in line or "'''" in line):
                break

        if look_for in line:
            read_docstring = True

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
    line_count = 0
    indent = 0
    for line in content:
        if (initial_capture_docstring and ('"""' in line or "'''" in line)) or (capture_docstring and not initial_capture_docstring):
            #if ("Returns:" in line or "Parameters:" in line) and initial_capture_docstring is False:
                #capture_docstring = False
                #docstring = docstring.replace('"""', '').replace("'''", '')
                #docstring = docstring[:-7]
                #with open(doc_component_file, "a") as open_file:
                    #open_file.write(docstring)
                #docstring = ""

            #docstring += line.strip() + "\n    "
            if ("Returns:" in line or "Parameters:" in line):
                indent = 0
            docstring += "    "*indent + line.strip() + "\n    "
            if ("Returns:" in line or "Parameters:" in line):
                indent = 1

            if ('"""' in line or "'''" in line) and initial_capture_docstring is False:
                capture_docstring = False
                docstring = docstring.replace('"""', '').replace("'''", '')
                docstring = docstring[:-7]
                with open(doc_component_file, "a") as open_file:
                    open_file.write(docstring)
                docstring = ""
                indent = 0
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

            found_class = False
            input_list_attrs = []
            output__list_attrs = []
            constructor_docstring = ""
            found_init = False
            constructor_capture_docstring = False
            for new_line in content:
                if f"class {class_name}" in new_line:
                    found_class = True

                if found_class and "def __init__" in new_line:
                    print("Found init")
                    found_init = True
                    if "(" in new_line and ")" in new_line:
                        init_data = new_line.split("(")[-1].split(")")[0].strip()
                        if init_data != "":
                            for arg in init_data.split(","):
                                input_list_attrs.append(arg.strip())

                if found_init:
                    if constructor_docstring == "":
                        if ('"""' in new_line or "'''" in new_line):
                            constructor_capture_docstring = True
                            constructor_docstring += "    " + new_line.strip() + "\n    "
                    elif constructor_capture_docstring:
                        if ('"""' in new_line or "'''" in new_line):
                            constructor_docstring = constructor_docstring.replace('"""', '').replace("'''", '')
                            constructor_docstring = constructor_docstring[:-7]
                            with open(doc_component_file, "a") as open_file:
                                open_file.write(constructor_docstring)
                            constructor_docstring = ""
                            constructor_capture_docstring = False
                        else:
                            constructor_docstring += "    " + new_line.strip() + "\n    "

            if input_list_attrs != []:
                del input_list_attrs[0]

            input_attrs = ", ".join(input_list_attrs)
            output_attrs = ", ".join(output__list_attrs)

            create_data = f"""
Create
++++++
..py:method:: pmma.{class_name}({input_attrs}) -> {output_attrs}

{constructor_docstring}
"""
            with open(doc_component_file, "a") as open_file:
                open_file.write(create_data)

        if "def " in line:
            indent_level = len(line.split("def")[0]) // 4
            if indent_level == 0 and in_class:
                written_methods_data = False
                in_class = False
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
                new_line_count = 0
                for new_line in content:
                    if new_line_count == line_count:
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
                        new_line_count += 1

            if function_arguments != [] and function_arguments[0] == "self":
                function_arguments.pop(0)

            #print(function_arguments)

            ### docstring inference
            inputs = []
            outputs = []

            at_point = False
            caught_inputs = False
            caught_outputs = False

            capture_docstring = False
            initial_capture_docstring = False
            searchable_docstring = ""
            #################
            new_line_count = 0
            for new_line in content:
                if new_line_count == line_count:
                    capture_docstring = True
                    initial_capture_docstring = True

                if (initial_capture_docstring and ('"""' in new_line or "'''" in new_line)) or (capture_docstring and not initial_capture_docstring):
                    searchable_docstring += new_line.strip() + "\n    "
                    if ('"""' in new_line or "'''" in new_line) and initial_capture_docstring is False:
                        capture_docstring = False
                        searchable_docstring = searchable_docstring.replace('"""', '').replace("'''", '')
                        searchable_docstring = searchable_docstring[:-7]
                        break

                    initial_capture_docstring = False
                new_line_count += 1
            #################
            for new_line in searchable_docstring.split("\n"):
                if caught_inputs:
                    print(new_line)
                    input_data = new_line.split("(")[-1].strip()
                    input_data = input_data.split(")")[0].strip()
                    inputs.append(input_data)

                if caught_outputs:
                    if "-" in new_line:
                        output_data = new_line.split("-")[0].strip()
                    elif ": " in new_line:
                        output_data = new_line.split(": ")[0].strip()
                    else:
                        output_data = new_line.strip()
                    outputs.append(output_data)

                if "Parameters:" in new_line:
                    caught_outputs = False
                    caught_inputs = True
                if "Returns:" in new_line:
                    caught_outputs = True
                    caught_inputs = False

            ### end
            try:
                inputs += [""]*(len(function_arguments)-len(inputs))
                refined_function_arguments = ""
                for i in range(len(function_arguments)):
                    if inputs[i] == "":
                        refined_function_arguments += f"{function_arguments[i]}, "
                    else:
                        refined_function_arguments += f"{function_arguments[i]}: {inputs[i]}, "
            except IndexError as error:
                print("Problem in inputs...")
                print(refined_function_arguments)
                print(function_arguments)
                print(inputs)
                print(file)
                print(function_name)
                print(class_name)

            refined_function_arguments = refined_function_arguments[:-2]
            ###

            ### end
            try:
                refined_function_outputs = ""
                for i in range(len(outputs)):
                    refined_function_outputs += f"{outputs[i]}, "
            except IndexError as error:
                print("Problem in inputs...")
                print(refined_function_arguments)
                print(function_arguments)
                print(inputs)
                print(file)
                print(function_name)
                print(class_name)

            refined_function_outputs = refined_function_outputs[:-4]
            if refined_function_outputs != "":
                refined_function_outputs = f" -> {refined_function_outputs}:"
            else:
                refined_function_outputs = ":"
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
.. py:method:: {class_name}.{function_name}({refined_function_arguments}){refined_function_outputs}
"""
###################################################################

                with open(doc_component_file, "a") as open_file:
                    open_file.write(methods_data)
                #print("method: ", function_name)
            else:
###################################################################
                methods_data = f"""
.. py:method:: {function_name}({refined_function_arguments}){refined_function_outputs}
"""
###################################################################

                with open(doc_component_file, "a") as open_file:
                    open_file.write(methods_data)

        line_count += 1