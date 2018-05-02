from abc_copy import comparison
import unittest


class Test(unittest.TestCase):
    """
    Class for unittests.
    """

    def test_comparison_positive(self):
        """
        Positive unittest for correctness of function.
        Checks if function returns correct result.

        :returns: None; AssertionError -- if test fails
        """
        x = comparison('aaa.txt', 'bbb.txt', 'ccc.txt')
        self.assertEqual(x, [[2, ['aaa.txt', 'bbb.txt']], [1, ['ccc.txt']]])

    def test_comparison_type(self):
        """
        Positive unittest for correctness of type of result.
        Result should be of type ""list".

        :returns: None; AssertionError -- if test fails
        """
        x = comparison('aaa.txt', 'bbb.txt', 'ccc.txt')
        self.assertIsInstance(x, list)

    def test_comparison_no_file(self):
        """
        Negative unittest for situation when inputted file does not exist.

        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(FileNotFoundError) as raised_exception:
            comparison('aaa.txt', 'bbb.txt', 'ddd.txt')
        self.assertEqual(raised_exception.exception.args[0],
                         'File does not exist!')


if __name__ == '__main__':
    unittest.main()
