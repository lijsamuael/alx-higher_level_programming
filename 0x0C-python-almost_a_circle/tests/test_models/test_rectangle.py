#!/usr/bin/python3
"""Module for testing the Rectangle class"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleClass(unittest.TestCase):
    """Tests the Rectangle class"""

    def setUp(self):
        """Resets the class to prevent interference"""
        Base._Base__nb_objects = 0

    def test_class_setup(self):
        """Tests to make sure Rectangle inherits Base"""
        self.assertTrue(issubclass(Rectangle, Base))
        a = Rectangle(1, 1)
        self.assertTrue(isinstance(a, Base))

    def test_init(self):
        """Tests proper initialization

        TODO: improper number of args
        """
        a = Rectangle(1, 1)
        self.assertEqual(type(a), Rectangle)
        b = Rectangle(1, 1, 3)
        self.assertEqual(type(b), Rectangle)
        c = Rectangle(1, 1, 3, 4)
        self.assertEqual(type(c), Rectangle)
        d = Rectangle(1, 1, 3, 4, 29)
        self.assertEqual(type(d), Rectangle)
        e = Rectangle(width=1, height=1, x=3, y=4, id=29)
        self.assertEqual(type(e), Rectangle)

        with self.assertRaisesRegex(TypeError, "missing 2 required positional arguments"):
            f = Rectangle()
        with self.assertRaisesRegex(TypeError, "missing 1 required positional argument"):
            f = Rectangle(1)

    def test_id(self):
        """Tests that the correct IDs are being assigned"""
        a = Rectangle(1, 1)
        self.assertEqual(a.id, 1)
        b = Rectangle(1, 1, id=47)
        self.assertEqual(b.id, 47)
        c = Rectangle(1, 1)
        self.assertEqual(c.id, 2)

    def test_dimensions(self):
        """Tests that the rectangle's dimensions are handled properly

        This test makes sure that the dimensions are assigned correctly during
        init, but also when changed manually. Also makes sure the other
        dimension is not changed when the other is modified

        """
        a = Rectangle(1, 2)
        self.assertEqual(a.width, 1)
        self.assertEqual(a.height, 2)
        a.width = 4
        self.assertEqual(a.width, 4)
        self.assertEqual(a.height, 2)
        a.height = 5
        self.assertEqual(a.height, 5)
        self.assertEqual(a.width, 4)

    def test_coordinates(self):
        """Tests that the rectangle's coordinates are handled properly

        This test makes sure that the coordinates are assigned correctly
        during init, but also when changed manually. Also makes sure the other
        coordinate is not changed when the other is modified

        """
        a = Rectangle(1, 1)
        self.assertEqual(a.x, 0)
        self.assertEqual(a.y, 0)
        b = Rectangle(1, 1, 2, 3)
        self.assertEqual(b.x, 2)
        self.assertEqual(b.y, 3)
        b.x = 4
        self.assertEqual(b.x, 4)
        self.assertEqual(b.y, 3)
        b.y = 5
        self.assertEqual(b.y, 5)
        self.assertEqual(b.x, 4)

    def test_illegal_dimension_types(self):
        """Tests for correct handling of illegal dimension attributes"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("foo", 1)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 1)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float("inf"), 1)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "foo")

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float("inf"))

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, float("inf"))

    def test_illigal_dimension_values(self):
        """Tests for correct handling of illegal dimension values"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 5)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-9, 5)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(5, 0)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(5, -9)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-9, -10)

    def test_illegal_coordinate_types(self):
        """Tests for correct handling of illegal coordinate types"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, x="foo")

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, x=None)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, x=float("inf"))

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, y="foo")

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, y=None)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, y=float("inf"))

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, x=None, y=float("inf"))

    def test_illegal_coordinate_values(self):
        """Tests for correct handling of illegal coordinate values"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 1, x=-1)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 1, y=-1)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 1, x=-5, y=-1)

    def test_area(self):
        """Tests the area instance method"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_str(self):
        """Tests the builtin str function"""
        r1 = Rectangle(3, 2)
        self.assertEqual(str(r1), "[Rectangle] (1) 0/0 - 3/2")

        r2 = Rectangle(4, 7, 2, 3, 47)
        self.assertEqual(str(r2), "[Rectangle] (47) 2/3 - 4/7")

    def test_update(self):
        """Tests the update method"""
        r1 = Rectangle(3, 2, 9, 5, 21)

        r1.update(4)
        self.assertEqual(r1.id, 4)

        r1.update(4, 1, 6)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 6)

        r1.update(4, 1, 6, 11, 13)
        self.assertEqual(r1.x, 11)
        self.assertEqual(r1.y, 13)

        r1.update(5, 2, 7, 12, 15)
        self.assertEqual(r1.id, 5)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 7)
        self.assertEqual(r1.x, 12)
        self.assertEqual(r1.y, 15)

    def test_update_kwargs(self):
        """Tests the update method with kwargs"""
        r1 = Rectangle(1, 2, 3, 4)

        r1.update(id=9)
        self.assertEqual(r1.id, 9)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

        r1.update(x=7, width=5)
        self.assertEqual(r1.x, 7)
        self.assertEqual(r1.width, 5)

        r1.update(y=11, x=21, width=1, id=100, height=98)
        self.assertEqual(r1.id, 100)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 98)
        self.assertEqual(r1.x, 21)
        self.assertEqual(r1.y, 11)

    def test_dictionary(self):
        """Tests getting dictionary representation"""
        r1 = Rectangle(3, 4)
        r1_dict = r1.to_dictionary()
        r1_correct = {"id":1, "width":3, "height":4, "x":0, "y":0}
        self.assertEqual(r1_dict, r1_correct)

        r2 = Rectangle(9, 2, 1, 3, 47)
        r2.update(**r1.to_dictionary())
        self.assertEqual(r2.to_dictionary(), r1_correct)
