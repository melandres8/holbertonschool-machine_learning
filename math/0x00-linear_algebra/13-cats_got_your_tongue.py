#!/usr/bin/env python3
import numpy as np
"""Concatenate matrices"""


def np_cat(mat1, mat2, axis=0):
    """Concatenates two matrices along specific axis.

    Args:
        mat1 ([int]): a list of elements
        mat2 ([int]): a list of elements
    """
    return np.concatenate((mat1, mat2), axis)
