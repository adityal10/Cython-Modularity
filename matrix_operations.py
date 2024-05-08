# matrix_operations.py
import numpy as np

def transpose(matrix):
    """
    Transpose the given matrix.
    """
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def determinant(matrix):
    """
    Calculate the determinant of the given matrix recursively.
    """
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
    cofactor_matrix = []
    for i in range(len(matrix)):
        cofactor_row = []
        for j in range(len(matrix)):
            minor = [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]
            cofactor_row.append((-1) ** (i + j) * determinant(minor))
        cofactor_matrix.append(cofactor_row)
    return cofactor_matrix


def inverse(matrix):
    """
    Calculate the inverse of the given matrix.
    """
    det = determinant(matrix)
    if det == 0:
        return "Inverse does not exist for a singular matrix"
    else:
        cofactor_matrix = cofactor(matrix)
        adjoint_matrix = transpose(cofactor_matrix)
        inv_matrix = [[adjoint_matrix[i][j] / det for j in range(len(adjoint_matrix[0]))] for i in range(len(adjoint_matrix))]
        return inv_matrix
