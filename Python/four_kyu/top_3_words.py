# Python solution for 'Most frequently used words in a text' codewars question.
# Level: 4 kyu
# Tags: ALGORITHMS, STRINGS, PARSING, RANKING, and FILTERING.
# Author: Jack Brokenshire
# Date: 26/01/2021

import unittest
from collections import Counter
import re


def top_3_words(text):
    """ Find the three most used words in a string.

    Args:
        text (str): A string of text (possibly with punctuation and line-breaks).

    Returns:
        Array: An array of the top-3 most occurring words, in descending order of the number of occurrences.
    """
    words = re.findall("[\s]?([']?[A-Za-z]+'?[A-Za-z']*)[\s,:]?", text)
    c = Counter()
    for x in words:
        c[x.lower()] += 1
    return [x[0] for x in c.most_common(3)]


class TestTopThreeWords(unittest.TestCase):
    """Class to test 'top_3_words' function"""

    def test_top_3_words(self):
        self.assertEqual(top_3_words("a a a  b  c c  d d d d  e e e e e"), ["e", "d", "a"])
        self.assertEqual(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"), ["e", "ddd", "aa"])
        self.assertEqual(top_3_words("  //wont won't won't "), ["won't", "wont"])
        self.assertEqual(top_3_words("  , e   .. "), ["e"])
        self.assertEqual(top_3_words("  ...  "), [])
        self.assertEqual(top_3_words("  '  "), [])
        self.assertEqual(top_3_words("  '''  "), [])
        self.assertEqual(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
        mind, there lived not long since one of those gentlemen that keep a lance
        in the lance-rack, an old buckler, a lean hack, and a greyhound for
        coursing. An olla of rather more beef than mutton, a salad on most
        nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
        on Sundays, made away with three-quarters of his income."""), ["a", "of", "on"])


if __name__ == '__main__':
    unittest.main()