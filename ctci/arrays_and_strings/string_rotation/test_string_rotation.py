import unittest
from ctci.arrays_and_strings.string_rotation.string_rotation import string_rotation


class TestStringRotation(unittest.TestCase):
    def test_string_rotation(self):
        input_string_1 = "waterbottle"
        input_string_2 = "ttlewaterbo"
        result = string_rotation(input_string_1, input_string_2)
        self.assertEqual(result, True)

        input_string_1 = "waterbottle"
        input_string_2 = "ttlewaterb"
        result = string_rotation(input_string_1, input_string_2)
        self.assertEqual(result, False)
