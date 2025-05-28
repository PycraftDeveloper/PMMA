from setuptools import setup, Extension
from Cython.Build import cythonize
import sys, os

import numpy

cwd = os.path.dirname(__file__)

def add_source(name):
    return [
        os.path.join(cwd, "pmma", "core", "pyx_src", f"{name}.pyx"),
        os.path.join(cwd, "pmma", "core", "cpp_src", f"{name}.cpp")
        ]

# Recommended C++ optimization flags
extra_compile_args = ["-O3", "-march=native", "-ffast-math", "-std=c++17"]
extra_link_args = []

glfw_include = "H:/Downloads/CPMMA/extern/glfw-3.4.bin.WIN64/include"
glfw_lib = "H:/Downloads/CPMMA/extern/glfw-3.4.bin.WIN64/lib-vc2022"

# Adjust for Windows (optional)
if sys.platform == "win32":
    extra_compile_args = ["/O2"]  # MSVC optimization
    extra_link_args = []

mywrapper_ext = Extension( # EXAMPLE
    name="mywrapper",
    sources=[*add_source("mywrapper")],
    language="c++",
    include_dirs=[os.path.join(cwd, "pmma", "core", "hpp_src"), glfw_include, numpy.get_include()],
    library_dirs=[glfw_lib],
    libraries=["glfw3",
            "user32",
            "gdi32",
            "shell32",
            "advapi32",
            "ole32",
            "oleaut32",
            "uuid",
            "comdlg32",
            "winmm",],
    extra_compile_args=extra_compile_args,
    extra_link_args=extra_link_args,
)

AdvancedMathematics_ext = Extension(
    name="AdvancedMathematics",
    sources=[*add_source("AdvancedMathematics")],
    language="c++",
    include_dirs=[os.path.join(cwd, "pmma", "core", "hpp_src"), numpy.get_include()],
    extra_compile_args=extra_compile_args,
    extra_link_args=extra_link_args,
)

setup(
    name="PMMA",
    ext_modules=cythonize(
        [mywrapper_ext, AdvancedMathematics_ext],
        compiler_directives={"language_level": "3"},
        annotate=True,  # Optional: creates .html annotation file to inspect performance
    ),
)
