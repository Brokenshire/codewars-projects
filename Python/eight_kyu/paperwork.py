# Python solution for 'Beginner Series #1 School Paperwork' codewars question.
# Level: 8 kyu
# Tags: FUNDAMENTALS.
# Author: Jack Brokenshire
# Date: 06/08/2020

import unittest


def paperwork(n, m):
    """
    Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork
    has 'm' pages.
    :param n: integer value.
    :param m: integer value.
    :return: calculate how many blank pages do you need.
    """
    return 0 if n < 0 or m < 0 else m * n


class TestPaperwork(unittest.TestCase):
    """Class to test 'paperwork' function"""

    def test_paperwork(self):
        self.assertEqual(paperwork(5, 5), 25, "Failed at Paperwork(5,5)")


if __name__ == "__main__":
    unittest.main()
