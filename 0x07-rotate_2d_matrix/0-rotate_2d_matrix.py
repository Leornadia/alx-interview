#!/usr/bin/python3
"""
Module 0-rotate_2d_matrix
Contains function that rotates a 2D matrix 90 degrees clockwise in-place
"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix 90 degrees clockwise in-place

    Args:
        matrix: A list of lists representing the 2D matrix
    """
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            # Perform a 4-way swap for each element in the current layer
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = temp
