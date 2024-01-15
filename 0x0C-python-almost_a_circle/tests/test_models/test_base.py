#!/usr/bin/python3
"""Unittest for the base class
"""
import unittest
from models.base import Base


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


if __name__ == '__main__':
    unittest.main()
