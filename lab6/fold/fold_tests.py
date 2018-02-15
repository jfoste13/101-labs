import unittest
from fold import *

class TestCases(unittest.TestCase):
    def test_sum_1(self):
        self.assertEqual(sum([2, 4, 3]), 9)
    def test_sum_2(self):
        self.assertEqual(sum([-9, 10, -3]), -2)
    def test_index_of_smallest_1(self):
        self.assertEqual(index_of_smallest([7, 9, 3]), 2)
    def test_index_of_smallest_2(self):
        self.assertEqual(index_of_smallest([0, 9, 3]), 0)
    def test_index_of_smallest_3(self):
        self.assertEqual(index_of_smallest([0, -5, -5]), 1)
    def test_index_of_smallest_4(self):
        self.assertEqual(index_of_smallest([]), -1)



# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
