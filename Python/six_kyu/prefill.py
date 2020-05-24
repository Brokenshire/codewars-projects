# Python solution for 'Prefill an Array' codewars question.
# Level: 6 kyu
# Tags: FUNDAMENTALS, VALIDATION, ALGORITHMS, BASIC LANGUAGE FEATURES, ARRAYS, CONTROL FLOW, and UTILITIES.
# Author: Jack Brokenshire
# Date: 24/05/2020

import unittest


def prefill(n=0, v=None):
    """
    Either prefills an array with values or throws an TypeError.
    :param n: can be anything.
    :param v: can be anything.
    :return: an array of n elements that all have the same value v.
    """
    try:
        return [v for _ in range(int(n))]
    except:
        raise TypeError(str(n) + " is invalid")


class TestPrefill(unittest.TestCase):
    """Class to test 'prefill' function"""

    def test_prefill(self):
        self.assertEqual(prefill(3,1), [1,1,1])
        self.assertEqual(prefill(2,'abc'), ['abc','abc'])
        self.assertEqual(prefill('1',1), [1])
        self.assertEqual(prefill(3, prefill(2,'2d')), [['2d','2d'],['2d','2d'],['2d','2d']])
        try:
            prefill('xyz', 1)
        except TypeError as err:
            self.assertEqual(str(err), "xyz is invalid")


if __name__ == '__main__':
    unittest.main()
