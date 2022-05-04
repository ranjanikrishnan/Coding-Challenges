import unittest
from ctci.arrays_and_strings.zero_matrix.zero_matrix import zero_matrix, print_matrix


class TestZeroMatrix(unittest.TestCase):
    def test_zero_matrix(self):
        input_matrix = [[1, 2, 0], [4, 0, 3], [9, 7, 8]]
        print('Input matrix: \n')
        print_matrix(input_matrix)
        output_matrix = [[0, 0, 0], [0, 0, 0], [9, 0, 0]]
        result = zero_matrix(input_matrix)
        print('Output matrix: \n')
        print_matrix(result)
        self.assertEqual(result, output_matrix)
