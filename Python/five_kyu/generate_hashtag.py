# Python solution for 'The Hashtag Generator' codewars question.
# Level: 5 kyu
# Tags: ALGORITHMS and STRINGS.
# Author: Jack Brokenshire
# Date: 26/04/2020

import unittest


def generate_hashtag(s):
    """
    Generates a hashtag which ever word is capitalized and we start with a hashtag. Also, string can't be longer than
    140 chars or empty.
    :param s: a string value.
    :return: the string in hashtag form otherwise, False.
    """
    if len(s) > 140 or len(s) < 1: return False
    return "#" + "".join(x.capitalize() for x in s.split())


class TestGenerateHashtag(unittest.TestCase):
    """Class to test 'generate_hashtag' function"""

    def test_generate_hashtag(self):
        self.assertEqual(generate_hashtag(''), False, 'Expected an empty string to return False')
        self.assertEqual(generate_hashtag('Do We have A Hashtag')[0], '#', 'Expeted a Hashtag (#) at the beginning.')
        self.assertEqual(generate_hashtag('Codewars'), '#Codewars', 'Should handle a single word.')
        self.assertEqual(generate_hashtag('Codewars      '), '#Codewars', 'Should handle trailing whitespace.')
        self.assertEqual(generate_hashtag('Codewars Is Nice'), '#CodewarsIsNice', 'Should remove spaces.')
        self.assertEqual(generate_hashtag('codewars is nice'), '#CodewarsIsNice', 'Should capitalize first letters of words.')
        self.assertEqual(generate_hashtag('CodeWars is nice'), '#CodewarsIsNice', 'Should capitalize all letters of words - all lower case but the first.')
        self.assertEqual(generate_hashtag('c i n'), '#CIN', 'Should capitalize first letters of words even when single letters.')
        self.assertEqual(generate_hashtag('codewars  is  nice'), '#CodewarsIsNice', 'Should deal with unnecessary middle spaces.')
        self.assertEqual(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'), False, 'Should return False if the final word is longer than 140 chars.')


if __name__ == '__main__':
    unittest.main()
