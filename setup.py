from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
from Cython.Build import cythonize
import numpy
import os
import sys
import subprocess

cwd = os.path.dirname(__file__)
build_dir = os.path.join(cwd, "pmma", "build")
cpp_dir = os.path.join(cwd, "pmma", "core", "cpp_src")
hpp_dir = os.path.join(cwd, "pmma", "core", "hpp_src")

# Shared C++ source files to compile into static library
cpp_sources = [
    "Components.cpp",
    "Registry.cpp",
    "Display.cpp",
    "PerlinNoise.cpp"
]
cpp_sources = [os.path.join(cpp_dir, f) for f in cpp_sources]

glfw_include = ""
glfw_lib = ""
glfw_libraries = []
compile_args = []
link_args = []

if sys.platform.startswith("win"):
    compile_args = ["/O2", "/fp:fast", "/GL", "/GF", "/GS-", "/std:c++17"]
    link_args = ["/LTCG"]

    glfw_include = "H:/Downloads/CPMMA/extern/glfw-3.4.bin.WIN64/include"
    glfw_lib = "H:/Downloads/CPMMA/extern/glfw-3.4.bin.WIN64/lib-vc2022"
    glfw_libraries = [
        "glfw3", "user32", "gdi32", "shell32", "advapi32",
        "ole32", "oleaut32", "uuid", "comdlg32", "winmm",
    ]
elif sys.platform.startswith("linux"):
    compile_args = ["-O3", "-ffast-math", "-funroll-loops", "-fstrict-aliasing", "-fomit-frame-pointer", "-std=c++17"]
    glfw_include = "/usr/include"
    glfw_lib = "/usr/lib/x86_64-linux-gnu"
    glfw_libraries = ["glfw", "GL", "X11", "pthread", "Xrandr", "Xi", "dl", "m"]
elif sys.platform == "darwin":
    compile_args = ["-O3", "-ffast-math", "-funroll-loops", "-fstrict-aliasing", "-fomit-frame-pointer", "-std=c++17"]
    glfw_include = "/opt/homebrew/include"
    glfw_lib = ""
    glfw_libraries = ["glfw", "Cocoa", "OpenGL", "IOKit", "CoreVideo"]
else:
    raise NotImplementedError("Unsupported platform")

# Static library build command
class BuildStaticLib(build_ext):
    def run(self):
        os.makedirs(build_dir, exist_ok=True)
        objects = []

        for source in cpp_sources:
            obj_file = os.path.join(build_dir, os.path.splitext(os.path.basename(source))[0] + ".o")
            cmd = ["g++" if not sys.platform.startswith("win") else "cl"]
            cmd += compile_args
            if not sys.platform.startswith("win"):
                cmd += ["-c", source, "-o", obj_file, "-I", hpp_dir, "-I", glfw_include]
            else:
                obj_file = os.path.join(build_dir, os.path.splitext(os.path.basename(source))[0] + ".obj")
                cmd += [
                    "/c", source,
                    f"/Fo{obj_file}",
                    f"/I{hpp_dir}",
                    f"/I{glfw_include}"
                ]

            print("Compiling:", " ".join(cmd))
            subprocess.check_call(cmd)
            objects.append(obj_file)

        static_lib = os.path.join(build_dir, "libpmma.a")
        subprocess.check_call(["ar", "rcs", static_lib] + objects)
        print("Built static library:", static_lib)

        # Store for linking
        self.static_lib = static_lib
        build_ext.run(self)

def make_ext(name, pyx_name):
    return Extension(
        name=name,
        sources=[os.path.join(cwd, "pmma", "core", "pyx_src", pyx_name + ".pyx")],
        language="c++",
        include_dirs=[hpp_dir, glfw_include, numpy.get_include()],
        library_dirs=[glfw_lib],
        libraries=glfw_libraries,
        extra_objects=[os.path.join(build_dir, "libpmma.a")],
        extra_compile_args=compile_args,
        extra_link_args=link_args,
        define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')],
    )

ext_modules = [
    make_ext("Display", "Display"),
    make_ext("AdvancedMathematics", "AdvancedMathematics"),
    make_ext("PerlinNoise", "PerlinNoise"),
    make_ext("FractalBrownianMotion", "FractalBrownianMotion"),
    make_ext("NumberConverter", "NumberConverter"),
]

setup(
    name="PMMA",
    cmdclass={'build_ext': BuildStaticLib},
    ext_modules=cythonize(
        ext_modules,
        compiler_directives={"language_level": "3"},
        annotate=True
    ),
)
