#!/usr/bin/env python3
"""element wise functions"""


def np_elementwise(mat1, mat2):
    """Performs element-wise addition, substraction,
        multiplication and division.

    Args:
        mat1 ([int]): a list of elements
        mat2 ([int]): a list of elements
    """
    return mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2
