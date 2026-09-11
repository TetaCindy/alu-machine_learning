#!/usr/bin/env python3
"""Module that returns the transpose of a 2D matrix."""


def matrix_transpose(matrix):
    """Returns the transpose of a 2D matrix.

    Args:
        matrix: a 2D list representing the matrix.

    Returns:
        A new 2D list that is the transpose of matrix.
    """
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
