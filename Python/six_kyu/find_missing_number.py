# Python solution for 'Number Zoo Patrol' codewars question.
# Level: 6 kyu
# Tags: ALGORITHMS, PERFORMANCE, MATHEMATICS, and NUMBERS.
# Author: Jack Brokenshire
# Date: 09/05/2020

import unittest


def find_missing_number(numbers):
    """
    akes a shuffled list of unique numbers from 1 to n with one element missing (which can be any number including n).
    :param numbers: array of intergers.
    :return: this missing number.
    """
    total = 1
    for i in range(2, len(numbers) + 2):
        total += i
        total -= numbers[i - 2]
    return total


class TestFindMissingNumber(unittest.TestCase):
    """Class to test 'find_missing_number' function"""

    def test_find_missing_number(self):
        self.assertEqual(find_missing_number([2, 3, 4]), 1)
        self.assertEqual(find_missing_number([1, 3, 4]), 2)
        self.assertEqual(find_missing_number([1, 2, 4]), 3)
        self.assertEqual(find_missing_number([1, 2, 3]), 4)


if __name__ == '__main__':
    unittest.main()
