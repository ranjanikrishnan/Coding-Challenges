import unittest
from ctci.arrays_and_strings.permutation_of_palindrome.permutation_of_palindrome import permutation_of_palindrome


class TestPermutationOfPalindrome(unittest.TestCase):
    def test_permutation_of_palindrome(self):
        inputs = ["helleh", "heleh", "tact ocoa", "helloe", "Tact Coa"]
        expected = [True, True, True, False, True]
        for i in range(len(inputs)):
            result = permutation_of_palindrome(inputs[i])
            self.assertEqual(expected[i], result)
