from typing import List


def print_matrix(matrix: List[List[int]]) -> None:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print('')


def matrix_rotation(matrix: List[List[int]]) -> List[List[int]]:
    copied_matrix = [[]] * len(matrix)
    for i in range(len(matrix)):
        position = len(matrix) - 1
        matrix_copy_inner = [0] * len(matrix)
        for j in range(len(matrix[i])):
            matrix_copy_inner[j] = matrix[position][i]
            position = position - 1
        copied_matrix[i] = matrix_copy_inner
    return copied_matrix


def copy_matrix(matrix: List[List[int]]) -> List[List[int]]:
    copied_matrix = [[]] * len(matrix)
    for i in range(len(matrix)):
        matrix_copy_inner = [0] * len(matrix)
        for j in range(len(matrix[i])):
            matrix_copy_inner[j] = matrix[i][j]
        copied_matrix[i] = matrix_copy_inner
    return copied_matrix


def transpose_matrix(matrix: List[List[int]]):
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


def reverse_rows_in_matrix(matrix: List[List[int]]):
    for i in range(len(matrix)):
        # matrix[i] = matrix[i][::-1]
        matrix[i].reverse()
    return matrix


def matrix_rotation_in_place(matrix: List[List[int]]):
    transpose_matrix(matrix)
    reverse_rows_in_matrix(matrix)
    return matrix
