import unittest
from ctci.arrays_and_strings.one_away.one_away import one_away


class TestOneAway(unittest.TestCase):
    def test_one_away(self):
        input_string_1 = ["pale", "pales", "pale", "pale", "aabcc", "abcd", "aaa"]
        input_string_2 = ["ple", "pale", "bale", "bake", "abbcb", "dcba", "aaa"]
        output = [True, True, True, False, False, False, True]
        for i in range(len(input_string_1)):
            result = one_away(input_string_1[i], input_string_2[i])
            self.assertEqual(result, output[i])

