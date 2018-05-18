from supertool.abc import directory_check
import os
import unittest


class Test(unittest.TestCase):
    """
    Class for unittests.
    """

    def test_dir_check_positive(self):
        """
        Positive unittest for correctness of function.
        Checks if function returns correct result.

        :returns: None; AssertionError -- if test fails
        """
        x = directory_check('C:/Users/USER/Desktop/supertool/files')
        self.assertEqual(x, [[2, ['aaa.txt', 'bbb.txt']], [1, ['ccc.txt']]])

    def test_dir_check_positive_type(self):
        """
        Positive unittest for correctness of function.
        Checks if function returns correct result.

        :returns: None; AssertionError -- if test fails
        """
        x = directory_check('C:/Users/USER/Desktop/supertool/files')
        self.assertEqual(x, [[2, ['aaa.txt', 'bbb.txt']], [1, ['ccc.txt']]])

    def test_dir_check_no_file(self):
        """
        Negative unittest for situation when inputted file does not exist.

        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(FileNotFoundError) as raised_exception:
            directory_check('what')
        self.assertEqual(raised_exception.exception.args[0],
                         'No such directory!')


if __name__ == '__main__':
    unittest.main()
