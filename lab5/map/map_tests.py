import unittest
import map

class TestCases(unittest.TestCase):
    def test_square_all_1(self):
        iList = [1, 3, 5]
        oList = [1, 9, 25]
        self.assertListEqual(map.square_all(iList), oList)
    def test_square_all_2(self):
        iList = [-3, 0, 10]
        oList = [9, 0, 100]
        self.assertListEqual(map.square_all(iList), oList)
    def test_add_n_all_1(self):
        iList = [-100, -50, 73]
        increment = 5
        oList = [-95, -45, 78]
        self.assertListEqual(map.add_n_all(iList, increment), oList)
    def test_add_n_all_2(self):
        iList = [0, 10, 4]
        increment = 2
        oList = [2, 12, 6]
        self.assertListEqual(map.add_n_all(iList, increment), oList)
    def test_even_or_odd_all_1(self):
        iList = [1, 9, 4]
        oList = [False, False, True]
        self.assertListEqual(map.even_or_odd_all(iList), oList)
    def test_even_or_odd_all_2(self):
        iList = [0, -1, 8]
        oList = [True, False, True]
        self.assertListEqual(map.even_or_odd_all(iList), oList)


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
