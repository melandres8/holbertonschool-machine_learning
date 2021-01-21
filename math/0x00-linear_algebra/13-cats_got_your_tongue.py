#!/usr/bin/env python3
"""Concatenate matrices"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Concatenates two matrices along specific axis.

    Args:
        mat1 ([int]): a list of elements
        mat2 ([int]): a list of elements
    """
    return np.concatenate((mat1, mat2), axis)
