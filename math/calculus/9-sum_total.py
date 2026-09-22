#!/usr/bin/env python3
"""Module for calculating summation of i^2."""


def summation_i_squared(n):
    """Calculate sum of i^2 for i = 1 to n without using loops."""
    if not isinstance(n, int) or n < 1:
        return None
    return n * (n + 1) * (2 * n + 1) // 6
