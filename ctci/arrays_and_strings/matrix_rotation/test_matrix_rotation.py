import unittest
from ctci.arrays_and_strings.matrix_rotation.matrix_rotation import print_matrix, matrix_rotation, copy_matrix


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
