# Python solution for 'Friend or Foe?' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS
# Author: Jack Brokenshire
# Date: 12/04/2020

import unittest


def friend(x):
    """
    If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can
    be sure he's not...
    :param x: an array of strings.
    :return: an array of strings of length 4.
    """
    return [i for i in x if len(i) == 4]


class TestFriend(unittest.TestCase):
    """Class to test 'friend' function"""

    def test_friend(self):
        self.assertEqual(friend(["Ryan", "Kieran", "Mark"]), ["Ryan", "Mark"])


if __name__ == '__main__':
    unittest.main()
