#!/usr/bin/python3
"""
    Generates Pascal's Triangle up to the nth row.
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the nth row.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list of lists: A list of lists representing Pascal's Triangle.
                       Returns an empty list if n <= 0.
    """
    row = [1]
    temp = [0]
    triangle = []

    if n <= 0:
        return triangle

    for i in range(n):
        triangle.append(row)
        row = [l+r for l, r in zip(row + temp, temp + row)]
    return triangle
