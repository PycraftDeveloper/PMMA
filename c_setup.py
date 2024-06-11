from setuptools import setup, Extension
import os

import numpy
from Cython.Build import cythonize

cython_src_path = "cython_src"+os.sep+"utility"+os.sep

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
]

setup(
    ext_modules=cythonize(extensions),
)