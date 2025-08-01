#!/usr/bin/env python3
"""
Module that contains the function matrix_transpose
"""


def matrix_transpose(matrix):
    """
    Returns the transpose of the matrix
    """
    rows = len(matrix)
    cols = len(matrix[0])
    new_matrix = [[0] * rows for i in range(cols)]

    for i in range(rows):
        for j in range(cols):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix
