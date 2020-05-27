# Python solution for 'Grasshopper - Messi Goals' codewars question.
# Level: 8 kyu
# Tags: FUNDAMENTALS, VARIABLES, and BASIC LANGUAGE FEATURES.
# Author: Jack Brokenshire
# Date: 27/05/2020

import unittest


la_liga_goals = 43
champions_league_goals = 10
copa_del_rey_goals = 5

total_goals = la_liga_goals + champions_league_goals + copa_del_rey_goals


class TestFirstNonRepeatingLetter(unittest.TestCase):
    """Class to test 'total_goals' function"""

    def test_total_goals(self):
        self.assertEquals(total_goals, 58, 'total goals should equal to 58')


if __name__ == '__main__':
    unittest.main()
