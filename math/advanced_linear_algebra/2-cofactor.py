#!/usr/bin/env python3
"""Module for calculating the cofactor matrix of a matrix."""
minor = __import__('1-minor').minor


def cofactor(matrix):
    """Calculate the cofactor matrix of a matrix."""
    m = minor(matrix)
    n = len(m)
    return [[((-1) ** (i + j)) * m[i][j] for j in range(n)]
            for i in range(n)]
