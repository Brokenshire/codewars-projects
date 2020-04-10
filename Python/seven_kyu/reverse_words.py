# Python solution for 'Reverse words' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS and STRINGS.
# Author: Jack Brokenshire
# Date: 09/04/2020

import unittest


def reverse_words(text):
    """
    Complete the function that accepts a string parameter, and reverses each word in the string. All spaces
    in the string should be retained.
    :param text: string of words.
    :return: all words in the string reversed.
    """
    return " ".join(x[::-1] for x in text.split(" "))


class TestReverseWords(unittest.TestCase):
    """Class to test 'reverse_words' function"""

    def test_reverse_words(self):
        self.assertEqual(reverse_words('The quick brown fox jumps over the lazy dog.'), 'ehT kciuq nworb xof spmuj revo eht yzal .god')
        self.assertEqual(reverse_words('apple'), 'elppa')
        self.assertEqual(reverse_words('a b c d'), 'a b c d')
        self.assertEqual(reverse_words('double  spaced  words'), 'elbuod  decaps  sdrow')


if __name__ == '__main__':
    unittest.main()
