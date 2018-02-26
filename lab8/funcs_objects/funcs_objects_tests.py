import unittest
from objects import *
from funcs_objects import *

class TestCases(unittest.TestCase):
    def test_point(self):
        p = Point(1, 5)
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 5)

    def test_circle(self):
        p = Point(2, 2)
        c = Circle(p, 5)
        self.assertEqual(c.point.x, 2)
        self.assertEqual(c.point.y, 2)
        self.assertEqual(c.radius, 5)

    def test_distance_1(self):
        p1 = Point(1, 1)
        p2 = Point(4, 4)
        self.assertEqual(distance(p1, p2), 4.242640687119285146405066172629094235709015626130844219530)
    def test_distance_2(self):
        p1 = Point(0, 0)
        p2 = Point(5, 0)
        self.assertEqual(distance(p1, p2), 5)

    def test_circles_overlap_1(self):
        p1 = Point(1, 1)
        p2 = Point(4, 4)
        c1 = Circle(p1, 2)
        c2 = Circle(p2, 2)
        self.assertEqual(circles_overlap(c1, c2), False)
    def test_circles_overlap_2(self):
        p1 = Point(1, 1)
        p2 = Point(4, 4)
        c1 = Circle(p1, 2)
        c2 = Circle(p2, 3)
        self.assertEqual(circles_overlap(c1, c2), True)

if __name__ == '__main__':
   unittest.main()
