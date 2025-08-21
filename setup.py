#type: ignore

from setuptools import setup, Extension
from Cython.Build import cythonize
import sys, os
import platform
import multiprocessing

import numpy

cwd = os.path.dirname(__file__)

sys.path.insert(0, os.path.join(cwd, "pmma", "build"))

def add_source(name: str):
    return [
        os.path.join("pmma", "core", "pyx_src", f"{name}.pyx"),
        os.path.join("pmma", "core", "cpp_src", f"{name}.cpp")
        ]

if sys.platform.startswith("win"):
    compile_args = ["/O2", "/fp:fast", "/GL", "/GF", "/GS-", "/std:c++17", "/wd4551", "/wd4251"] # disable warning 4551 & 4251 which is an issue for Cython
    link_args = ["/LTCG"]

elif sys.platform.startswith("linux"):
    compile_args = [
        "-O3", "-ffast-math", "-funroll-loops", "-fstrict-aliasing", "-fomit-frame-pointer", "-std=c++17"
    ]
    link_args = []

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
else:
    raise NotImplementedError("Unsupported platform")

shared_name = 'PMMA_Core'

def make_ext(component, extra_cpp=None, add_numpy=False, raw_depends=[]):
    sources = [os.path.join("pmma", "core", "pyx_src", component)]
    if extra_cpp is not None:
        sources.extend(extra_cpp)

    depends = []
    for item in raw_depends:
        depends.append(os.path.join("pmma", "core", "pyx_src", item))

    lib_dirs = [os.path.join(cwd, "pmma", "lib")]

    libs = [shared_name]

    includes = [os.path.join(cwd, "pmma", "core", "hpp_src"), os.path.join(cwd, "pmma", "extern", "include")]

    if add_numpy:
        includes += [numpy.get_include()]

    macros = []
    if add_numpy:
        macros.append(('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION'))

    name = component.split(os.sep)[-1].replace(".pyx", "")

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
        depends=depends
    )

ext_modules = [
    make_ext("AdvancedMathematics.pyx", add_numpy=True),
    make_ext("Display.pyx", add_numpy=True, raw_depends=["NumberFormats.pyx"]),
    make_ext(os.path.join("Events", "KeyEvents.pyx")),
    make_ext(os.path.join("Events", "KeyPadEvents.pyx")),
    make_ext(os.path.join("Events", "WindowEvents.pyx")),
    make_ext(os.path.join("Events", "ControllerEvents.pyx"), add_numpy=True),
    make_ext(os.path.join("Events", "MouseEvents.pyx"), add_numpy=True),
    make_ext("FractalBrownianMotion.pyx", add_numpy=True),
    make_ext("NumberFormats.pyx", add_numpy=True),
    make_ext("PerlinNoise.pyx", add_numpy=True),
    make_ext("PMMA_Core.pyx", raw_depends=["General.pyx"]),
    make_ext("TextRenderer.pyx", add_numpy=True),
    make_ext("General.pyx", add_numpy=True),
    make_ext("Shapes2D.pyx", add_numpy=True, raw_depends=["NumberFormats.pyx"]),
    make_ext("Passport.pyx", raw_depends=["General.pyx", "Logger.pyx"]),
    make_ext("Logger.pyx"),
    make_ext("Animation.pyx", add_numpy=True, raw_depends=["NumberFormats.pyx"])
]

# Read the long description from README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read the requirements from requirements.txt
with open("requirements.txt", "r", encoding="utf-8") as req_file:
    requirements = req_file.read().splitlines()

packages = ['pmma']

if __name__ == '__main__':
    multiprocessing.freeze_support()

    use_parallel = True
    if '--no-parallel' in sys.argv:
        use_parallel = False
        sys.argv.remove('--no-parallel')

    annotate_build = "--annotate_build" in sys.argv
    if annotate_build:
        sys.argv.remove("--annotate_build")

    if use_parallel:
        cython_command = cythonize(ext_modules, compiler_directives={"language_level": "3"}, annotate=annotate_build, nthreads=multiprocessing.cpu_count())
    else:
        cython_command = cythonize(ext_modules, compiler_directives={"language_level": "3"}, annotate=annotate_build)

    setup(
        name="pmma",
        version="5.0.15",
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
        ext_modules=cython_command, # nthreads=multiprocessing.cpu_count()
    )