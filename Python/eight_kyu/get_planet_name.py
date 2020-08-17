# Python solution for 'Get Planet Name By ID' codewars question.
# Level: 8 kyu
# Tags: BUGS, CONTROL FLOW, BASIC LANGUAGE FEATURES, AND FUNDAMENTALS.
# Author: Jack Brokenshire
# Date: 17/08/2020

import unittest


def get_planet_name(id):
    """
    The function is not returning the correct values. Can you figure out why?
    :param id: an integer value.
    :return: plant string given an id.
    """
    return ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"][id-1]


class TestGetPlanetName(unittest.TestCase):
    """Class to test 'get_planet_name' function"""

    def test_get_planet_name(self):
        self.assertEqual(get_planet_name(2), 'Venus')
        self.assertEqual(get_planet_name(5), 'Jupiter')
        self.assertEqual(get_planet_name(3), 'Earth')
        self.assertEqual(get_planet_name(4), 'Mars')
        self.assertEqual(get_planet_name(8), 'Neptune')
        self.assertEqual(get_planet_name(1), 'Mercury')


if __name__ == "__main__":
    unittest.main()
