#!/usr/bin/env python3
"""Definiteness of a matrix"""
import numpy as np


def definiteness(matrix):
    """Calculates the definiteness of a matrix

    matrix: numpy.ndarray of shape (n, n)
    Returns: the definiteness as a string, or None
    """
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")
    if (matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1] or
            matrix.size == 0):
        return None
    if not np.allclose(matrix, matrix.T):
        return None
    w = np.linalg.eigvalsh(matrix)
    tol = 1e-10
    pos = w > tol
    neg = w < -tol
    if pos.all():
        return "Positive definite"
    if neg.all():
        return "Negative definite"
    if not neg.any():
        return "Positive semi-definite"
    if not pos.any():
        return "Negative semi-definite"
    return "Indefinite"
