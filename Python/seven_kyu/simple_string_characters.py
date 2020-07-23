# Python solution for 'Simple string characters' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS
# Author: Jack Brokenshire
# Date: 23/07/2020

import unittest


def solve(s):
    """
    Count all the uppercase letters, lowercase, numbers and special characters in a string.
    :param s: a string input.
    :return: a list of ints detailing the count of uppercase letters, lowercase, numbers and special characters,
             as follows.
    """
    lower = upper = num = char = 0
    for i in s:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i.isdigit():
            num += 1
        else:
            char += 1
    return [upper, lower, num, char]


class TestSolve(unittest.TestCase):
    """Class to test 'solve' function"""

    def test_solve(self):
        self.assertEqual(solve("Codewars@codewars123.com"), [1, 18, 3, 2])
        self.assertEqual(solve("bgA5<1d-tOwUZTS8yQ"), [7, 6, 3, 2])
        self.assertEqual(solve("P*K4%>mQUDaG$h=cx2?.Czt7!Zn16p@5H"), [9, 9, 6, 9])
        self.assertEqual(solve("RYT'>s&gO-.CM9AKeH?,5317tWGpS<*x2ukXZD"), [15, 8, 6, 9])
        self.assertEqual(solve("$Cnl)Sr<7bBW-&qLHI!mY41ODe"), [10, 7, 3, 6])
        self.assertEqual(solve("@mw>0=QD-iAx!rp9TaG?o&M%l$34L.nbft"), [7, 13, 4, 10])


if __name__ == '__main__':
    unittest.main()
