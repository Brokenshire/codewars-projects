# Python solution for 'Data Reverse' codewars question.
# Level: 6 kyu
# Tags: FUNDAMENTALS and ARRAYS.
# Author: Jack Brokenshire
# Date: 23/06/2020

import unittest


def data_reverse(data):
    """
    Each segment is 8 bits long, meaning the order of these segments needs to be reversed.
    :param data: an array of ones and zeros.
    :return: the reversed of the 8 bit sequences inside the array.
    """
    final = []
    while data:
        for i in data[-8:]:
            final.append(i)
        data = data[:-8]
    return final


class TestDataReverse(unittest.TestCase):
    """Class to test 'data_reverse' function"""

    def test_data_reverse(self):
        data1 = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0]
        data2 = [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]

        self.assertEqual(data_reverse(data1), data2)

        data3 = [0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1]
        data4 = [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0]
        self.assertEqual(data_reverse(data3), data4)


if __name__ == '__main__':
    unittest.main()
