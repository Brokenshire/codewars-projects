# Python solution for Two to One codewars question.
# Level: 7 kyu
# Tags: Fundamentals
# Author: Jack Brokenshire
# Date: 24/01/2020

from collections import OrderedDict
import unittest


def longest(s1, s2):
    """ Returns a new sorted string, the longest possible, containing distinct letters."""
    word = "".join(OrderedDict.fromkeys(s1.join((s2))))
    return "".join(sorted(word))


class TestLongest(unittest.TestCase):
    """Class to test longest function"""
    
    def test_longest_string(self):
        self.assertEqual(longest("aretheyhere", "yestheyarehere"), "aehrsty")
        self.assertEqual(longest("loopingisfunbutdangerous", "lessdangerousthancoding"), "abcdefghilnoprstu")
        self.assertEqual(longest("inmanylanguages", "theresapairoffunctions"), "acefghilmnoprstuy")


if __name__ == '__main__':
    unittest.main()
