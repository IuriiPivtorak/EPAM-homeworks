from supertool.weather import weather, weather_forecast, nominatim_weather
import unittest


class Test(unittest.TestCase):
    """
    Class for unittests.
    """

    def test_weather_positive(self):
        """
        Positive unittest for correctness of function.
        Checks if function returns correct result.

        :returns: None; AssertionError -- if test fails
        """
        x = weather('Moscow', 'b4a9d8e16b916107e741f1e84440c660')
        self.assertEqual(x, None)

    def test_weather_negative_city(self):
        """
        Negative unittest for situation when inputted city does not exist.

        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(NameError) as raised_exception:
            weather('Antverp', 'b4a9d8e16b916107e741f1e84440c660')
        self.assertEqual(raised_exception.exception.args[0],
                         'Input location name correctly!')

    def test_weather_negative_token(self):
        """
        Negative unittest for situation when inputted token id
        is not valid.

        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(NameError) as raised_exception:
            weather('Moscow', 'b4a9wdaa')
        self.assertEqual(raised_exception.exception.args[0],
                         'You have inputted invalid token id!')

    def test_weather_forecast_positive(self):
        """
        Positive unittest for correctness of function.
        Checks if function returns correct result.

        :returns: None; AssertionError -- if test fails
        """
        x = weather_forecast('Moscow', 'b4a9d8e16b916107e741f1e84440c660')
        self.assertEqual(x, None)

    def test_weather_forecast_negative_city(self):
        """
        Negative unittest for situation when inputted city does not exist.

        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(NameError) as raised_exception:
            weather_forecast('Antverp', 'b4a9d8e16b916107e741f1e84440c660')
        self.assertEqual(raised_exception.exception.args[0],
                         'Input location name correctly!')

    def test_weather_forecast_negative_token(self):
        """
        Negative unittest for situation when inputted token id
        is not valid.

        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(NameError) as raised_exception:
            weather_forecast('Moscow', 'b4a9wdaa')
        self.assertEqual(raised_exception.exception.args[0],
                         'You have inputted invalid token id!')

    def test_nominatim_positive(self):
        """
        Positive unittest for correctness of function.
        Checks if function returns correct result.

        :returns: None; AssertionError -- if test fails
        """
        x = nominatim_weather('Moscow', 'b4a9d8e16b916107e741f1e84440c660')
        self.assertEqual(x, None)

    def test_nominatim_negative_location(self):
        """
        Negative unittest for situation when inputted location does not exist.

        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(NameError) as raised_exception:
            nominatim_weather('Antverp', 'b4a9d8e16b916107e741f1e84440c660')
        self.assertEqual(raised_exception.exception.args[0],
                         'no such location found!')

    def test_nominatim_negative_token(self):
        """
        Negative unittest for situation when inputted token id
        is not valid.

        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(NameError) as raised_exception:
            nominatim_weather('Moscow', 'b4a9wdaa')
        self.assertEqual(raised_exception.exception.args[0],
                         'You have inputted invalid token id!')

    def test_nominatim_negative_type(self):
        """
        Negative unittest for situation when inputted location is
        of not str type.

        :returns: None; AssertionError -- if test fails
        """
        with self.assertRaises(TypeError) as raised_exception:
            nominatim_weather(1, 'b4a9d8e16b916107e741f1e84440c660')
        self.assertEqual(raised_exception.exception.args[0],
                         '"location" should be of type str')


if __name__ == '__main__':
    unittest.main()