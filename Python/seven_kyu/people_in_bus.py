# Python solution for "Number of People in the Bus" codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS.
# Author: Jack Brokenshire
# Date: 03/04/2020

import unittest


def people_in_bus(bus_stops):
    """
    Given a list of lists we find the amount of people on the bus.
    :param bus_stops: A list (or array) of integer arrays (or tuples). Each integer array has two items which represent
    number of people get into bus (The first item) and number of people get off the bus (The second item) in a bus stop.
    :return: Number of people who are still in the bus after the last bus station (after the last array).
    """
    return sum(x[0] - x[1] for x in bus_stops)


class TestPeopleInBus(unittest.TestCase):
    """Class to test "people_in_bus" function"""

    def test_people_in_bus(self):
        self.assertEqual(people_in_bus([[10, 0], [3, 5], [5, 8]]), 5)
        self.assertEqual(people_in_bus([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]]), 17)
        self.assertEqual(people_in_bus([[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]]), 21)


if __name__ == "__main__":
    unittest.main()
