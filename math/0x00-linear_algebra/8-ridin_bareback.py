#!/usr/bin/env python3
"""Matrix multiplication function"""


def mat_mul(mat1, mat2):
    """Performs matrix multiplication

    Args:
        mat1 ([int]): a list of elements
        mat2 ([int]): a list of elements
    """
    # Number of mat1[0] columns must be equal to number of mat2 rows
    matrix = []
    col2 = len(mat2[0])
    col1 = len(mat1[0])
    row1 = len(mat1)
    if len(mat1[0]) != len(mat2):
        return None
    else:
        for i in range(row1):
            row = []
            for j in range(col2):
                operation = 0
                for k in range(col1):
                    operation += mat1[i][k] * mat2[k][j]
                row.append(operation)
            matrix.append(row)
        return matrix
