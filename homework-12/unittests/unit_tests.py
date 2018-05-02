from decimal import Decimal
from triangle_area_copy import triangle_area
import unittest
from unittest.mock import patch


class Test(unittest.TestCase):
    """
    Class for unittests.
    """

    def test_triangle_area_calculation(self):
        """
        Positive unittest for correctness of calculations.
        Because of float values, tests if result
        is almost equal to theoretical result.

        :returns: None; AssertionError -- if test fails
        """
        with patch('builtins.input', side_effect=['1 1', '0 0', '3 5']):
            x = triangle_area()
            self.assertAlmostEqual(x, 1)

    def test_triangle_area_format(self):
        """
        Positive unittest for correctness of type of result.
        Result should be of type ""Decimal".

        :returns: None; AssertionError -- if test fails
        """
        with patch('builtins.input', side_effect=['1 1', '0 0', '3 5']):
            x = triangle_area()
            self.assertIsInstance(x, Decimal)

    def test_triangle_area_wrong_input(self):
        """
        Negative unittest that checks for correctness
        of user inputs.
        If user inputs incorrect types, ValueError is called.

        :returns: None; AssertionError -- if test fails
        """
        with patch('builtins.input', side_effect=['a 1', '0 0', '3 3 ']):
            with self.assertRaises(ValueError) as raised_exception:
                triangle_area()
            self.assertEqual(raised_exception.exception.args[0],
                             'Please, use integer or float values only!')

    def test_triangle_area_length(self):
        """
        Negative unittest for wrong number of user inputs.
        If each input is more/less than 2 values, IndexError is called.

        :return: None; AssertionError -- if test fails
        """
        with patch('builtins.input', side_effect=['1 1 1', '0 0', '3 5']):
            with self.assertRaises(IndexError) as raised_exception:
                triangle_area()
            self.assertEqual(raised_exception.exception.args[0],
                             'Please, input exactly 2 coordinates for each point!')

    def test_triangle_area_same_line(self):
        """
        Negative unittest for correctness of user inputs.
        If points lie on the same line (square area = 0) raises ValueError.
        This is tested by "Triangle inequality" theorem: sum of length of any
        2 sides of triangle must be greater than 3rd side.

        :return: None; AssertionError -- if test fails
        """
        with patch('builtins.input', side_effect=['1 1', '0 0', '3 3']):
            with self.assertRaises(ValueError) as raised_exception:
                triangle_area()
            self.assertEqual(raised_exception.exception.args[0],
                             'All points cannot lie on the same line!')

    def test_triangle_area_same_dots(self):
        """
        Negative unittest for correctness of user inputs.
        If each 2 or 3 points are the same, raises ValueError.

        :return: None; AssertionError -- if test fails
        """
        with patch('builtins.input', side_effect=['0 0', '0 0', '1 1']):
            with self.assertRaises(ValueError) as raised_exception:
                triangle_area()
            self.assertEqual(raised_exception.exception.args[0],
                             'Points cannot be the same!')


if __name__ == '__main__':
    unittest.main()
