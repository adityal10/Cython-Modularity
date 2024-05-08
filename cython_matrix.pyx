# matrix_operations.pyx
cimport numpy as np
import numpy as np
# cython: language_level=3

def transpose(matrix):
    """
    Transpose the given matrix.
    """
    cdef int i, j
    cdef int rows = len(matrix)
    cdef int cols = len(matrix[0])
    cdef np.ndarray[np.float64_t, ndim=2] transposed = np.zeros((cols, rows), dtype=np.float64)
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    return transposed


def determinant(matrix):
    """
    Calculate the determinant of the given matrix recursively.
    """
    cdef int i
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for i in range(len(matrix)):
            minor = [row[:i] + row[i + 1:] for row in (matrix[1:])]
            det += (-1) ** i * matrix[0][i] * determinant(minor)
        return det


def cofactor(matrix):
    """
    Calculate the cofactor matrix of the given matrix.
    """
    cdef int i, j
    cdef int rows = len(matrix)
    cdef int cols = len(matrix[0])
    cdef np.ndarray[np.float64_t, ndim=2] cofactor_matrix = np.zeros((rows, cols), dtype=np.float64)
    for i in range(rows):
        for j in range(cols):
            minor = [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]
            cofactor_matrix[i][j] = (-1) ** (i + j) * determinant(minor)
    return cofactor_matrix


def inverse(matrix):
    """
    Calculate the inverse of the given matrix.
    """
    cdef int i, j
    cdef int rows = len(matrix)
    cdef int cols = len(matrix[0])
    cdef det = determinant(matrix)
    if det == 0:
        return "Inverse does not exist for a singular matrix"
    else:
        adjoint_matrix = transpose(cofactor(matrix))
        inv_matrix = np.zeros((rows, cols), dtype=np.float64)
        for i in range(rows):
            for j in range(cols):
                inv_matrix[i][j] = adjoint_matrix[i][j] / det
        return inv_matrix


