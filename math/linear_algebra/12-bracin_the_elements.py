#!/usr/bin/env python3
"""Module that performs element-wise matrix operations."""


def np_elementwise(mat1, mat2):
    """Performs element-wise addition, subtraction, multiplication,
    and division.

    Args:
        mat1: a numpy.ndarray (or array-like).
        mat2: a numpy.ndarray, int, or float.

    Returns:
        A tuple (sum, difference, product, quotient), element-wise.
    """
    return mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2
