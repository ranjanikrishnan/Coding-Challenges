import unittest
from string_permutation import string_permutation_one, string_permutation_two


class TestDuplicateCharacters(unittest.TestCase):
    def test_string_permutation(self):
        result = string_permutation_one("kut", "tuk")
        self.assertEqual(result, True)

        result = string_permutation_one("abcd", "dabc")
        self.assertEqual(result, True)

        result = string_permutation_one("abd", "dabc")
        self.assertEqual(result, False)

        result = string_permutation_one("cad", "gdc")
        self.assertEqual(result, False)

    def test_string_permutation_two(self):
        result = string_permutation_two("aacd", "dabc")
        self.assertEqual(result, False)

        result = string_permutation_two("cad", "gdc")
        self.assertEqual(result, False)

        result = string_permutation_two("abd", "dabc")
        self.assertEqual(result, False)

        result = string_permutation_two("abcd", "dabc")
        self.assertEqual(result, True)

        result = string_permutation_two("kut", "tuk")
        self.assertEqual(result, True)

