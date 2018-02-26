import unittest
from conditional import *

class TestCases(unittest.TestCase):
    def test_max_101_1(self):
        self.assertEqual(max_101(50, 25), 50)
    def test_max_101_2(self):
        self.assertEqual(max_101(0, 100), 100)
    def test_max_101_3(self):
        self.assertEqual(max_101(-10, 0), 0)
    def test_max_101_4(self):
        self.assertEqual(max_101(-50, 50), 50)

    def test_max_of_three_1(self):
        self.assertEqual(max_of_three(10.0, 5.0, 17.0), 17.0)
    def test_max_of_three_2(self):
        self.assertEqual(max_of_three(-5.0, 0.0, 5.0), 5.0)
    def test_max_of_three_3(self):
        self.assertEqual(max_of_three(-100.0, -57.4, -11.4), -11.4)
    def test_max_of_three_4(self):
        self.assertEqual(max_of_three(5.5, -18.2, 44.94), 44.94)

    def test_rental_late_fee_1(self):
        self.assertEqual(rental_late_fee(-5), 0)
    def test_rental_late_fee_2(self):
        self.assertEqual(rental_late_fee(25), 100)
    def test_rental_late_fee_3(self):
        self.assertEqual(rental_late_fee(15), 7)
    def test_rental_late_fee_4(self):
        self.assertEqual(rental_late_fee(1000), 100)

# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
