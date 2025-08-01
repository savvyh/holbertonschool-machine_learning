#!/usr/bin/env python3
"""
Module that adds two matrices
"""


def add_matrices2D(mat1, mat2):
    """
    Adds two matrices
    """
    if len(mat1) != len(mat2):
        return None

    if len(mat1[0]) != len(mat2[0]):
        return None

    new_matrix = []
    for i in range(len(mat1)):
        new_row = []
        for j in range(len(mat2)):
            new_row.append(mat1[i][j] + mat2[i][j])
        new_matrix.append(new_row)

    return new_matrix
