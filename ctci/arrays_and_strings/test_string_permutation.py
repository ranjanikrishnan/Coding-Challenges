import unittest
from string_permutation import string_permutation


class TestDuplicateCharacters(unittest.TestCase):
    def test_string_permutation(self):
        result = string_permutation("kut", "tuk")
        self.assertEqual(result, True)

        result = string_permutation("abcd", "dabc")
        self.assertEqual(result, True)

        result = string_permutation("abd", "dabc")
        self.assertEqual(result, False)

        result = string_permutation("cad", "gdc")
        self.assertEqual(result, False)

