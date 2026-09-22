#!/usr/bin/env python3
"""Module for calculating the integral of a polynomial."""


def poly_integral(poly, C=0):
    """Calculate the integral of a polynomial represented as a list."""
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    if not isinstance(C, (int, float)):
        return None
    if not all(isinstance(c, (int, float)) for c in poly):
        return None
    if poly == [0]:
        return [C]

    integral = [C]
    for i in range(len(poly)):
        coeff = poly[i] / (i + 1)
        if coeff == int(coeff):
            coeff = int(coeff)
        integral.append(coeff)

    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()

    return integral
