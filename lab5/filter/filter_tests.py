import unittest
import filter

class TestCases(unittest.TestCase):
    def test_are_positive_1(self):
        iList = [1, 3, 5, -9, 8]
        oList = [1, 3, 5, 8]
        self.assertListEqual(filter.are_positive(iList), oList)
    def test_are_positive_2(self):
        iList = [-3, 0, -10, -50, 5]
        oList = [5]
        self.assertListEqual(filter.are_positive(iList), oList)
    def test_are_greater_than_n_1(self):
        iList = [-100, 10, 90]
        n = 10
        oList = [90]
        self.assertListEqual(filter.are_greater_than_n(iList, n), oList)
    def test_are_greater_than_n_2(self):
        iList = [0, -50, 4]
        n = -20
        oList = [0, 4]
        self.assertListEqual(filter.are_greater_than_n(iList, n), oList)
    def test_are_divisible_by_n_1(self):
        iList = [10, 9, 6]
        n = 3
        oList = [9, 6]
        self.assertListEqual(filter.are_divisible_by_n(iList, n), oList)
    def test_are_divisible_by_n_2(self):
        iList = [0, -1, 8, 12, -16]
        n = 4
        oList = [0, 8, 12, -16]
        self.assertListEqual(filter.are_divisible_by_n(iList, n), oList)



# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
