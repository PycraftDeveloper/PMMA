from setuptools import setup, Extension
from Cython.Build import cythonize
import sys, os
import platform

import numpy

cwd = os.path.dirname(__file__)

def add_source(name: str):
    return [
        os.path.join(cwd, "pmma", "core", "pyx_src", f"{name}.pyx"),
        os.path.join(cwd, "pmma", "core", "cpp_src", f"{name}.cpp")
        ]

if sys.platform.startswith("win"):
    compile_args = ["/O2", "/fp:fast", "/GL", "/GF", "/GS-", "/std:c++17"]
    link_args = ["/LTCG"]

    glfw_include = "D:/Visual Studio C++ Extensions/glfw-3.4.bin.WIN64/include"
    glfw_lib = "D:/Visual Studio C++ Extensions/glfw-3.4.bin.WIN64/lib-vc2022"
    glfw_libraries = [
        "glfw3",
        "user32",
        "gdi32",
        "shell32",
        "advapi32",
        "ole32",
        "oleaut32",
        "uuid",
        "comdlg32",
        "winmm",
    ]

elif sys.platform.startswith("linux"):
    compile_args = [
        "-O3", "-ffast-math", "-funroll-loops", "-fstrict-aliasing", "-fomit-frame-pointer", "-std=c++17"
    ]
    link_args = []

    glfw_include = "/usr/include"
    glfw_lib = "/usr/lib/x86_64-linux-gnu"
    glfw_libraries = ["glfw", "GL", "X11", "pthread", "Xrandr", "Xi", "dl", "m"]

elif sys.platform == "darwin":
    compile_args = [
        "-O3", "-ffast-math", "-funroll-loops", "-fstrict-aliasing", "-fomit-frame-pointer", "-std=c++17"
    ]
    link_args = []

    glfw_include = "/opt/homebrew/include"  # or /usr/local/include depending on installation
    glfw_lib = ""
    glfw_libraries = ["glfw", "Cocoa", "OpenGL", "IOKit", "CoreVideo"]
else:
    raise NotImplementedError("Unsupported platform")

shared_name = 'PMMA_Core'
pmma_lib_dir = os.path.join(cwd, "pmma", "lib")

Display_ext = Extension(
    name="Display",
    sources=[*add_source("Display"), add_source("Registry")[-1]],
    language="c++",
    include_dirs=[os.path.join(cwd, "pmma", "core", "hpp_src"), glfw_include, numpy.get_include()],
    library_dirs=[pmma_lib_dir, glfw_lib],
    libraries=[shared_name, *glfw_libraries],
    extra_compile_args=compile_args,
    extra_link_args=link_args,
    define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')],
)

AdvancedMathematics_ext = Extension(
    name="AdvancedMathematics",
    sources=[*add_source("AdvancedMathematics")],
    language="c++",
    include_dirs=[os.path.join(cwd, "pmma", "core", "hpp_src"), numpy.get_include()],
    extra_compile_args=compile_args,
    extra_link_args=link_args,
    define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')],
)

PerlinNoise_ext = Extension(
    name="PerlinNoise",
    sources=[*add_source("PerlinNoise")],
    language="c++",
    include_dirs=[os.path.join(cwd, "pmma", "core", "hpp_src"), numpy.get_include()],
    extra_compile_args=compile_args,
    extra_link_args=link_args,
    define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')],
)

FractalBrownianMotion_ext = Extension(
    name="FractalBrownianMotion",
    sources=[*add_source("FractalBrownianMotion"), add_source("PerlinNoise")[-1]],  # Reuse PerlinNoise's cpp file
    language="c++",
    include_dirs=[os.path.join(cwd, "pmma", "core", "hpp_src"), numpy.get_include()],
    extra_compile_args=compile_args,
    extra_link_args=link_args,
    define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')],
)

NumberConverter_ext = Extension(
    name="NumberConverter",
    sources=[add_source("NumberConverter")[0], add_source("Display")[-1], add_source("Registry")[-1]], # This is header only
    language="c++",
    library_dirs=[pmma_lib_dir, glfw_lib],
    libraries=[shared_name, *glfw_libraries],
    include_dirs=[os.path.join(cwd, "pmma", "core", "hpp_src"), glfw_include, numpy.get_include()],
    extra_compile_args=compile_args,
    extra_link_args=link_args,
    define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')],
)

setup(
    name="PMMA",
    ext_modules=cythonize(
        [Display_ext, AdvancedMathematics_ext, PerlinNoise_ext, FractalBrownianMotion_ext, NumberConverter_ext],
        compiler_directives={"language_level": "3"},
        annotate=True,  # Optional: creates .html annotation file to inspect performance
    ),
)
