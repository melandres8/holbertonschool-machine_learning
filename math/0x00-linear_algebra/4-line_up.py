#!/usr/bin/env python3
def add_arrays(arr1, arr2):
    """Adds two arrays alement-wise
    Args:
        arr1 ([int]): a list of elements
        arr2 ([int]): a list of elements
    """
    arr = []
    if len(arr1) != len(arr2):
        return None
    else:
        for num1, num2 in zip(arr1, arr2):
            arr.append(num1 + num2)

    return arr
