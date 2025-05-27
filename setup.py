from setuptools import setup, Extension
from Cython.Build import cythonize
import sys, os

cwd = os.path.dirname(__file__)

def add_source(name):
    return [
        os.path.join(cwd, "pmma_dev", "core", "pyx_src", f"{name}.pyx"),
        os.path.join(cwd, "pmma_dev", "core", "cpp_src", f"{name}.cpp")
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

ext = Extension(
    name="mywrapper",
    sources=[*add_source("mywrapper")],
    language="c++",
    include_dirs=[os.path.join(cwd, "pmma_dev", "core", "hpp_src"), glfw_include],
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

setup(
    name="MyCythonCppProject",
    ext_modules=cythonize(
        [ext],
        compiler_directives={"language_level": "3"},
        annotate=True,  # Optional: creates .html annotation file to inspect performance
    ),
)
