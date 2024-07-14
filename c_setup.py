from setuptools import setup, Extension
import os

import numpy
from Cython.Build import cythonize

def _up(path: str) -> str:
    return path[::-1].split(os.sep, 1)[-1][::-1]

base_path = _up(__file__)

cython_src_path = base_path+os.sep+"cython_src"+os.sep+"utility"+os.sep

extensions = [
    Extension(
        "perlin_noise",
        [cython_src_path+"perlin_noise.pyx"],
        extra_compile_args=["-O3"],  # Use optimization flag DEBUG THIS
    ),
    Extension(
        "extended_perlin_noise",
        [cython_src_path+"extended_perlin_noise.pyx"],
        include_dirs=[numpy.get_include()],
        extra_compile_args=["-O3"],  # Use optimization flag
    ),
    Extension(
        "laminator",
        [cython_src_path+"laminator.pyx"],
        extra_compile_args=["-O3"],  # Use optimization flag
    ),
    Extension(
        "parallel_executor",
        [cython_src_path+"parallel_executor.pyx"],
        extra_compile_args=["-O3"],  # Use optimization flag
    )
]

setup(
    ext_modules=cythonize(extensions),
)