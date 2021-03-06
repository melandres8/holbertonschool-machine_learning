#!/usr/bin/env python3
"""Derive happiness in oneself from a good day's work"""


def poly_derivative(poly):
    """Derivative func"""
    if len(poly) == 1:
        return [0]
    elif not isinstance(poly, list):
        return None
    elif len(poly) == 0:
        return None
    else:
        return [poly[i] * i for i in range(1, len(poly))]
