from setuptools import setup
from Cython.Build import cythonize

import os

setup(
    ext_modules=cythonize(
        "pyx_src"+os.sep+"utility"+os.sep+"perlin_noise.pyx")
)
