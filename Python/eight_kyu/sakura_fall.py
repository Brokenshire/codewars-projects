# Python solution for 'The falling speed of petals' codewars question.
# Level: 8 kyu
# Tags: ALGORITHMS
# Author: Jack Brokenshire
# Date: 24/07/2020

import unittest


def sakura_fall(v):
    """
    Suppose that the falling speed of a petal is 5 centimeters per second (5 cm/s), and it takes 80 seconds for the
    petal to reach the ground from a certain branch.
    :param v: integer value of speed in centimeters per second.
    :return: the time it takes for that petal to reach the ground from the same branch.
    """
    if v < 1:
        return 0
    else:
        return 80 / (v / 5)


class TestSakuraFall(unittest.TestCase):
    """Class to test 'sakura_fall' function"""

    def test_sakura_fall(self):
        self.assertEqual(sakura_fall(5), 80)
        self.assertEqual(sakura_fall(10), 40)
        self.assertEqual(sakura_fall(-1), 0)


if __name__ == '__main__':
    unittest.main()
