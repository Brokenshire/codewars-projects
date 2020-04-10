# Python solution for "The Supermarket Queue" codewars question.
# Level: 6 kyu
# Tags: Fundamentals, Arrays, Loops, Control Flow, and Basic Language Features.
# Author: Jack Brokenshire
# Date: 22/03/2020

import unittest


def queue_time(customers, n):
    """
    Calculates the total time required for all the customers to check out!
    :param customers: an array of positive integers representing the queue. Each integer represents a customer,
                      and its value is the amount of time they require to check out.
    :param n: a positive integer, the number of checkout tills.
    :return: an integer, the total time required.
    """
    tills = [0] * n
    for x in customers:
        tills[0] += x
        tills.sort()
    return max(tills)


class TestQueueTime(unittest.TestCase):
    """Class to test "queue_time" function"""

    def test_queue_time(self):
        self.assertEqual(queue_time([], 1), 0)
        self.assertEqual(queue_time([5], 1), 5)
        self.assertEqual(queue_time([2], 5), 2)
        self.assertEqual(queue_time([1, 2, 3, 4, 5], 1), 15)
        self.assertEqual(queue_time([1, 2, 3, 4, 5], 100), 5)
        self.assertEqual(queue_time([2, 2, 3, 3, 4, 4], 2), 9)


if __name__ == "__main__":
    unittest.main()
