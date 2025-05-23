#!/usr/bin/python3
"""
Module defines a function for pascals triangle
"""


def pascal_triangle(n):
    """
    returns a list representation of pascals triangle
    """
    if n <= 0:
        return []

    triangle = []

    for row_num in range(n):
        row = [1] * (row_num + 1)
        for j in range(1, row_num):
            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
        triangle.append(row)

    return triangle
