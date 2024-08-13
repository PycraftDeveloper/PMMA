import ast
import re
from typing import Union

class DocstringExtractor(ast.NodeVisitor):
    def __init__(self):
        self.docs = []

    def visit_FunctionDef(self, node: ast.FunctionDef):
        """Visit a function or method definition."""
        docstring = ast.get_docstring(node)
        if docstring:
            func_name = node.name
            args = self._get_args(node.args, docstring)
            ret_type = self._get_return_type(node, docstring)
            self.docs.append(self.format_function_or_method(func_name, args, ret_type, docstring))
        self.generic_visit(node)

    def visit_ClassDef(self, node: ast.ClassDef):
        """Visit a class definition."""
        class_name = node.name
        class_docstring = ast.get_docstring(node)
        if class_docstring:
            self.docs.append(self.format_class(class_name, class_docstring))

        # Visit the __init__ method separately
        for body_item in node.body:
            if isinstance(body_item, ast.FunctionDef) and body_item.name == '__init__':
                init_docstring = ast.get_docstring(body_item)
                if init_docstring:
                    args = self._get_args(body_item.args, init_docstring)
                    self.docs.append(self.format_function_or_method(f"{class_name}.{body_item.name}", args, "None", init_docstring))

            elif isinstance(body_item, ast.FunctionDef):
                # For other methods in the class
                self.visit_FunctionDef(body_item)

        self.generic_visit(node)

    def format_function_or_method(self, name: str, args: str, ret_type: str, docstring: str) -> str:
        """Format a function or method into the desired output."""
        return f".. py:method:: pmma.{name}({args}) -> {ret_type}:\n\n\t{docstring}\n"

    def format_class(self, name: str, docstring: str) -> str:
        """Format a class into the desired output."""
        return f"\nCLASSNAME (``pmma.{name}``)\n=======\n\nObject\n++++++\n\n.. py:class:: {name}\n\n\t{docstring}\n"

    def _get_args(self, args: ast.arguments, docstring: str) -> str:
        """Extract the arguments from a function or method and infer types from the docstring."""
        docstring_types = self._parse_docstring(docstring)
        arg_list = []
        for arg in args.args:
            arg_type = docstring_types.get(arg.arg, "TYPE")
            arg_list.append(f"{arg.arg}: {arg_type}")
        return ", ".join(arg_list)

    def _get_return_type(self, node: ast.FunctionDef, docstring: str) -> str:
        """Get the return type annotation of a function or method, inferred from the docstring if available."""
        docstring_types = self._parse_docstring(docstring)
        return docstring_types.get('return', 'TYPE')

    def _parse_docstring(self, docstring: str) -> dict:
        """Parse the docstring to extract parameter types and return types."""
        types = {}

        # Extract parameter types
        param_matches = re.findall(r'PARAMETERS:\s*(.*?)\s*RETURNS:', docstring, re.DOTALL)
        if param_matches:
            param_section = param_matches[0].strip()
            for line in param_section.splitlines():
                match = re.match(r'\s*(\w+)\s*:\s*([\w\s\[\],]*)', line)
                if match:
                    param_name, param_type = match.groups()
                    types[param_name] = param_type.strip()

        # Extract return type
        return_match = re.search(r'RETURNS:\s*(\w+)', docstring)
        if return_match:
            types['return'] = return_match.group(1)

        return types

def extract_documentation(source_code: str) -> str:
    tree = ast.parse(source_code)
    extractor = DocstringExtractor()
    extractor.visit(tree)
    return "\n".join(extractor.docs)

# Example usage
source_code = """
class CLASSNAME:
    \"""
    DEFINITION_1

    PARAMETERS:
        g: STR

    RETURNS:
        NONE
    \"""
    def __init__(self, g):
        \"""
        DEFINITION_2
        \"""

        self.g = g

    def METHODNAME(self, x):
        \"""
        DEFINITION_3

        PARAMETERS:
            x: INT or FLOAT

        RETURNS:
            INT
        \"""
        return x * 2

def FUNCTIONNAME(x):
    \"""
    DEFINITION_4

    PARAMETERS:
        x: INT

    RETURNS:
        FLOAT
    \"""
    return x / 2
"""

documentation = extract_documentation(source_code)
print(documentation)
