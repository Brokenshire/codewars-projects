# Python solution for 'Sum of a sequence' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS, NUMBERS, RECURSION, ALGORITHMS, COMPUTABILITY THEORY, THEORETICAL COMPUTER SCIENCE, LOOPS,
#       CONTROL FLOW, and BASIC LANGUAGE FEATURES.
# Author: Jack Brokenshire
# Date: 14/04/2020

import unittest


def sequence_sum(begin_number, end_number, step):
    """
    Goes through a loop and finds the sum of the sequence specified by three integer inputs.
    :param begin_number: the starting integer value.
    :param end_number: the ending integer value.
    :param step: integer of how many numbers to increase each step.
    :return: the sum of a sequence of integers.
    """
    return sum(x for x in range(begin_number, end_number+1, step))


class TestSequenceSum(unittest.TestCase):
    """Class to test 'sequence_sum' function"""

    def test_sequence_sum(self):
        self.assertEqual(sequence_sum(2, 6, 2), 12)
        self.assertEqual(sequence_sum(1, 5, 1), 15)
        self.assertEqual(sequence_sum(1, 5, 3), 5)
        self.assertEqual(sequence_sum(0, 15, 3), 45)
        self.assertEqual(sequence_sum(16, 15, 3), 0)
        self.assertEqual(sequence_sum(2, 24, 22), 26)
        self.assertEqual(sequence_sum(2, 2, 2), 2)
        self.assertEqual(sequence_sum(2, 2, 1), 2)
        self.assertEqual(sequence_sum(1, 15, 3), 35)
        self.assertEqual(sequence_sum(15, 1, 3), 0)


if __name__ == '__main__':
    unittest.main()
