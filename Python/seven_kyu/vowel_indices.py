# Python solution for 'Find the vowels' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS.
# Author: Jack Brokenshire
# Date: 19/05/2020

import unittest


def vowel_indices(word):
    """
    We want to know the index of the vowels in a given word, for example, there are two vowels in the word super
    (the second and fourth letters).
    :param word: A string input.
    :return: a list of indices of the vowels.
    """
    return [i + 1 for i, j in enumerate(word) if j.lower() in "aeiouy"]


class TestVowelIndices(unittest.TestCase):
    """Class to test 'vowel_indices' function"""

    def test_vowel_indices(self):
        self.assertEqual(vowel_indices("super"), [2,4])
        self.assertEqual(vowel_indices("Mmmm"), [])
        self.assertEqual(vowel_indices("Super"), [2, 4])
        self.assertEqual(vowel_indices("Apple"), [1, 5])
        self.assertEqual(vowel_indices("YoMama"), [1, 2, 4, 6])


if __name__ == '__main__':
    unittest.main()
