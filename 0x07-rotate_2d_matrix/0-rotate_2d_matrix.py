#!/usr/bin/python3
"""
0-rotate_2d_matrix.py
"""


def rotate_2d_matrix(matrix):
    """rotate it 90 degrees clockwise"""
    n = len(matrix)

    # Step 1: Transpose the matrix (swap rows and columns)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row of the transposed matrix
    for i in range(n):
        matrix[i].reverse()


if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    for row in matrix:
        print(row)
