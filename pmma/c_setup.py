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
            extra_compile_args=["/O2"],
            define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')],
        ),
        Extension(
            "extended_perlin_noise",
            [cython_src_path+"extended_perlin_noise.pyx"],
            include_dirs=[numpy.get_include()],
            extra_compile_args=["/O2"],
            define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')],
        ),
        Extension(
            "number_converter",
            [cython_src_path+"number_converter.pyx"],
            include_dirs=[numpy.get_include()],
            extra_compile_args=["/O2"],
            define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')],
        ),
        Extension(
            "math_utils",
            [cython_src_path+"math_utils.pyx"],
            include_dirs=[numpy.get_include()],
            extra_compile_args=["/O2"],
            define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')],
        ),
        Extension(
            "render_pipeline_utils",
            [cython_src_path+"render_pipeline_utils.pyx"],
            include_dirs=[numpy.get_include()],
            extra_compile_args=["/O2"],
            define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')],
        ),
        Extension(
            "render_pipeline_manager_utils",
            [cython_src_path+"render_pipeline_manager_utils.pyx"],
            include_dirs=[numpy.get_include()],
            extra_compile_args=["/O2"],
            define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')],
        )
    ]
elif compiler == "gcc" or compiler == "unix":
    extensions = [
        Extension(
            "perlin_noise",
            [cython_src_path+"perlin_noise.pyx"],
            extra_compile_args=["-O3"],
            define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')],
        ),
        Extension(
            "extended_perlin_noise",
            [cython_src_path+"extended_perlin_noise.pyx"],
            include_dirs=[numpy.get_include()],
            extra_compile_args=["-O3"],
            define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')],
        ),
        Extension(
            "number_converter",
            [cython_src_path+"number_converter.pyx"],
            include_dirs=[numpy.get_include()],
            extra_compile_args=["-O3"],
            define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')],
        ),
        Extension(
            "math_utils",
            [cython_src_path+"math_utils.pyx"],
            include_dirs=[numpy.get_include()],
            extra_compile_args=["-O3"],
            define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')],
        ),
        Extension(
            "render_pipeline_utils",
            [cython_src_path+"render_pipeline_utils.pyx"],
            include_dirs=[numpy.get_include()],
            extra_compile_args=["-O3"],
            define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')],
        ),
        Extension(
            "render_pipeline_manager_utils",
            [cython_src_path+"render_pipeline_manager_utils.pyx"],
            include_dirs=[numpy.get_include()],
            extra_compile_args=["-O3"],
            define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')],
        )
    ]
else:
    extensions = [
        Extension(
            "perlin_noise",
            [cython_src_path+"perlin_noise.pyx"],
            define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')],
        ),
        Extension(
            "extended_perlin_noise",
            [cython_src_path+"extended_perlin_noise.pyx"],
            include_dirs=[numpy.get_include()],
            define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')],
        ),
        Extension(
            "number_converter",
            [cython_src_path+"number_converter.pyx"],
            include_dirs=[numpy.get_include()],
            define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')],
        ),
        Extension(
            "math_utils",
            [cython_src_path+"math_utils.pyx"],
            include_dirs=[numpy.get_include()],
            define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')],
        ),
        Extension(
            "render_pipeline_utils",
            [cython_src_path+"render_pipeline_utils.pyx"],
            include_dirs=[numpy.get_include()],
            define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')],
        ),
        Extension(
            "render_pipeline_manager_utils",
            [cython_src_path+"render_pipeline_manager_utils.pyx"],
            include_dirs=[numpy.get_include()],
            define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')],
        )
    ]

setup(
    ext_modules=cythonize(extensions),
)