# Python solution for 'Total amount of points' codewars question.
# Level: 8 kyu
# Tags: FUNDAMENTALS, ALGORITHMS, MATHEMATICS, and NUMBERS.
# Author: Jack Brokenshire
# Date: 05/05/2020

import unittest


def points(games):
    """
    Our football team finished the championship. The result of each match look like "x:y". Results of all matches are
    recorded in the collection. Write a function that takes such collection and counts the points of our team in the
    championship. Rules for counting points for each match: if x>y - 3 points, if x<y - 0 point, and if x=y - 1 point
    :param games: a list of strings containing the scores.
    :return: the total amount of points our football team earned.
    """
    score = 0
    for x in games:
        if x[0] > x[2]:
            score += 3
        elif x[0] == x[2]:
            score += 1
    return score


class TestPoints(unittest.TestCase):
    """Class to test 'points' function"""

    def test_points(self):
        self.assertEqual(points(['1:0', '2:0', '3:0', '4:0', '2:1', '3:1', '4:1', '3:2', '4:2', '4:3']), 30)
        self.assertEqual(points(['1:1', '2:2', '3:3', '4:4', '2:2', '3:3', '4:4', '3:3', '4:4', '4:4']), 10)
        self.assertEqual(points(['0:1', '0:2', '0:3', '0:4', '1:2', '1:3', '1:4', '2:3', '2:4', '3:4']), 0)
        self.assertEqual(points(['1:0', '2:0', '3:0', '4:0', '2:1', '1:3', '1:4', '2:3', '2:4', '3:4']), 15)
        self.assertEqual(points(['1:0', '2:0', '3:0', '4:4', '2:2', '3:3', '1:4', '2:3', '2:4', '3:4']), 12)


if __name__ == '__main__':
    unittest.main()
