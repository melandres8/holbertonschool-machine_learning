#!/usr/bin/env python3
def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenates two matrices along specific axis

    Args:
        mat1 ([int]): a list of elements.
        mat2 ([int]): a list of elements.
        axis (int, optional): Defaults to 0.
    """
    new_matrix = []

    if len(mat1[0]) != len(mat2[0]) and axis == 0:
        return None
    if len(mat1) != len(mat2) and axis == 1:
        return None

    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j])
        if axis == 1:
            for j in range(len(mat2[0])):
                row.append(mat2[i][j])
        new_matrix.append(row)
    if axis == 0:
        for i in range(len(mat2)):
            row = []
            for j in range(len(mat2[0])):
                row.append(mat2[i][j])
            new_matrix.append(row)

    return new_matrix
