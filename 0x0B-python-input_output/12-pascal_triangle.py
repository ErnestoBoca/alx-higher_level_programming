#!/usr/bin/python3
"""Pascal Triangle module"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal’s triangle of n"""
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = []
        for j in range(len(triangle[i-1])+1):
            if j == 0 or j == len(triangle[i-1]):
                row.append(1)
            else:
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(row)
    return triangle
