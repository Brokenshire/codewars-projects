# Python solution for 'Grasshopper - Debug' codewars question.
# Level: 8 kyu
# Tags: BUGS.
# Author: Jack Brokenshire
# Date: 15/07/2020

import unittest


def weather_info(temp):
    c = convert_to_celsius(temp)
    if c < 0:
        return str(c) + " is freezing temperature"
    else:
        return str(c) + " is above freezing temperature"


def convert_to_celsius(temperature):
    celsius = (temperature - 32) * (5 / 9)
    return celsius


class TestWeatherInfo(unittest.TestCase):
    """Class to test 'weather_info' function"""

    def test_weather_info(self):
        self.asserEqual(weather_info(50), '10.0 is above freezing temperature')
        self.asserEqual(weather_info(23),  '-5.0 is freezing temperature')


if __name__ == '__main__':
    unittest.main()
