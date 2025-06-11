import unittest
from bowling import calc_score

class TestCalcScore(unittest.TestCase):
    def test_does_simple_numbers(self):
        self.assertEqual(calc_score("11 11 11 11"), 8)

