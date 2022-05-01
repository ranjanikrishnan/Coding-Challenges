import unittest
from hackerrank.parcels.parcels import get_minimum_days


class TestParcels(unittest.TestCase):
    def test_parcels(self):
        # input_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        # print_matrix(input_matrix)
        # output_matrix = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        input_parcels = [9,5,4,9,3,2,3]
        result = get_minimum_days(input_parcels)
        self.assertEqual(result, 5)