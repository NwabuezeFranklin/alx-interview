#!/usr/bin/python3
"""
Pascal Trangle
"""


def pascal_triangle(n):
    '''
    Creates a list of lists of integers in a Pascal's triangle
    of a given integer.
    '''
    if n <= 0:
        return []
    else:
        res = []
        for i in range(n):
            if len(res) == 0:
                res.append([1])
            else:
                row = [1]
                for j in range(1, len(res[-1])):
                    row.append(res[-1][j] + res[-1][j - 1])
                row.append(1)
                res.append(row)
        return res
