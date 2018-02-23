import unittest
from strspn import *

class TestCases(unittest.TestCase):
    def test_my_strspn_01(self):
        self.assertEqual(3, my_strspn("calpoly", "california"))
    def test_my_strspn_02(self):
        self.assertEqual(4, my_strspn("alligator", "illa"))
    def test_my_strspn_03(self):
        self.assertEqual(0, my_strspn("apple", "birk"))
    def test_my_strspn_04(self):
        self.assertEqual(8, my_strspn("swedishdogsgobjork", "hsidews"))
    def test_my_strspn_05(self):
        self.assertEqual(3, my_strspn("hey man", "ehyma"))
    def test_my_strspn_06(self):
        self.assertEqual(6, my_strspn("hello world", "hellocat "))




# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
