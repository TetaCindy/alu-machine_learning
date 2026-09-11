#!/usr/bin/env python3
"""Module that transposes a numpy.ndarray."""


def np_transpose(matrix):
    """Transposes a numpy.ndarray.

    Args:
        matrix: a numpy.ndarray (or array-like).

    Returns:
        A new numpy.ndarray that is the transpose of matrix.
    """
    return matrix.transpose()
