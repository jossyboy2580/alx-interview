#!/usr/bin/python3
"""
Rotate a 2 Dimensional Matrix with this function
"""


def rotate_2d_matrix(matrix):
    """
    This function takes a 2 Dimensional matrix as an
    argument and transposes it in the clockwise direction
    """

    size = len(matrix)
    temp = [[0] * size for _ in range(size)]

    for i in range(size):
        for j in range(size):
            temp[i][j] = matrix[size - j - 1][i]

    for i in range(size):
        for j in range(size):
            matrix[i][j] = temp[i][j]
