import unittest
from ctci.arrays_and_strings.string_compression.string_compression import string_compression


class TestStringCompression(unittest.TestCase):
    def test_string_compression(self):
        input_string_1 = ["aabcccccaaa", "abc", "aabbcc"]
        output = ["a2b1c5a3", "abc", "aabbcc"]
        for i in range(len(input_string_1)):
            result = string_compression(input_string_1[i])
            self.assertEqual(result, output[i])
