import unittest
from duplicate_characters import duplicate_characters


class TestDuplicateCharacters(unittest.TestCase):
    def test_duplicate_characters(self):
        has_duplicate_characters = duplicate_characters("wearehere")
        self.assertEqual(has_duplicate_characters, True)

        has_duplicate_characters = duplicate_characters("kutan")
        self.assertEqual(has_duplicate_characters, False)
