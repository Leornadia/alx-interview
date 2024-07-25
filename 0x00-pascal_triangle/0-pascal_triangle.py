#!/usr/bin/python3
"""
This module provides a function to generate Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to n rows.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists representing Pascal's Triangle.
               Returns an empty list if n <= 0.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)

    return triangle
