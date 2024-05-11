# Matrix Operations - Cython and Modularity


This project demonstrates the calculation of the inverse of a matrix using both Python and Cython implementations.

## Setup

To compile the Cython code and install the necessary dependencies, run the following command:

```bash
python setup.py build_ext --inplace
```

This command compiles the Cython code and generates the Python extension module required for the Cython implementation.

## Requirements for succesfully running setup.py
1. **Cython Installed:** Make sure you have Cython installed on your system. You can install Cython using pip: `pip install cython`
2. **Microsoft Studio C++ Version 14 or Greater:** You need to have Microsoft Visual C++ Build Tools installed, specifically version 14.0 or greater. This is required for compiling the Cython code on Windows.
3. **Include NumPy's Include Directory:** When setting up the project in setup.py, include NumPy's include directory to ensure compatibility: `include_dirs=[np.get_include()]` 

## Files

### `setup.py`

This file is used to set up the project for building the Cython extension module. It uses `setuptools` and `Cython.Build` to compile the Cython code (`cython_matrix.pyx`). Additionally, it includes NumPy's include directory to ensure compatibility.

### `main.py`

This file contains the main code for running the matrix operations. It imports the Python and Cython implementations of the inverse function from `matrix_operations.pyx` and `cython_matrix.pyx` respectively. The `main()` function demonstrates the usage of both implementations and measures their running time.

### `matrix_operations.pyx`

This file contains the Python implementation of matrix operations. It includes functions for transposing a matrix, calculating its determinant recursively, computing the cofactor matrix, and finding the inverse of a matrix.

### `cython_matrix.pyx`

This file contains the Cython implementation of matrix operations. It includes functions similar to those in `matrix_operations.pyx`, but with optimizations provided by Cython.

## Usage

To run the matrix operations, execute the `main.py` file:

```bash
python main.py
```

This will demonstrate the usage of both Python and Cython implementations and measure their running time.
