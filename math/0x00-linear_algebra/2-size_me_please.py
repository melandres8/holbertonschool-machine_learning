#!/usr/bin/env python3
"""Shape of a given matrix function"""


def matrix_shape(matrix):
    """ Calculates the shape of a matrix
    Args:
        matrix ([int]): contains all elements
    """
    shape = []
    if not matrix:
        return [0]
    else:
        shape.append(len(matrix))
        while isinstance(matrix[0], list):
            shape.append(len(matrix[0]))
            matrix = matrix[0]
        return shape
