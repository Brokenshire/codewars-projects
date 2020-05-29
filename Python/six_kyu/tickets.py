# Python solution for 'Vasya - Clerk' codewars question.
# Level: 6 kyu
# Tags: FUNDAMENTALS, MATHEMATICS, ALGORITHMS, NUMBERS, and GAMES.
# Author: Jack Brokenshire
# Date: 29/05/2020

import unittest


def tickets(people):
    """
    Determines whether Vasya can sell a ticket to all people in the queue.
    :param people: an array integers ranging from numbers 25, 50, and 100.
    :return: YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that
             moment. Otherwise return NO.
    """
    a,b = 0, 0
    for x in range(len(people)):
        if people[x] == 25:
            a += 1
        elif people[x] == 50 and a > 0:
            a -= 1
            b += 1
        elif people[x] == 100 and a > 0 and b > 0:
            a -= 1
            b -= 1
        elif people[x] == 100 and a > 2:
            a -= 3
        else:
            return "NO"
    return "YES"


class TestTickets(unittest.TestCase):
    """Class to test 'tickets' function"""

    def test_tickets(self):
        self.assertEquals(tickets([25, 25, 50]), "YES")
        self.assertEquals(tickets([25, 100]), "NO")


if __name__ == '__main__':
    unittest.main()
