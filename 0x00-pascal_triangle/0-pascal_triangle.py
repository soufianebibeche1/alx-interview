#!/usr/bin/python3
"""
    Generates Pascal's Triangle up to the nth row.
"""


def pascal_triangle(n):
    """
        Generates Pascal's Triangle up to the nth row.
        Args:
            n (int): number of lists and digits
        Returns: list of lists
    """
    t_row = [1]
    temp_l = [0]
    pTri = []

    if n <= 0:
        return pTri

    for i in range(n):
        pTri.append(t_row)
        t_row = [l+r for l, r in zip(t_row + temp_l, temp_l + t_row)]
    return pTri
