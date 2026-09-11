#!/usr/bin/env python3
"""Module that adds two arrays element-wise."""


def add_arrays(arr1, arr2):
    """Adds two arrays element-wise.

    Args:
        arr1: a list of ints/floats.
        arr2: a list of ints/floats.

    Returns:
        A new list containing the element-wise sum of arr1 and arr2,
        or None if arr1 and arr2 are not the same shape.
    """
    if len(arr1) != len(arr2):
        return None
    return [a + b for a, b in zip(arr1, arr2)]
