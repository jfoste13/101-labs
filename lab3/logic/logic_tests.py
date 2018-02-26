import unittest
from logic import *

class TestCases(unittest.TestCase):
    def test_is_even_1(self):
        self.assertTrue(is_even(8))
    def test_is_even_2(self):
        self.assertFalse(is_even(5))
    def test_is_even_3(self):
        self.assertTrue(is_even(-2))
    def test_is_even_4(self):
        self.assertFalse(is_even(-5))

    def test_in_an_interval_1(self):
        self.assertFalse(in_an_interval(9))
    def test_in_an_interval_2(self):
        self.assertTrue(in_an_interval(2))
    def test_in_an_interval_3(self):
        self.assertTrue(in_an_interval(102))
    def test_in_an_interval_4(self):
        self.assertFalse(in_an_interval(500))

# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
