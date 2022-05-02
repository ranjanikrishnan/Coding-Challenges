import unittest
from ctci.arrays_and_strings.matrix_rotation.matrix_rotation import print_matrix, matrix_rotation, \
     copy_matrix, transpose_matrix, reverse_rows_in_matrix, matrix_rotation_in_place


class TestMatrixRotation(unittest.TestCase):
    def test_matrix_rotation(self):
        input_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        print('Input matrix: \n')
        print_matrix(input_matrix)
        output_matrix = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        result = matrix_rotation(input_matrix)
        print('Output matrix: \n')
        print_matrix(result)
        self.assertEqual(result, output_matrix)

        input_matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
        print('Input matrix: \n')
        print_matrix(input_matrix)
        output_matrix = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
        result = matrix_rotation(input_matrix)
        print('Output matrix: \n')
        print_matrix(result)
        self.assertEqual(result, output_matrix)

    def test_copy_matrix(self):
        input_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        copied_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = copy_matrix(input_matrix)
        self.assertEqual(result, copied_matrix)

    def test_transpose_matrix(self):
        input_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        output_matrix = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        matrix = transpose_matrix(input_matrix)
        self.assertEqual(matrix, output_matrix)

    def test_reverse_rows(self):
        input_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        output_matrix = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
        matrix = reverse_rows_in_matrix(input_matrix)
        self.assertEqual(matrix, output_matrix)

    def test_matrix_rotation_in_place(self):
        input_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        print('Input matrix: \n')
        print_matrix(input_matrix)
        output_matrix = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        result = matrix_rotation_in_place(input_matrix)
        print('Output matrix: \n')
        print_matrix(result)
        self.assertEqual(result, output_matrix)

        input_matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
        print('Input matrix: \n')
        print_matrix(input_matrix)
        output_matrix = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
        result = matrix_rotation_in_place(input_matrix)
        print('Output matrix: \n')
        print_matrix(result)
        self.assertEqual(result, output_matrix)
