#!/usr/bin/python3
"""
Pascal Triangle
"""


def pascal_triangle(n):
    """
    A function that returns the first n rows of the pascal triangle
    """
    triangle = []
    if n <= 0:
        return triangle
    else:
        for i in range(n):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    data = triangle[i - 1][j - 1] + triangle[i - 1][j]
                    row.append(data)
            triangle.append(row)
    return triangle
