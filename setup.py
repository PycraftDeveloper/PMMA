#type: ignore

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
    compile_args = ["/O2", "/fp:fast", "/GL", "/GF", "/GS-", "/std:c++17", "/wd4551", "/wd4251"] # disable warning 4551 & 4251 which is an issue for Cython
    link_args = ["/LTCG"]

    build_tools_dir = os.path.join(cwd, "build_tools")
    vcpkg_dir = os.path.join(build_tools_dir, "vcpkg")

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

    glfw_libraries = ["glfw3", "GL", "X11", "pthread", "Xrandr", "Xi", "dl", "m"]

elif sys.platform == "darwin":
    compile_args = [
        "-O3", "-ffast-math", "-funroll-loops", "-fstrict-aliasing", "-fomit-frame-pointer", "-std=c++17"
    ]
    link_args = [
        "-framework", "Cocoa",
        "-framework", "OpenGL",
        "-framework", "IOKit",
        "-framework", "CoreVideo",
    ]

    arch = platform.machine()
    if arch == "arm64":
        compile_args.append("-arch")
        compile_args.append("arm64")
        link_args.append("-arch")
        link_args.append("arm64")

    glfw_libraries = ["glfw3"]
else:
    raise NotImplementedError("Unsupported platform")

shared_name = 'PMMA_Core'

def make_ext(name, extra_cpp=None, add_numpy=False):
    sources = [os.path.join("pmma", "core", "pyx_src", f"{name}.pyx")]
    if extra_cpp is not None:
        sources.extend(extra_cpp)

    lib_dirs = [os.path.join(cwd, "pmma", "lib"), os.path.join(cwd, "pmma", "extern", "lib")]

    libs = [shared_name, *glfw_libraries]

    includes = [os.path.join(cwd, "pmma", "core", "hpp_src"), os.path.join(cwd, "pmma", "extern", "include")]

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
    make_ext("AdvancedMathematics", add_numpy=True),
    make_ext("Display", add_numpy=True),
    make_ext("Events", add_numpy=True),
    make_ext("FractalBrownianMotion", add_numpy=True),
    make_ext("KeyEvents"),
    make_ext("NumberConverter", add_numpy=True),
    make_ext("PerlinNoise", add_numpy=True),
]

# Read the long description from README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read the requirements from requirements.txt
with open("requirements.txt", "r", encoding="utf-8") as req_file:
    requirements = req_file.read().splitlines()

package_data={"pmma": ["**/*"]}

packages = []
def list_dirs(root_dir):
    for dirpath, dirnames, _ in os.walk(root_dir):
        if not (dirpath in ["temporary", "pyx_src", "cpp_src", "hpp_src"]):
            package = "pmma." + dirpath.replace(root_dir, "").replace(os.sep, ".")[1:]
            if package == "pmma.":
                package = "pmma"
            packages.append(package)
list_dirs(os.path.join(cwd, "pmma"))

setup(
    name="pmma",
    version="5.0.7",
    author="PycraftDev",
    author_email="thomasjebbo@gmail.com",
    description="Python Multi-Media API (PMMA) is a multi-purpose API designed to make working on multi-media projects easier and faster!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PycraftDeveloper/PMMA",
    project_urls={
        "Bug Tracker": "https://github.com/PycraftDeveloper/PMMA/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=packages,  # Include the pmma package and all its sub-packages
    python_requires=">=3.8",
    install_requires=requirements,
    include_package_data=True,
    package_data=package_data,
    ext_modules=cythonize(ext_modules, compiler_directives={"language_level": "3"}, annotate=True),
)