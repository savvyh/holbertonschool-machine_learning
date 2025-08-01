#!/usr/bin/env python3
"""
Module that adds two arrays element-wise
"""


def add_arrays(arr1, arr2):
    """
    Adds two arrays element-wise
    """
    if len(arr1) != len(arr2):
        return None

    new_list = []
    for i in range(len(arr1)):
        new_list.append(arr1[i] + arr2[i])

    return new_list
