# Python solution for 'Fizz Buzz' codewars question.
# Level: 7 kyu
# Tags: ALGORITHMS, FUNDAMENTALS, NUMBERS, AND ARRAYS.
# Author: Jack Brokenshire
# Date: 13/08/2020

import unittest


def fizzbuzz(n):
    """
    Return an array containing the numbers from 1 to N, where N is the parametered value. N will never be less than 1.
    :param n: an integer value.
    :return: an array with integers and FizzBuzz.
    """
    final = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            final.append("FizzBuzz")
        elif i % 3 == 0:
            final.append("Fizz")
        elif i % 5 == 0:
            final.append("Buzz")
        else:
            final.append(i)
    return final


class TestFizzbuzz(unittest.TestCase):
    """Class to test 'fizzbuzz' function"""

    def test_fizzbuzz(self):
        expected = [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz']
        self.assertEqual(fizzbuzz(10), expected)


if __name__ == "__main__":
    unittest.main()
