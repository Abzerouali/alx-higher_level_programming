#!/usr/bin/python3
"""Unit tests for the Base class"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test class for the Base class"""

    def setUp(self):
        """Setup for the tests"""
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()
        self.b4 = Base(12)
        self.b5 = Base()
        self.r1 = Rectangle(10, 7, 2, 8, 1)
        self.s1 = Square(10, 7, 2, 8)
        self.dic1 = self.r1.to_dictionary()
        self.dic2 = self.s1.to_dictionary()
        self.dic3 = {}

    def test_id(self):
        """Test JSON string conversion and parsing"""
        self.assertEqual(self.b1.id, 7)
        self.assertEqual(self.b2.id, 8)
        self.assertEqual(self.b3.id, 9)
        self.assertEqual(self.b4.id, 12)
        self.assertEqual(self.b5.id, 10)

    def test_json_str_dic(self):
        """ testing the json string and..."""
        self.assertEqual([self.dic1], Rectangle.from_json_string(
            Rectangle.to_json_string([self.dic1])))
        self.assertEqual([self.dic2], Square.from_json_string(
            Square.to_json_string([self.dic2])))
        self.assertEqual([self.dic3], Base.from_json_string(
            Base.to_json_string([self.dic3])))
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string(None), '[]')
        self.assertEqual(Base.to_json_string(3), '3')

    def test_create(self):
        """ testing create function """
        self.assertEqual(str(Rectangle.create(**self.dic1)), str(self.r1))
        self.assertEqual(str(Square.create(**self.dic2)), str(self.s1))
