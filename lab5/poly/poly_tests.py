import unittest
import poly

class TestPoly(unittest.TestCase):

    def assertListAlmostEqual(self, l1, l2):
       self.assertEqual(len(l1), len(l2))
       for el1, el2 in zip(l1, l2):
          self.assertAlmostEqual(el1, el2)


    # Add tests here
    def test_poly_add2_1(self):
        poly1 = [2.3, 4.7, 1.0]
        poly2 = [1.2, 2.1, -3.2]
        poly3 = poly.poly_add2(poly1, poly2)
        self.assertListAlmostEqual(poly3, [3.5, 6.8, -2.2])
    def test_poly_add2_2(self):
        poly1 = [9.8, 2.2, -5.23]
        poly2 = [-5.0, -2.2, 9.23]
        poly3 = poly.poly_add2(poly1, poly2)
        self.assertListAlmostEqual(poly3, [4.8, 0, 4.0])

    def test_poly_mult2_1(self):
        poly1 = [5, 3, 5]
        poly2 = [3, 4, 2]
        poly3 = poly.poly_mult2(poly1, poly2)
        self.assertListAlmostEqual(poly3, [15, 29, 37, 26, 10])
    def test_poly_mult2_2(self):
        poly1 = [-2.3, 4.3, -99]
        poly2 = [-100.5, 0, 4.3]
        poly3 = poly.poly_mult2(poly1, poly2)
        self.assertListAlmostEqual(poly3, [231.15, -432.15, 9939.61, 18.49, -425.7])

if __name__ == '__main__':
    unittest.main()
