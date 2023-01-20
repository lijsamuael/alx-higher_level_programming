"""This module tests the Square class using unittests"""
import unittest
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """Tests the Square class"""

    def setUp(self):
        """Resets the class to prevent interference"""
        Base._Base__nb_objects = 0

    def test_init(self):
        """Tests that squares are initialized properly"""
        s1 = Square(4)
        self.assertEqual(s1.width, 4)
        self.assertEqual(s1.height, 4)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        s2 = Square(5, 2, 3, 47)
        self.assertEqual(s2.width, 5)
        self.assertEqual(s2.height, 5)
        self.assertEqual(s2.id, 47)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)

    def test_str(self):
        """Tests that str() prints a nice version of the square"""
        s1 = Square(4, 2, 3, 47)
        self.assertEqual(str(s1), "[Square] (47) 2/3 - 4")

    def test_size(self):
        """Tests that the size of a square can be gotten and set"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

        s1.size = 9
        self.assertEqual(s1.size, 9)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.size = "foo"

    def test_update(self):
        """Tests the update method of square"""
        s1 = Square(2)

        s1.update(10)
        self.assertEqual(s1.id, 10)

        s1.update(10, 4)
        self.assertEqual(s1.size, 4)
        self.assertEqual(s1.width, 4)
        self.assertEqual(s1.height, 4)

        s1.update(10, 4, 9)
        self.assertEqual(s1.x, 9)

        s1.update(10, 4, 9, 7)
        self.assertEqual(s1.y, 7)

    def test_update_kwargs(self):
        """Tests the update method with kwargs"""
        s1 = Square(2)

        s1.update(size=4)
        self.assertEqual(s1.size, 4)
        self.assertEqual(s1.width, 4)
        self.assertEqual(s1.height, 4)

        s1.update(id=31)
        self.assertEqual(s1.id, 31)

        s1.update(x=29)
        self.assertEqual(s1.x, 29)

        s1.update(y=47)
        self.assertEqual(s1.y, 47)

        s1.update(x=21, size=5, y=99, id=23)
        self.assertEqual(s1.x, 21)
        self.assertEqual(s1.y, 99)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.id, 23)

    def test_dict(self):
        """Tests the dictionary representation of a square"""
        s1 = Square(4)
        s1_dict = s1.to_dictionary()
        s1_correct = {"id":1, "size":4, "x":0, "y":0}
        self.assertEqual(s1_dict, s1_correct)

        s2 = Square(9)
        s2_new = {"id":9, "size":4, "x":3, "y":4}
        s2.update(**s2_new)
        self.assertEqual(s2.to_dictionary(), s2_new)
