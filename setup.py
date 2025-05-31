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

glfw_include = "H:/Downloads/CPMMA/extern/glfw-3.4.bin.WIN64/include"
glfw_lib = "H:/Downloads/CPMMA/extern/glfw-3.4.bin.WIN64/lib-vc2022"

if sys.platform == "win32":
    compile_args = ["/O2", "/fp:fast", "/GL", "/GF", "/GS-"]
    link_args = ["/LTCG"]
else:
    compile_args = [
        "-O3", "-ffast-math", "-funroll-loops", "-fstrict-aliasing",
        "-fno-exceptions", "-fomit-frame-pointer", "-std=c++17"
    ]
    link_args = []

mywrapper_ext = Extension( # EXAMPLE
    name="Display",
    sources=[*add_source("Display")],
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
    extra_compile_args=compile_args,
    extra_link_args=link_args,
)

AdvancedMathematics_ext = Extension(
    name="AdvancedMathematics",
    sources=[*add_source("AdvancedMathematics")],
    language="c++",
    include_dirs=[os.path.join(cwd, "pmma", "core", "hpp_src"), numpy.get_include()],
    extra_compile_args=compile_args,
    extra_link_args=link_args,
)

PerlinNoise_ext = Extension( # this one
    name="PerlinNoise",
    sources=[*add_source("PerlinNoise")],
    language="c++",
    include_dirs=[os.path.join(cwd, "pmma", "core", "hpp_src"), numpy.get_include()],
    extra_compile_args=compile_args,
    extra_link_args=link_args,
)

FractalBrownianMotion_ext = Extension( # this one
    name="FractalBrownianMotion",
    sources=[*add_source("FractalBrownianMotion"), add_source("PerlinNoise")[-1]],  # Reuse PerlinNoise's cpp file
    language="c++",
    include_dirs=[os.path.join(cwd, "pmma", "core", "hpp_src"), numpy.get_include()],
    extra_compile_args=compile_args,
    extra_link_args=link_args,
)

setup(
    name="PMMA",
    ext_modules=cythonize(
        [mywrapper_ext, AdvancedMathematics_ext, PerlinNoise_ext, FractalBrownianMotion_ext],
        compiler_directives={"language_level": "3"},
        annotate=True,  # Optional: creates .html annotation file to inspect performance
    ),
)
