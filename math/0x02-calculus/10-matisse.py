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
        i = 1
        result = []
        while i < len(poly):
            result.append(poly[i] * i)
            i += 1
        return result
