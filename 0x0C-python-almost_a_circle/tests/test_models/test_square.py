#!/usr/bin/python3
"""Unittest for the Square class class
"""
import unittest
from models.square import Square
from models.base import Base
from io import StringIO
from unittest.mock import patch


class TestSquare(unittest.TestCase):
    """Tests the Square class"""

    def test_rectangle_is_base(self):
        self.assertIsInstance(Square(10, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Square()

    def test_two_args(self):
        s1 = Square(10, 2)
        s2 = Square(2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        s1 = Square(2, 2, 4)
        s2 = Square(4, 4, 2)
        self.assertEqual(s1.id, s2.id - 1)

    def test_five_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_size_private(self):
        with self.assertRaises(AttributeError):
            print(Square(5, 5, 0, 0).__size)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Square(5, 5, 0, 0).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Square(5, 5, 0, 0).__y)

    def test_size_getter(self):
        r = Square(5, 7, 7, 5)
        self.assertEqual(5, r.size)

    def test_size_setter(self):
        r = Square(5, 7, 7, 5)
        r.size = 10
        self.assertEqual(10, r.size)

    def test_x_getter(self):
        r = Square(5, 7, 7, 5)
        self.assertEqual(7, r.x)

    def test_x_setter(self):
        r = Square(5, 7, 7, 5)
        r.x = 10
        self.assertEqual(10, r.x)

    def test_y_getter(self):
        r = Square(5, 7, 7, 5)
        self.assertEqual(7, r.y)

    def test_y_setter(self):
        r = Square(5, 7, 7, 5)
        r.y = 10
        self.assertEqual(10, r.y)

    def test_size(self):
        """Tests the validation of size"""
        s1 = Square(10, 2)
        s1.size = 7
        self.assertEqual(s1.size, 7)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.size = []
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.size = 2.5
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1.size = -1
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1.size = 0

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid", 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"a": 1, "b": 2}, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 3), 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(frozenset({1, 2, 3, 1}), 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3}, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3], 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(5), 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(b'Python', 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(bytearray(b'abcdefg'), 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(memoryview(b'abcedfg'), 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(5), 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(5.5, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None, 3)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-2, 3)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'), 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'), 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", 2, 3, "invalid y")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", 2, "invalid x")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", "invalid height")

    def test_x(self):
        """Tests the validation of x"""
        s3 = Square(7, 8, 3, 5)
        s3.x = 10
        self.assertEqual(s3.x, 10)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s3.x = []
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s3.x = 2.5
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s3.x = -1

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, "1", 2)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(3, -2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, complex(5))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, True, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, [1, 2, 3], 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, memoryview(b'abcedfg'))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, bytearray(b'abcdefg'))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, (1, 2, 3), 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('inf'), 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('nan'), 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, range(5))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, [1, 2, 3], 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 5.5, 9)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid x", "invalid y")

    def test_y(self):
        """Tests the validation of y"""
        s3 = Square(7, 8, 3, 5)
        s3.y = 10
        self.assertEqual(s3.y, 10)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s3.y = []
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s3.y = 2.5
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s3.y = -1

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 5, "2")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 10, -2)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, float('inf'))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, float('nan'))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, None)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, {"a": 1, "b": 2})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2,  {1, 2, 3})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, frozenset({1, 2, 3, 1}))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, 5.5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, complex(5))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, (1, 2, 3))

    def test_area(self):
        """Tests the area() function"""
        s1 = Square(10)
        s2 = Square(2)
        s3 = Square(7, 8, 3, 5)
        self.assertEqual(s1.area(), 100)
        self.assertEqual(s2.area(), 4)
        self.assertEqual(s3.area(), 49)

        with self.assertRaises(TypeError):
            s3.area(12)

    def test_display(self):
        """Tests the display() function"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            s1 = Square(3)
            s1.display()
            printed_output = mock_stdout.getvalue().strip()

        expected_output = "###\n###\n###"
        self.assertEqual(printed_output, expected_output)

    def test_display_x_y(self):
        s1 = Square(2, 2, 2)
        held_output = StringIO()
        with patch('sys.stdout', held_output):
            s1.display()
            printed_output = held_output.getvalue()

        expected_output = "\n\n  ##\n  ##\n"
        self.assertEqual(printed_output, expected_output)

    def test_display_x_y_2(self):
        s1 = Square(4, 3, 2)
        held_output = StringIO()
        with patch('sys.stdout', held_output):
            s1.display()
            printed_output = held_output.getvalue()

        expected_output = "\n\n   ####\n   ####\n   ####\n   ####\n"
        self.assertEqual(printed_output, expected_output)

    def test_display_args(self):
        with self.assertRaises(TypeError):
            s1 = Square(3, 2, 2)
            s1.display(10)

    def test_str(self):
        s1 = Square(4, 2, 1, 12)
        self.assertEqual(s1.__str__(),
                         "[Square] ({}) 2/1 - 4".format(s1.id))

        s2 = Square(5, 1)
        self.assertEqual(s2.__str__(),
                         "[Square] ({}) 1/0 - 5".format(s2.id))

        s3 = Square(5, 0, 1)
        self.assertEqual(s3.__str__(),
                         "[Square] ({}) 0/1 - 5".format(s3.id))

    def test_update_args_zero(self):
        r = Square(10, 10, 10, 10)
        r.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(r))

    def test_update_args_one(self):
        r = Square(10, 10, 10, 10)
        r.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(r))

    def test_update_args_two(self):
        r = Square(10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual("[Square] (89) 10/10 - 2", str(r))

    def test_update_args_three(self):
        r = Square(10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual("[Square] (89) 3/10 - 2", str(r))

    def test_update_args_four(self):
        r = Square(10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 3/4 - 2", str(r))

    def test_update_args_more_than_five(self):
        r = Square(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        self.assertEqual("[Square] (89) 3/4 - 2", str(r))

    def test_update_args_None_id(self):
        r = Square(10, 10, 10, 10)
        r.update(None)
        correct = "[Square] ({}) 10/10 - 10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_None_id_and_more(self):
        r = Square(10, 10, 10, 10)
        r.update(None, 4, 5, 2)
        correct = "[Square] ({}) 5/2 - 4".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_twice(self):
        r = Square(10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        r.update(6, 5, 4, 3)
        self.assertEqual("[Square] (6) 4/3 - 5", str(r))

    def test_update_args_invalid_size_type(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid")

    def test_update_args_size_zero(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, 0)

    def test_update_args_size_negative(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, -5)

    def test_update_args_invalid_x_type(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 2, "invalid")

    def test_update_args_x_negative(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(89, 1, -6)

    def test_update_args_invalid_y(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(89, 2, 4, "invalid")

    def test_update_args_y_negative(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(89, 1, 2, -6)

    def test_update_args_size_before_x(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", "invalid")

    def test_update_args_size_before_y(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", 2, "invalid")

    def test_update_args_x_before_y(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 1, "invalid", "invalid")

    def test_update_kwargs_one(self):
        r = Square(10, 10, 10, 10)
        r.update(id=1)
        self.assertEqual("[Square] (1) 10/10 - 10", str(r))

    def test_update_kwargs_two(self):
        r = Square(10, 10, 10, 10)
        r.update(size=2, id=1)
        self.assertEqual("[Square] (1) 10/10 - 2", str(r))

    def test_update_kwargs_three(self):
        r = Square(10, 10, 10, 10)
        r.update(id=89, x=1, size=4)
        self.assertEqual("[Square] (89) 1/10 - 4", str(r))

    def test_update_kwargs_four(self):
        r = Square(10, 10, 10, 10)
        r.update(y=5, x=8, id=99, size=1)
        self.assertEqual("[Square] (99) 8/5 - 1", str(r))

    def test_update_kwargs_None_id(self):
        r = Square(10, 10, 10, 10)
        r.update(id=None)
        correct = "[Square] ({}) 10/10 - 10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_None_id_and_more(self):
        r = Square(10, 10, 10, 10)
        r.update(id=None, size=7, y=9)
        correct = "[Square] ({}) 10/9 - 7".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_twice(self):
        r = Square(10, 10, 10, 10)
        r.update(id=89, x=1, size=2)
        r.update(y=3)
        self.assertEqual("[Square] (89) 1/3 - 2", str(r))

    def test_update_kwargs_invalid_size_type(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(size="invalid")

    def test_update_kwargs_size_zero(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(size=0)

    def test_update_kwargs_size_negative(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(size=-5)

    def test_update_kwargs_inavlid_x_type(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-5)

    def test_update_kwargs_invalid_y_type(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-5)

    def test_update_args_and_kwargs(self):
        r = Square(10, 10, 10, 10)
        r.update(89, 2, y=6)
        self.assertEqual("[Square] (89) 10/10 - 2", str(r))

    def test_update_kwargs_wrong_keys(self):
        r = Square(10, 10, 10, 10)
        r.update(a=5, b=10)
        self.assertEqual("[Square] (10) 10/10 - 10", str(r))

    def test_update_kwargs_some_wrong_keys(self):
        r = Square(10, 10, 10, 10)
        r.update(id=89, a=1, b=54, x=19, y=7)
        self.assertEqual("[Square] (89) 19/7 - 10", str(r))

    def test_to_dictionary_output(self):
        s = Square(10, 2, 1, 1)
        correct = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(correct, s.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)

    def test_to_dictionary_arg(self):
        s = Square(10, 2, 4, 1)
        with self.assertRaises(TypeError):
            s.to_dictionary(1)


if __name__ == '__main__':
    unittest.main()
