# Python solution for 'Square Every Digit' codewars question.
# Level: 5 kyu
# Tags: Algorithms
# Author: Jack Brokenshire
# Date: 11/02/2020

import unittest


def pig_it(text):
    """
    Move the first letter of each word to the end of it, then add "ay" to the end of the word.
    Leave punctuation marks untouched.
    :param text: an input string value.
    :return: the first letter of each word to the end of it, then add "ay" to the end of the word.
    """
    return " ".join(map(str, [x[1:] + x[0:1] + "ay" if x.isalpha() else x for x in text.split()]))


class TestPigIt(unittest.TestCase):
    """Class to test 'pig_it' function"""

    def test_pig_it(self):
        self.assertEqual(pig_it('Pig latin is cool'), 'igPay atinlay siay oolcay')
        self.assertEqual(pig_it('This is my string'), 'hisTay siay ymay tringsay')


if __name__ == '__main__':
    unittest.main()
