#!/usr/bin/env python3
"""Adjugate matrix of a matrix"""
cofactor = __import__('2-cofactor').cofactor


def adjugate(matrix):
    """Calculates the adjugate matrix of a matrix

    matrix: list of lists whose adjugate matrix should be calculated
    Returns: the adjugate matrix of matrix
    """
    cof = cofactor(matrix)
    return [list(col) for col in zip(*cof)]
