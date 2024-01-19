#!/usr/bin/python3
"""Unittest for the base class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase(unittest.TestCase):
    """Tests the Base class"""
    def test_base_init(self):
        """Tests the __init__ method"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(10)
        b5 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 10)
        self.assertEqual(b5.id, 4)
        with self.assertRaises(TypeError):
            Base(11, 12)
        with self.assertRaises(AttributeError):
            print(Base.nb_objects)

    def test_to_json(self):
        self.assertEqual("[]", Base.to_json_string([]))
        self.assertEqual("[]", Base.to_json_string(None))
        with self.assertRaises(TypeError):
            Base.to_json_string()
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)

    def test_to_json_string_rectangle(self):
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)

        self.assertEqual(str, type(Base.to_json_string([r1.to_dictionary()])))
        self.assertTrue(len(Base.to_json_string([r1.to_dictionary()])) == 53)

        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_to_json_string_square(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)

        self.assertEqual(str, type(Base.to_json_string([s1.to_dictionary()])))
        self.assertTrue(len(Base.to_json_string([s1.to_dictionary()])) == 39)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_save_to_file(self):
        s = Square(10, 7, 2, 8)
        Base.save_to_file([s])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)

    def test_save_to_file_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)

        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

    def test_save_to_file_square(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)

        Square.save_to_file([s1])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)

    def test_from_json_string(self):
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

        self.assertEqual([], Base.from_json_string(None))
        self.assertEqual([], Base.from_json_string("[]"))
        with self.assertRaises(TypeError):
            Base.from_json_string()
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)

    def test_from_json_string_rectangle(self):
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_square(self):
        list_input = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_create_rectangle(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)

        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r1))
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r2))
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_create_square(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)

        self.assertEqual("[Square] (7) 5/1 - 3", str(s1))
        self.assertEqual("[Square] (7) 5/1 - 3", str(s2))
        self.assertIsNot(s1, s2)
        self.assertNotEqual(s1, s2)

    def test_load_from_file_empty(self):
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_output, [])

        list_squares_output = Square.load_from_file()
        self.assertEqual(list_squares_output, [])

        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)

    def test_load_from_file_all(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()

        self.assertEqual(str(r1), str(list_rectangles_output[0]))
        self.assertEqual(str(r2), str(list_rectangles_output[1]))


if __name__ == '__main__':
    unittest.main()
