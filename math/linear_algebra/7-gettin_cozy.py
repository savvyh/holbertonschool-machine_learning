#!/usr/bin/env python3
"""
Module that concatenates two matrices along a specific axis
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis
    """
    new_matrix = []
    if axis == 0:
        new_matrix = mat1 + mat2
    elif axis == 1:
        for i in range(len(mat1)):
            new_matrix.append(mat1[i] + mat2[i])
        return new_matrix
    else:
        new_matrix = mat1 + mat2
        new_matrix.append(mat1[i] + mat2[i])
        return new_matrix

    return new_matrix
