#!/usr/bin/python3
"""Rotating 2d matrix"""


def rotate_2d_matrix(matrix):
    """
    Prototype for matrix to be rotated 90 degrees
    """

    n = len(matrix)

    # transpose matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse each row
            for i in range(n):
                matrix[i].reverse()


if __name__ == "--main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    rotate_2d_matrix(matrix)
    print(matrix)
