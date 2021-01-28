#!/usr/bin/env python3
"""Sigma function"""


def summation_i_squared(n):
    """Summation"""
    if n > 0 and isinstance(n, int):
        return int(n * (n + 1) * (2 * n + 1) / 6)
    else:
        return None
