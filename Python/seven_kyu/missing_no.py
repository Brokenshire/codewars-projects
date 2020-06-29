# Python solution for 'Find the Missing Number' codewars question.
# Level: 7 kyu
# Tags: ALGORITHMS.
# Author: Jack Brokenshire
# Date: 29/06/2020

import unittest


def missing_no(nums):
    """
    Finds one removed element in an array of integers from 0 to 100.
    :param nums: unsorted array containing all the integers from 0 to 100 inclusively.
    :return: the missing integer within the array.
    """
    return list(set(range(0, len(nums) + 1)).difference(nums))[0]


class TestMissingNo(unittest.TestCase):
    """Class to test 'missing_no' function"""

    def test_missing_no(self):
        nums = list(range(0, 101))
        nums.remove(5)
        self.assertEqual(missing_no(nums), 5)

        nums = list(range(0, 101))
        nums.remove(10)
        self.assertEqual(missing_no(nums), 10)


if __name__ == '__main__':
    unittest.main()
