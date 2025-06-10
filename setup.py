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
    compile_args = ["/O2", "/fp:fast", "/GL", "/GF", "/GS-", "/std:c++17", "/wd4551"] # disable warning 4551 which is an issue for Cython
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
        "opengl32"
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

def make_ext(name, extra_cpp=None, add_numpy=False):
    sources = [os.path.join(cwd, "pmma", "core", "pyx_src", f"{name}.pyx")]
    if extra_cpp is not None:
        sources.extend(extra_cpp)

    lib_dirs = [pmma_lib_dir, glfw_lib]

    libs = [shared_name, *glfw_libraries]

    includes = [os.path.join(cwd, "pmma", "core", "hpp_src"), glfw_include]

    if add_numpy:
        includes += [numpy.get_include()]

    macros = []
    if add_numpy:
        macros.append(('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION'))

    return Extension(
        name=name,
        sources=sources,
        language="c++",
        include_dirs=includes,
        library_dirs=lib_dirs,
        libraries=libs,
        extra_compile_args=compile_args,
        extra_link_args=link_args,
        define_macros=macros,
    )

ext_modules = [
    make_ext("Display", add_numpy=True),
    make_ext("AdvancedMathematics", add_numpy=True),
    make_ext("PerlinNoise", add_numpy=True),
    make_ext("FractalBrownianMotion", add_numpy=True),
    make_ext("NumberConverter", add_numpy=True),
]

setup(
    name="PMMA",
    ext_modules=cythonize(ext_modules, compiler_directives={"language_level": "3"}, annotate=True),
)