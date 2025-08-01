#!/usr/bin/env python3

def matrix_transpose(matrix):
    """
    Args:
        matrix: list of lists of ints/floats

    Returns:
        The transpose of the matrix
    """
    rows = len(matrix)
    cols = len(matrix[0])
    new_matrix = [[0] * rows for i in range(cols)]

    for i in range(rows):
        for j in range(cols):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix
