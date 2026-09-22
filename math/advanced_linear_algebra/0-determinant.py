#!/usr/bin/env python3
"""Module that calculates the determinant of a matrix"""


def determinant(matrix):
    """Calculates the determinant of a matrix

    matrix: list of lists whose determinant should be calculated

    Returns: the determinant of matrix
    """
    # Step 1: validate that matrix is a non-empty list of lists
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a list of lists")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Step 2: [[]] is the 0x0 matrix, whose determinant is 1
    if matrix == [[]]:
        return 1

    # Step 3: validate that the matrix is square
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a square matrix")

    # Step 4: base cases
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Step 5: cofactor expansion along the first row
    det = 0
    for j in range(n):
        # minor: remove row 0 and column j
        minor = [row[:j] + row[j + 1:] for row in matrix[1:]]
        det += ((-1) ** j) * matrix[0][j] * determinant(minor)
    return det
