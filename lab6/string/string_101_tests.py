import unittest
from string_101 import *

class TestString(unittest.TestCase):
    def test_str_rot_13_1(self):
        self.assertEqual(str_rot_13('APPLES'), 'NCCYRF')
    def test_str_rot_13_2(self):
        self.assertEqual(str_rot_13('APPLES578'), 'NCCYRF578')
    def test_str_rot_13_3(self):
        self.assertEqual(str_rot_13('Hello world!'), 'Uryyb jbeyq!')

    def test_str_translate_101_1(self):
        self.assertEqual(str_translate_101('Whattup homie', 't', 'z'), 'Whazzup homie')
    def test_str_translate_101_2(self):
        self.assertEqual(str_translate_101('I am a b', 'b', 'c'), 'I am a c')
    def test_str_translate_101_3(self):
        self.assertEqual(str_translate_101('AAAA   AAAA', ' ', 'X'), 'AAAAXXXAAAA')


if __name__ == '__main__':
    unittest.main()
