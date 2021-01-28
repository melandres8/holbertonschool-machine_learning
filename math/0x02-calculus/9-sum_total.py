#!/usr/bin/env python3
"""Sigma function"""


def summation_i_squared(n):
    """Summation"""
    if n > 0 and isinstance(n, int):
        return int(((n ** 2 * 2 + 5) * 2) / 2)
    else:
        return None
