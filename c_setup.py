from setuptools import setup, Extension
import os
import distutils.ccompiler

import numpy
from Cython.Build import cythonize

def _up(path: str) -> str:
    return path[::-1].split(os.sep, 1)[-1][::-1]

base_path = _up(__file__)

cython_src_path = base_path+os.sep+"cython_src"+os.sep+"utility"+os.sep

compiler = distutils.ccompiler.get_default_compiler()

if compiler == "msvc":
    extensions = [
        Extension(
            "perlin_noise",
            [cython_src_path+"perlin_noise.pyx"],
            extra_compile_args=["-O3", "/O2"],
        ),
        Extension(
            "extended_perlin_noise",
            [cython_src_path+"extended_perlin_noise.pyx"],
            include_dirs=[numpy.get_include()],
            extra_compile_args=["-O3", "/O2"],
        ),
        Extension(
            "number_converter",
            [cython_src_path+"number_converter.pyx"],
            include_dirs=[numpy.get_include()],
            extra_compile_args=["-O3", "/O2"],
        )
    ]
elif compiler == "gcc" or compiler == "unix":
    extensions = [
        Extension(
            "perlin_noise",
            [cython_src_path+"perlin_noise.pyx"],
            extra_compile_args=["-O3"],
        ),
        Extension(
            "extended_perlin_noise",
            [cython_src_path+"extended_perlin_noise.pyx"],
            include_dirs=[numpy.get_include()],
            extra_compile_args=["-O3"],
        ),
        Extension(
            "number_converter",
            [cython_src_path+"number_converter.pyx"],
            include_dirs=[numpy.get_include()],
            extra_compile_args=["-O3"],
        )
    ]
else:
    extensions = [
        Extension(
            "perlin_noise",
            [cython_src_path+"perlin_noise.pyx"],
        ),
        Extension(
            "extended_perlin_noise",
            [cython_src_path+"extended_perlin_noise.pyx"],
            include_dirs=[numpy.get_include()],
        ),
        Extension(
            "number_converter",
            [cython_src_path+"number_converter.pyx"],
            include_dirs=[numpy.get_include()],
        )
    ]

setup(
    ext_modules=cythonize(extensions),
)