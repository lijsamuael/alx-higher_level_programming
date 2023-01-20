#!/usr/bin/python3
"""Module for testing the Base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json


class TestBaseClass(unittest.TestCase):
    """Tests the Base class"""

    def setUp(self):
        """Resets the base class to prevent interference"""
        Base._Base__nb_objects = 0

    def test_init(self):
        """Tests proper initialization"""
        a = Base()
        self.assertEqual(type(a), Base)
        b = Base(47)
        self.assertEqual(type(b), Base)

    def test_id(self):
        """Tests that the correct IDs are being assigned"""
        a = Base()
        self.assertEqual(a.id, 1)
        b = Base(47)
        self.assertEqual(b.id, 47)
        c = Base()
        self.assertEqual(c.id, 2)

    def test_to_JSON(self):
        """Tests the dictionary to JSON conversion"""
        s1 = Square(3)
        r1 = Rectangle(4, 5, 1, 2, 47)

        ld = []
        ld.append(s1.to_dictionary())
        ld.append(r1.to_dictionary())
        ld_json = r1.to_json_string(ld)
        expected = [{"id":1, "size":3, "x":0, "y":0},
                    {"id":47, "width":4, "height":5, "x":1, "y":2}]
        expected_json = json.dumps(expected)

        self.assertEqual(ld_json, expected_json)

        self.assertEqual(s1.to_json_string(None), "[]")
        self.assertEqual(s1.to_json_string([]), "[]")

    def test_to_file(self):
        """Tests that the JSON of an object can be written to a file"""
        lo = []
        lo.append(Rectangle(10, 7, 2, 8))
        lo.append(Rectangle(2, 4))

        Base.save_to_file(lo)

        with open("Base.json") as f:
            self.assertEqual(json.loads(f.read()),
                             [x.to_dictionary() for x in lo])

        Rectangle.save_to_file(None)
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")

        Square.save_to_file([])
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_from_json_to_dict(self):
        """Tests the static method converting a json string to a dictionary"""
        s1 = Square(3)
        self.assertEqual([s1.to_dictionary()],
                         s1.from_json_string(
                             s1.to_json_string([s1.to_dictionary()])))

        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_dict_to_instance(self):
        """Tests the class method to convert a dictionary to an instance"""
        s1 = Square(3)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertEqual(str(s1), str(s2))

        self.assertIsNot(s1, s2)
        self.assertNotEqual(s1, s2)

        r1 = Rectangle(3, 4)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(str(r1), str(r2))

        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_from_file(self):
        """Tests that a list of objects can be loaded from a file"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rects = [r1, r2]

        Rectangle.save_to_file(list_rects)

        new_rects = Rectangle.load_from_file()

        self.assertEqual(str(r1), str(new_rects[0]))
        self.assertEqual(str(r2), str(new_rects[1]))

    def test_csv_save(self):
        """Tests that an instance can be saved as CSV"""
        r1 = Rectangle(3, 4, 2, 2, 99)
        r2 = Rectangle(2, 9)
        r_list = [r1, r2]

        Rectangle.save_to_file_csv(r_list)
        new_rects = Rectangle.load_from_file_csv()

        self.assertEqual(str(r1), str(new_rects[0]))
        self.assertEqual(str(r2), str(new_rects[1]))
