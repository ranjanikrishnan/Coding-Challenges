import unittest
from ctci.arrays_and_strings.urlify.urlify import urlify, shift_characters_two_ahead, string_to_chars


class TestUrlify(unittest.TestCase):
    def test_urlify(self):
        input = string_to_chars("Mr John Smith    ")
        expected = string_to_chars("Mr%20John%20Smith")
        result = urlify(input, 13)
        self.assertEqual(expected, result)

        input = string_to_chars("Mr John Sm Op He ro          ")
        expected = string_to_chars("Mr%20John%20Sm%20Op%20He%20ro")
        result = urlify(input, 19)
        self.assertEqual(expected, result)

    def test_shift_characters_two_ahead(self):
        input_string = "john smith  "  # "jo sm he    "
        output_string = "john%20smith"  # "jo%20sm he  "
        index = 4  # 2
        true_length = 10
        character_array = string_to_chars(input_string)

        shift_characters_two_ahead(character_array, index, true_length)
        self.assertEqual(character_array, string_to_chars(output_string))
