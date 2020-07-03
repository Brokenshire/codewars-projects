# Python solution for 'Counting sheep...' codewars question.
# Level: 8 kyu
# Tags: FUNDAMENTALS and ARRAYS.
# Author: Jack Brokenshire
# Date: 03/07/2020

import unittest


def count_sheeps(sheep):
    """
    Consider an array/list of sheep where some sheep may be missing from their place. We need a function that
    counts the number of sheep present in the array (true means present).
    :param sheep: array/list of True or False.
    :return: the number of sheep present in the array.
    """
    return sheep.count(True)


class TestCountSheeps(unittest.TestCase):
    """Class to test 'count_sheeps' function"""

    def test_count_sheeps(self):
        array1 = [True, True, True, False,
                  True, True, True, True,
                  True, False, True, False,
                  True, False, False, True,
                  True, True, True, True,
                  False, False, True, True]

        self.assertEqual(count_sheeps(array1), 17, "There are 17 sheeps in total, not %s" % count_sheeps(array1))


if __name__ == '__main__':
    unittest.main()
