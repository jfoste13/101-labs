import unittest
from char import *

class test_char(unittest.TestCase):
    def test_is_lower_101_1(self):
        self.assertTrue(is_lower_101('c'))
    def test_is_lower_101_2(self):
        self.assertTrue(is_lower_101('z'))
    def test_is_lower_101_3(self):
        self.assertFalse(is_lower_101('$'))
    def test_is_lower_101_4(self):
        self.assertFalse(is_lower_101('A'))

    def test_char_rot_13_1(self):
        self.assertEqual(char_rot_13('A'), 'N')
    def test_char_rot_13_2(self):
        self.assertEqual(char_rot_13('J'), 'W')
    def test_char_rot_13_3(self):
        self.assertEqual(char_rot_13('Z'), 'M')
    def test_char_rot_13_4(self):
        self.assertEqual(char_rot_13('a'), 'n')
    def test_char_rot_13_5(self):
        self.assertEqual(char_rot_13('j'), 'w')
    def test_char_rot_13_6(self):
        self.assertEqual(char_rot_13('z'), 'm')


if __name__ == '__main__':
    unittest.main()
