import unittest
from collections import Counter
from stats.functions import mean, median, mode, quartile, data_range, box_plot, variance,\
    std, dot, covariance, correlation, make_buckets, hist, plot, pdf, cdf


class Test(unittest.TestCase):
    """
    Class for unittests.
    """

    def test_mean_positive(self):
        """
        Positive unittest for correctness of function.
        Checks if function returns correct result.
        :returns: None; AssertionError -- if test fails
        """
        x = mean([1, 2])
        self.assertEqual(x, 1.5)

    def test_mean_positive_type(self):
        """
        Positive unittest for type correctness of result.
        :returns: None; AssertionError -- if test fails
        """
        x = mean([1, 3])
        self.assertIsInstance(x, float)

    def test_mean_negative_type(self):
        """
        Negative unittest for wrong input.
        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(TypeError) as raised_exception:
            mean('aaa')
        self.assertEqual(raised_exception.exception.args[0],
                         'elements of object should be int or float values')

    def test_mean_negative_elements(self):
        """
        Negative unittest for wrong input.
        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(TypeError) as raised_exception:
            mean(2)
        self.assertEqual(raised_exception.exception.args[0],
                         'object should be iterable with float or int values')

    def test_median_positive(self):
        """
        Positive unittest for correctness of function.
        Checks if function returns correct result.
        :returns: None; AssertionError -- if test fails
        """
        x = median([1, 2, 3])
        self.assertEqual(x, 2)

    def test_median_positive_type(self):
        """
        Positive unittest for type correctness of result.
        :returns: None; AssertionError -- if test fails
        """
        x = median([1, 2, 3])
        self.assertIsInstance(x, float)

    def test_median_negative_type(self):
        """
        Negative unittest for wrong input.
        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(TypeError) as raised_exception:
            median(2)
        self.assertEqual(raised_exception.exception.args[0],
                         'object should be iterable with float or int values')

    def test_median_negative_elements(self):
        """
        Negative unittest for wrong input.
        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(TypeError) as raised_exception:
            median(['aaa', 'bbb'])
        self.assertEqual(raised_exception.exception.args[0],
                         'elements of object should be int or float values')

    def test_mode_positive(self):
        """
        Positive unittest for correctness of function.
        Checks if function returns correct result.
        :returns: None; AssertionError -- if test fails
        """
        x = mode([1, 2, 2, 3])
        self.assertEqual(x, [2])

    def test_mode_positive_type(self):
        """
        Positive unittest for type correctness of result.
        :returns: None; AssertionError -- if test fails
        """
        x = mode([1, 2, 2, 3])
        self.assertIsInstance(x, list)

    def test_mode_negative_type(self):
        """
        Negative unittest for wrong input.
        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(TypeError) as raised_exception:
            mode(2)
        self.assertEqual(raised_exception.exception.args[0],
                         'object should be iterable')

    def test_quartile_positive(self):
        """
        Positive unittest for correctness of function.
        Checks if function returns correct result.
        :returns: None; AssertionError -- if test fails
        """
        x = quartile([1, 2, 2, 3], 0.9)
        self.assertEqual(x, 3)

    def test_quartile_positive_type(self):
        """
        Positive unittest for type correctness of result.
        :returns: None; AssertionError -- if test fails
        """
        x = quartile([1, 2, 2, 3], 0.9)
        self.assertIsInstance(x, int)

    def test_quartile_negative_type(self):
        """
        Negative unittest for wrong input.
        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(TypeError) as raised_exception:
            quartile(2, 0.9)
        self.assertEqual(raised_exception.exception.args[0],
                         'object should be iterable')

    def test_quartile_negative_elements(self):
        """
        Negative unittest for wrong input.
        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(TypeError) as raised_exception:
            quartile(['aaa', 2], 0.9)
        self.assertEqual(raised_exception.exception.args[0],
                         'elements of object should be int or float values')

    def test_quartile_negative_p(self):
        """
        Negative unittest for wrong input.
        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(ValueError) as raised_exception:
            quartile([1, 2], 1.1)
        self.assertEqual(raised_exception.exception.args[0],
                         'quartile value should be between 0 and 1')

    def test_data_range_positive(self):
        """
        Positive unittest for correctness of function.
        Checks if function returns correct result.
        :returns: None; AssertionError -- if test fails
        """
        x = data_range([1, 2, 2, 3])
        self.assertEqual(x, 2)

    def test_data_range_positive_type(self):
        """
        Positive unittest for type correctness of result.
        :returns: None; AssertionError -- if test fails
        """
        x = data_range([1, 2, 2, 3])
        self.assertIsInstance(x, int)

    def test_data_range_negative_type(self):
        """
        Negative unittest for wrong input.
        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(TypeError) as raised_exception:
            data_range(2)
        self.assertEqual(raised_exception.exception.args[0],
                         'object should be iterable')

    def test_data_range_negative_elements(self):
        """
        Negative unittest for wrong input.
        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(TypeError) as raised_exception:
            data_range(['aaa', 2])
        self.assertEqual(raised_exception.exception.args[0],
                         'elements of object should be int or float values')

    def test_box_plot_positive(self):
        """
        Positive unittest for correctness of function.
        Checks if function returns correct result.
        :returns: None; AssertionError -- if test fails
        """
        x = box_plot([1, 2, 2, 3])
        self.assertEqual(x, None)

    def test_box_plot_negative_type(self):
        """
        Negative unittest for wrong input.
        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(TypeError) as raised_exception:
            box_plot(2)
        self.assertEqual(raised_exception.exception.args[0],
                         'object should be iterable')

    def test_box_plot_negative_elements(self):
        """
        Negative unittest for wrong input.
        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(TypeError) as raised_exception:
            box_plot(['aaa', 2])
        self.assertEqual(raised_exception.exception.args[0],
                         'elements of object should be int or float values')

    def test_variance_positive(self):
        """
        Positive unittest for correctness of function.
        Checks if function returns correct result.
        :returns: None; AssertionError -- if test fails
        """
        x = variance([1, 2, 3])
        self.assertEqual(x, 1.0)

    def test_variance_positive_type(self):
        """
        Positive unittest for type correctness of result.
        :returns: None; AssertionError -- if test fails
        """
        x = variance([1, 2, 3])
        self.assertIsInstance(x, float)

    def test_variance_negative_type(self):
        """
        Negative unittest for wrong input.
        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(TypeError) as raised_exception:
            variance(2)
        self.assertEqual(raised_exception.exception.args[0],
                         'object should be iterable')

    def test_variance_negative_elements(self):
        """
        Negative unittest for wrong input.
        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(TypeError) as raised_exception:
            variance(['aaa', 2])
        self.assertEqual(raised_exception.exception.args[0],
                         'elements of object should be int or float values')

    def test_std_positive(self):
        """
        Positive unittest for correctness of function.
        Checks if function returns correct result.
        :returns: None; AssertionError -- if test fails
        """
        x = std([1, 2, 3])
        self.assertEqual(x, 1.0)

    def test_std_positive_type(self):
        """
        Positive unittest for type correctness of result.
        :returns: None; AssertionError -- if test fails
        """
        x = std([1, 2, 3])
        self.assertIsInstance(x, float)

    def test_std_negative_type(self):
        """
        Negative unittest for wrong input.
        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(TypeError) as raised_exception:
            std(2)
        self.assertEqual(raised_exception.exception.args[0],
                         'object should be iterable')

    def test_std_negative_elements(self):
        """
        Negative unittest for wrong input.
        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(TypeError) as raised_exception:
            std(['aaa', 2])
        self.assertEqual(raised_exception.exception.args[0],
                         'elements of object should be int or float values')

    def test_dot_positive(self):
        """
        Positive unittest for correctness of function.
        Checks if function returns correct result.
        :returns: None; AssertionError -- if test fails
        """
        x = dot([1, 2, 3], [1, 2, 3])
        self.assertEqual(x, 14)

    def test_dot_positive_type(self):
        """
        Positive unittest for type correctness of result.
        :returns: None; AssertionError -- if test fails
        """
        x = dot([1, 2, 3], [1, 2, 3])
        self.assertIsInstance(x, int)

    def test_dot_negative_type(self):
        """
        Negative unittest for wrong input.
        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(TypeError) as raised_exception:
            dot(2, 3)
        self.assertEqual(raised_exception.exception.args[0],
                         'object should be iterable')

    def test_dot_negative_elements(self):
        """
        Negative unittest for wrong input.
        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(TypeError) as raised_exception:
            dot(['aaa', 2], [2, 3])
        self.assertEqual(raised_exception.exception.args[0],
                         'elements of object should be int or float values')

    def test_dot_missing_elements(self):
        """
        Negative unittest for wrong input.
        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(TypeError) as raised_exception:
            dot([2, 3])
        self.assertEqual(raised_exception.exception.args[0],
                         "dot() missing 1 required positional argument: 'y'")

    def test_cov_positive(self):
        """
        Positive unittest for correctness of function.
        Checks if function returns correct result.
        :returns: None; AssertionError -- if test fails
        """
        x = covariance([1, 2, 3], [1, 2, 3])
        self.assertEqual(x, 1.0)

    def test_cov_positive_type(self):
        """
        Positive unittest for type correctness of result.
        :returns: None; AssertionError -- if test fails
        """
        x = covariance([1, 2, 3], [1, 2, 3])
        self.assertIsInstance(x, float)

    def test_cov_negative_type(self):
        """
        Negative unittest for wrong input.
        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(TypeError) as raised_exception:
            covariance(2, 3)
        self.assertEqual(raised_exception.exception.args[0],
                         'object should be iterable')

    def test_cov_negative_elements(self):
        """
        Negative unittest for wrong input.
        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(TypeError) as raised_exception:
            covariance(['aaa', 2], [2, 3])
        self.assertEqual(raised_exception.exception.args[0],
                         'elements of object should be int or float values')

    def test_cov_missing_elements(self):
        """
        Negative unittest for wrong input.
        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(TypeError) as raised_exception:
            covariance([2, 3])
        self.assertEqual(raised_exception.exception.args[0],
                         "covariance() missing 1 required positional argument: 'y'")

    def test_corr_positive(self):
        """
        Positive unittest for correctness of function.
        Checks if function returns correct result.
        :returns: None; AssertionError -- if test fails
        """
        x = correlation([1, 2, 3], [1, 2, 3])
        self.assertEqual(x, 1.0)

    def test_corr_positive_zero(self):
        """
        Positive unittest for correctness of function.
        Checks if function returns correct result.
        :returns: None; AssertionError -- if test fails
        """
        x = correlation([1, 1, 1], [1, 1, 1])
        self.assertEqual(x, 0)

    def test_corr_positive_type(self):
        """
        Positive unittest for type correctness of result.
        :returns: None; AssertionError -- if test fails
        """
        x = correlation([1, 2, 3], [1, 2, 3])
        self.assertIsInstance(x, float)

    def test_corr_negative_type(self):
        """
        Negative unittest for wrong input.
        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(TypeError) as raised_exception:
            correlation(2, 3)
        self.assertEqual(raised_exception.exception.args[0],
                         'object should be iterable')

    def test_corr_negative_elements(self):
        """
        Negative unittest for wrong input.
        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(TypeError) as raised_exception:
            correlation(['aaa', 2], [2, 3])
        self.assertEqual(raised_exception.exception.args[0],
                         'elements of object should be int or float values')

    def test_corr_missing_elements(self):
        """
        Negative unittest for wrong input.
        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(TypeError) as raised_exception:
            correlation([2, 3])
        self.assertEqual(raised_exception.exception.args[0],
                         "correlation() missing 1 required positional argument: 'y'")

    def test_buckets_positive(self):
        """
        Positive unittest for correctness of function.
        Checks if function returns correct result.
        :returns: None; AssertionError -- if test fails
        """
        x = make_buckets([1, 2, 3], 3)
        self.assertEqual(x, Counter({0: 2, 3: 1}))

    def test_buckets_negative_type(self):
        """
        Negative unittest for wrong input.
        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(TypeError) as raised_exception:
            make_buckets(2, 3)
        self.assertEqual(raised_exception.exception.args[0],
                         'object should be iterable')

    def test_buckets_negative_elements(self):
        """
        Negative unittest for wrong input.
        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(TypeError) as raised_exception:
            make_buckets(['aaa', 2], 3)
        self.assertEqual(raised_exception.exception.args[0],
                         'elements of object should be int or float values')

    def test_buckets_negative_size(self):
        """
        Negative unittest for wrong input.
        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(ValueError) as raised_exception:
            make_buckets([3, 2], -3)
        self.assertEqual(raised_exception.exception.args[0],
                         'bucket size should be positive int value')

    def test_hist_positive(self):
        """
        Positive unittest for correctness of function.
        Checks if function returns correct result.
        :returns: None; AssertionError -- if test fails
        """
        x = hist([1, 2, 3], 3, title='hist', xlabel='x', ylabel='y')
        self.assertEqual(x, None)

    def test_hist_negative_type(self):
        """
        Negative unittest for wrong input.
        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(TypeError) as raised_exception:
            hist(2, 3)
        self.assertEqual(raised_exception.exception.args[0],
                         'object should be iterable')

    def test_hist_negative_elements(self):
        """
        Negative unittest for wrong input.
        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(TypeError) as raised_exception:
            hist(['aaa', 2], 3)
        self.assertEqual(raised_exception.exception.args[0],
                         'elements of object should be int or float values')

    def test_plot_positive(self):
        """
        Positive unittest for correctness of function.
        Checks if function returns correct result.
        :returns: None; AssertionError -- if test fails
        """
        x = plot([1, 2, 3], [1, 2, 3])
        self.assertEqual(x, None)

    def test_plot_negative_type(self):
        """
        Negative unittest for wrong input.
        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(TypeError) as raised_exception:
            plot(2, 3)
        self.assertEqual(raised_exception.exception.args[0],
                         'object should be iterable')

    def test_plot_negative_elements(self):
        """
        Negative unittest for wrong input.
        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(TypeError) as raised_exception:
            plot(['aaa', 2], [2, 3])
        self.assertEqual(raised_exception.exception.args[0],
                         'elements of object should be int or float values')

    def test_plot_missing_elements(self):
        """
        Negative unittest for wrong input.
        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(TypeError) as raised_exception:
            plot([2, 3])
        self.assertEqual(raised_exception.exception.args[0],
                         "plot() missing 1 required positional argument: 'y'")

    def test_pdf_positive(self):
        """
        Positive unittest for correctness of function.
        Checks if function returns correct result.
        :returns: None; AssertionError -- if test fails
        """
        x = pdf([1, 2, 3, 3, 5, 6])
        self.assertEqual(x, None)

    def test_pdf_negative_type(self):
        """
        Negative unittest for wrong input.
        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(TypeError) as raised_exception:
            pdf(2)
        self.assertEqual(raised_exception.exception.args[0],
                         'object should be iterable')

    def test_pdf_negative_elements(self):
        """
        Negative unittest for wrong input.
        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(TypeError) as raised_exception:
            pdf(['aaa', 2, 3])
        self.assertEqual(raised_exception.exception.args[0],
                         'elements of object should be int or float values')

    def test_cdf_positive(self):
        """
        Positive unittest for correctness of function.
        Checks if function returns correct result.
        :returns: None; AssertionError -- if test fails
        """
        x = cdf([1, 2, 3, 3, 5, 6])
        self.assertEqual(x, None)

    def test_cdf_negative_type(self):
        """
        Negative unittest for wrong input.
        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(TypeError) as raised_exception:
            cdf(2)
        self.assertEqual(raised_exception.exception.args[0],
                         'object should be iterable')

    def test_cdf_negative_elements(self):
        """
        Negative unittest for wrong input.
        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(TypeError) as raised_exception:
            cdf(['aaa', 2, 3])
        self.assertEqual(raised_exception.exception.args[0],
                         'elements of object should be int or float values')


if __name__ == '__main__':
    unittest.main()