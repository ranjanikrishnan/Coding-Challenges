from typing import List


def print_matrix(matrix: List[List[int]]) -> None:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print('')


def zero_matrix(matrix: List[List[int]]):
    rows = {}
    columns = {}
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 0:
                rows, columns = mark_zero(r, c, rows, columns)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i in rows or j in columns:
                matrix[i][j] = 0

    # for r in rows.keys():
    #     for j in range(len(matrix)):
    #         matrix[r][j] = 0
    # for i in range(len(matrix)):
    #     for c in columns.keys():
    #         matrix[i][c] = 0
    return matrix


def mark_zero(r, c, rows, columns):
    rows[r] = True
    columns[c] = True
    return rows, columns
