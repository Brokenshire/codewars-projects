# Python solution for 'Title Case' codewars question.
# Level: 6 kyu
# Tags: FUNDAMENTALS, STRINGS, PARSING, and ALGORITHMS.
# Author: Jack Brokenshire
# Date: 25/04/2020

import unittest


def title_case(title, minor_words=''):
    """
    Converts a string into title case, given an optional list of exceptions (minor words).
    :param title: a string of words.
    :param minor_words: a string of words.
    :return: the title in title case form.
    """
    return " ".join(x.capitalize() if x not in minor_words.lower().split() or i == 0 else x for i, x in enumerate(title.lower().split()))


class TestTitleCase(unittest.TestCase):
    """Class to test 'title_case' function"""

    def test_title_case(self):
        self.assertEqual(title_case(''), '')
        self.assertEqual(title_case('a clash of KINGS', 'a an the of'), 'A Clash of Kings')
        self.assertEqual(title_case('THE WIND IN THE WILLOWS', 'The In'), 'The Wind in the Willows')
        self.assertEqual(title_case('the quick brown fox'), 'The Quick Brown Fox')


if __name__ == '__main__':
    unittest.main()
