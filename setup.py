# setup.py
from setuptools import setup  # important
from Cython.Build import cythonize
import numpy as np

setup(
    ext_modules=cythonize("cython_matrix.pyx"),
    include_dirs=[np.get_include()]
)