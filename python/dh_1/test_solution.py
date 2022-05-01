import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_solution(self):
        solution = Solution()
        # generated_str = solution.longest_diverse_string(6, 1, 1)
        # self.assertEqual(generated_str, "aabaacaa")
        # generated_str = solution.longest_diverse_string(1, 3, 1)
        # self.assertEqual(generated_str, "bbabc")
        generated_str = solution.longest_diverse_string(0, 1, 8)
        self.assertEqual(generated_str, "ccbcc")
        # generated_str = longestDiverseString(1, 3, 1)
        # self.assertEqual(generated_str, "bbabc")

