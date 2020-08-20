# Python solution for 'Grasshopper - If/else syntax debug' codewars question.
# Level: 8 kyu
# Tags: FUNDAMENTALS.
# Author: Jack Brokenshire
# Date: 20/08/2020

import unittest


def check_alive(health):
    """
    Fix the function so if the statement works.
    :param health: an integer value.
    :return: True if health greater than 0, otherwise, False.
    """
    if health <= 0:
        return False
    else:
        return True


class TestCheckAlive(unittest.TestCase):
    """Class to test 'check_alive' function"""

    def test_check_alive(self):
        self.assertEqual(check_alive(-2), False)
        self.assertEqual(check_alive(0), False)
        self.assertEqual(check_alive(1), True)
        self.assertEqual(check_alive(3), True)


if __name__ == "__main__":
    unittest.main()
