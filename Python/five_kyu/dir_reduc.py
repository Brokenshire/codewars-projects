# Python solution for 'Directions Reduction' codewars question.
# Level: 5 kyu
# Tags: Fundamentals.
# Author: Jack Brokenshire
# Date: 15/03/2020

import unittest


def dir_reduc(arr):
    """
    Finds the direction to travel removing needless moves.
    :param arr: array of strings.
    :return: an array of strings with the needless directions removed.
    """
    directions = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    result = []
    for x in arr:
        if result and directions[x] == result[-1]:
            result.pop()
        else:
            result.append(x)
    return result


class TestFormatDuration(unittest.TestCase):
    """Class to test 'format_duration' function"""

    def test_format_duration(self):
        self.assertEqual(dir_reduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]), ['WEST'])
        self.assertEqual(dir_reduc(["NORTH", "WEST", "SOUTH", "EAST"]), ["NORTH", "WEST", "SOUTH", "EAST"])


if __name__ == '__main__':
    unittest.main()
