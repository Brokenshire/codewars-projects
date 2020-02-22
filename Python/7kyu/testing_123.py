# Python solution for 'Testing 1-2-3' codewars question.
# Level: 7 kyu
# Tags: Fundamentals, Arrays, Iterators, Control Flow, Object-Oriented Programming, and Basic Language Features.
# Author: Jack Brokenshire
# Date: 22/02/2020

import unittest


def testing_123(lines):
    return ["{}: {}".format(i + 1, j) for i, j in enumerate(lines)]


class TestTesting123(unittest.TestCase):
    """Class to test 'testing_123' function"""

    def test_testing_123(self):
        self.assertEqual(testing_123([]), [])
        self.assertEqual(testing_123(["a", "b", "c"]), ["1: a", "2: b", "3: c"])


if __name__ == '__main__':
    unittest.main()
