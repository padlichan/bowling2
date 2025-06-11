import unittest
from bowling import calc_score

class TestCalcScore(unittest.TestCase):
    def test_does_one_empty(self):
        self.assertEqual(calc_score(""), 0)

    def test_does_one_strike(self):
        self.assertEqual(calc_score("X"), 10)

    def test_does_one_open_frame(self):
        self.assertEqual(calc_score("23"), 5)
