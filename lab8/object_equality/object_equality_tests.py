import unittest
from objects import *

class TestCases(unittest.TestCase):
   def test_equality(self):
      p1 = Point(1, 1)
      p2 = Point(1, 1)
      self.assertEqual(p1, p2)
      pass


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
