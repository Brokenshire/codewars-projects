# Python solution for 'Square Every Digit' codewars question.
# Level: 7 kyu
# Tags: Fundamentals, Mathematics, Algorithms, and Numbers
# Author: Jack Brokenshire
# Date: 11/02/2020

import unittest


def square_digits(num):
    """
    Welcome. In this kata, you are asked to square every digit of a number.
    For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
    Note: The function accepts an integer and returns an integer
    :param num: input integer value.
    :return: integer of all digits within the input number squared.
    """
    return int("".join(map(str, [x ** 2 for x in list(map(int, str(num)))])))


class TestSquareDigits(unittest.TestCase):
    """Class to test 'square_digits' function"""

    def test_square_digits(self):
        self.assertEqual(square_digits(9119), 811181)


if __name__ == '__main__':
    unittest.main()
