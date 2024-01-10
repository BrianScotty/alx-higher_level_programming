#!/usr/bin/python3
"""Pascal's Triangle"""

def pascal_triangle(n):
    """
    Returns a list  of lists of integers  representing the Pascal's triangle"""

    if n <= 0:
        return []

    pt = [[1]]
    while len(pt) != n:
        triangle = pt[-1]
        tmp = [1]
        for i in range(len(triangle) - 1):
            tmp.append(triangle[i] + triangle[i + 1])
        tmp.append(1)
        pt.append(tmp)
    return pt

