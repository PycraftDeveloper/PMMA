import os
import glob

input("Please note you are using a program that has now been automated \
using GitHib actions. You are still able to use this program, however \
it will put unnecessary strain on services like ReadTheDocs. This program \
runs nightly and its generally best to leave it as such. Proceed only \
if you absolutely have to.")

def _up(path: str) -> str:
    return path[::-1].split(os.sep, 1)[-1][::-1]

def path_builder(*args):
    result = ""
    for arg in args:
        result += arg
        result += os.sep
    result = result[:-1]
    return result

def capture_docstring(name, content, line_no, is_class=False):
    if is_class:
        look_for = f"class {name}"
    else:
        look_for = f"def {name}"

    docstring = ""
    found_definition = False
    found_docstring = False
    indent_level = 1
    found_args = False
    found_returns = False
    args = []
    returns = []

    content = content[line_no:]

    doc_parse_line_no = 0

    for line in content:
        if found_definition:
            if ('"""' in line or "'''" in line):
                found_docstring = True

        if found_docstring:
            if "arguments:" in line:
                line = line.replace("arguments:", "Arguments:")
                indent_level = 1
                found_args = False
                found_returns = False
            if "Arguments:" in line:
                indent_level = 1
                found_args = False
                found_returns = False
            if "ARGUMENTS:" in line:
                line = line.replace("ARGUMENTS:", "Arguments:")
                indent_level = 1
                found_args = False
                found_returns = False
            if "args:" in line:
                line = line.replace("args:", "Arguments:")
                indent_level = 1
                found_args = False
                found_returns = False
            if "Args:" in line:
                line = line.replace("Args:", "Arguments:")
                indent_level = 1
                found_args = False
                found_returns = False
            if "ARGS:" in line:
                line = line.replace("ARGS:", "Arguments:")
                indent_level = 1
                found_args = False
                found_returns = False
            if "parameters:" in line:
                line = line.replace("parameters:", "Arguments:")
                indent_level = 1
                found_args = False
                found_returns = False
            if "Parameters:" in line:
                line = line.replace("Parameters:", "Arguments:")
                indent_level = 1
                found_args = False
                found_returns = False
            if "PARAMETERS:" in line:
                line = line.replace("PARAMETERS:", "Arguments:")
                indent_level = 1
                found_args = False
                found_returns = False
            if "params:" in line:
                line = line.replace("params:", "Arguments:")
                indent_level = 1
                found_args = False
                found_returns = False
            if "Params:" in line:
                line = line.replace("Params:", "Arguments:")
                indent_level = 1
                found_args = False
                found_returns = False
            if "PARAMS:" in line:
                line = line.replace("PARAMS:", "Arguments:")
                indent_level = 1
                found_args = False
                found_returns = False

            if "returns:" in line:
                line = line.replace("returns:", "Returns:")
                indent_level = 1
                found_args = False
                found_returns = False
            if "Returns:" in line:
                indent_level = 1
                found_args = False
                found_returns = False
            if "RETURNS:" in line:
                line = line.replace("RETURNS:", "Returns:")
                indent_level = 1
                found_args = False
                found_returns = False
            if "returns:" in line:
                line = line.replace("returns:", "Returns:")
                indent_level = 1
                found_args = False
                found_returns = False
            if "Params:" in line:
                line = line.replace("Params:", "Returns:")
                indent_level = 1
                found_args = False
                found_returns = False
            if "PARAMS:" in line:
                line = line.replace("PARAMS:", "Returns:")
                indent_level = 1
                found_args = False
                found_returns = False

            if ('"""' in line or "'''" in line) and docstring != "":
                if is_class:
                    _indent_level = indent_level-1
                else:
                    _indent_level = indent_level
                docstring += "    "*_indent_level + line.strip() + "\n"
                break

            if is_class:
                _indent_level = indent_level-1
            else:
                _indent_level = indent_level
            docstring += "    "*_indent_level + line.strip() + "\n"
            if (found_args or found_returns) and line.strip() != "":
                #   points (list) -
                try:
                    arg = line.strip()
                    arg_start = arg.split("(")[0].strip()
                    arg_end = arg.split("(")[1].strip()
                    arg_end = arg_end.split(")")[0].strip()

                    if found_args:
                        args.append(f"{arg_start}: {arg_end}")
                    if found_returns:
                        returns.append(f"{arg_end}")
                except Exception as error:
                    print(error)
                    print(line)

            if "arguments:" in line:
                line = line.replace("arguments:", "Arguments:")
                indent_level = 2
                found_args = True
                found_returns = False
            elif "Arguments:" in line:
                indent_level = 2
                found_args = True
                found_returns = False
            elif "ARGUMENTS:" in line:
                line = line.replace("ARGUMENTS:", "Arguments:")
                indent_level = 2
                found_args = True
                found_returns = False
            elif "args:" in line:
                line = line.replace("args:", "Arguments:")
                indent_level = 2
                found_args = True
                found_returns = False
            elif "Args:" in line:
                line = line.replace("Args:", "Arguments:")
                indent_level = 2
                found_args = True
                found_returns = False
            elif "ARGS:" in line:
                line = line.replace("ARGS:", "Arguments:")
                indent_level = 2
                found_args = True
                found_returns = False
            elif "parameters:" in line:
                line = line.replace("parameters:", "Arguments:")
                indent_level = 2
                found_args = True
                found_returns = False
            elif "Parameters:" in line:
                line = line.replace("Parameters:", "Arguments:")
                indent_level = 2
                found_args = True
                found_returns = False
            elif "PARAMETERS:" in line:
                line = line.replace("PARAMETERS:", "Arguments:")
                indent_level = 2
                found_args = True
                found_returns = False
            elif "params:" in line:
                line = line.replace("params:", "Arguments:")
                indent_level = 2
                found_args = True
                found_returns = False
            elif "Params:" in line:
                line = line.replace("Params:", "Arguments:")
                indent_level = 2
                found_args = True
                found_returns = False
            elif "PARAMS:" in line:
                line = line.replace("PARAMS:", "Arguments:")
                indent_level = 2
                found_args = True
                found_returns = False
            else:
                found_args = False

            if "returns:" in line:
                line = line.replace("returns:", "Returns:")
                indent_level = 2
                found_args = False
                found_returns = True
            elif "Returns:" in line:
                indent_level = 2
                found_args = False
                found_returns = True
            elif "RETURNS:" in line:
                line = line.replace("RETURNS:", "Returns:")
                indent_level = 2
                found_args = False
                found_returns = True
            elif "returns:" in line:
                line = line.replace("returns:", "Returns:")
                indent_level = 2
                found_args = False
                found_returns = True
            elif "Params:" in line:
                line = line.replace("Params:", "Returns:")
                indent_level = 2
                found_args = False
                found_returns = True
            elif "PARAMS:" in line:
                line = line.replace("PARAMS:", "Returns:")
                indent_level = 2
                found_args = False
                found_returns = True
            else:
                found_returns = False

        if look_for in line:
            found_definition = True
            n = doc_parse_line_no
            for test_line in content:
                n += 1
                if ":" in test_line:
                    break

            if not ('"""' in content[n] or "'''" in content[n]):
                break

        doc_parse_line_no += 1

    docstring = docstring.replace('"""', '').replace("'''", '')
    if docstring == "":
        if is_class is False:
            docstring = "   Not Yet Written\n"
        else:
            docstring = "Not Yet Written\n"
    else:
        if is_class is False:
            docstring = " " + docstring[6:]
    return docstring, args, returns

### setup
base_path = _up(_up(__file__))

python_source_code_path = path_builder(base_path, "python_src")
documentation_path = path_builder(base_path, "docs", "library_breakdown")
temporary_documentation_path = path_builder(base_path, "documentation_autobuilder", "temp_docs")

files = glob.glob(python_source_code_path + os.sep + "*.py")

SEPARATOR = os.sep
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
### end

### write index.rst
index_start = """Library Breakdown
=========

The full breakdown of what everything does!

.. toctree::
    :maxdepth: 1

"""
for file in files:
    file_name = os.path.basename(file).split(".")[0]
    if file_name != "events":
        index_start += f"    {file_name}.rst\n"
index_start += f"    miscellaneous.rst\n"
index_start += f"    events.rst\n" # do last due to large number of classes - may help with documentation contents.

index_file_path = path_builder(documentation_path, "index.rst")
with open(index_file_path, "w") as index_file:
    index_file.write(index_start)

### end

### write documentation
for file in files:
    with open(file, "r") as original_file:
        content = original_file.readlines()

    file_name = os.path.basename(file).split(".")[0]
    in_class = False
    documentation = ""
    methods_header_written = False

    line_no = 0

    for line in content:
        indent_whitespace = len(line[:-len(line.lstrip())]) // 4
        if "def " in line and not "__" in line:
            if not ("def _" in line or "def wrapper(" in line): # hide hidden methods
                if in_class != in_class and indent_whitespace == 1:
                    methods_header_written = False

                in_class = in_class and indent_whitespace == 1
                if in_class is False:
                    class_name = "pmma"
                name = line.split("def ")[-1].split("(")[0].strip()

                docstring, args, returns = capture_docstring(name, content, line_no, is_class=False)
                formatted_args = ", ".join(args)
                formatted_returns = ", ".join(returns)
                if formatted_returns == "":
                    formatted_returns = "None"

                if methods_header_written is False:
                    methods_header_written = True
                    ln = "Methods\n"
                    if class_name == "pmma":
                        section_marker = "="
                    else:
                        section_marker = "-"
                    documentation += "Methods\n"
                    documentation += section_marker*(len(ln)-1) + "\n\n"
                documentation += f".. py:method:: {class_name}.{name}({formatted_args}) -> {formatted_returns}\n\n"
                documentation += docstring + "\n"

        elif "class " in line and ":" in line:
            if not "class _" in line: # hide hidden classes
                name = line.split("class ")[-1].split("(")[0]
                name = name.split(":")[0].strip()
                formatted_name = ""
                for character in name:
                    if character in ALPHABET or character in NUMBERS:
                        formatted_name += " "
                    formatted_name += character

                formatted_name = formatted_name.replace("Open G L", "OpenGL").strip()
                formatted_name = formatted_name.replace("G P U", "GPU").strip()
                formatted_name = formatted_name.replace("_ GPU", "_GPU").strip()
                formatted_name = formatted_name.replace("_ E V E N T", " Event").strip()
                formatted_name = formatted_name.replace("_ K E Y", " Key").strip()
                formatted_name = formatted_name.replace("_ M O U S E", " Mouse").strip()
                formatted_name = formatted_name.replace("_ S C R O L L", " Scroll").strip()
                formatted_name = formatted_name.replace("_ P O S I T I O N", " Position").strip()
                formatted_name = formatted_name.replace(" I C C P R O F ", " ICC Profile ").strip()
                formatted_name = formatted_name.replace("Sys W M", "System Window Management").strip()
                formatted_name = formatted_name.replace("Event Event", "Event").strip()

                formatted_name = formatted_name.replace("1 0", "10").strip()
                formatted_name = formatted_name.replace("1 1", "11").strip()
                formatted_name = formatted_name.replace("1 2", "12").strip()
                formatted_name = formatted_name.replace("1 3", "13").strip()
                formatted_name = formatted_name.replace("1 4", "14").strip()
                formatted_name = formatted_name.replace("1 5", "15").strip()
                formatted_name = formatted_name.replace("1 6", "16").strip()
                formatted_name = formatted_name.replace("1 7", "17").strip()
                formatted_name = formatted_name.replace("1 8", "18").strip()
                formatted_name = formatted_name.replace("1 9", "19").strip()
                formatted_name = formatted_name.replace("2 0", "20").strip()

                in_class = True
                methods_header_written = False
                docstring, args, returns = capture_docstring(name, content, line_no, is_class=True)
                init_docstring, init_args, init_returns = capture_docstring("__init__", content, line_no)
                formatted_init_args = ", ".join(init_args)
                class_name = name
                ln = f"{formatted_name} (``pmma.{name}``)\n"
                documentation += f"{formatted_name} (``pmma.{name}``)\n"
                documentation += "="*(len(ln)-1) + "\n\n"
                documentation += docstring.strip() + "\n\n"

                ln = "Create\n"
                documentation += "Create\n"
                documentation += "-"*(len(ln)-1) + "\n\n"
                documentation += f".. py:method:: pmma.{name}({formatted_init_args}) -> pmma.{name}\n\n"
                documentation += init_docstring + "\n"

        line_no += 1

    with open(path_builder(documentation_path, f"{file_name}.rst"), "w") as documentation_file:
        documentation_file.write(documentation)

general_documentation = """
PMMA Miscellaneous Methods (``pmma.``)
====================

Here you will find all the subroutines that aren't grouped into a specific object. Don't let the title fool you however, the subroutines found here can be incredibly powerful and helpful.

"""
files = glob.glob(documentation_path + os.sep + "*.rst")
for file in files:
    with open(file, "r") as doc_file:
        content = doc_file.readlines()
    if len(content) == 0:
        continue
    if content[0].strip() == "Methods" and content[1].strip() == "=======":
        #print(content[3])
        line_no = 3
        while line_no < len(content):
            line = content[line_no]
            if " (``" in line:
                break
            general_documentation += line

            line_no += 1

        content = content[line_no:]
        file_content = "".join(content)
        with open(file, "w") as doc_file:
            doc_file.write(file_content)

with open(path_builder(documentation_path, "miscellaneous.rst"), "w") as documentation_file:
    documentation_file.write(general_documentation)