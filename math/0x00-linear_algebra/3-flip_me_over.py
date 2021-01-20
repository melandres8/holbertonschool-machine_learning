#!/usr/bin/env python3
"""Transpose function"""

def matrix_transpose(matrix):
    """Returns the transpose of a 2D matrix.
    Args:
        matrix ([int]): a list of elements
    """
    transpose = []
    rows = len(matrix)
    columns = len(matrix[0])
    for i in range(columns):
        transpose.append([])
        for j in range(rows):
            transpose[i].append(matrix[j][i])

    return transpose
