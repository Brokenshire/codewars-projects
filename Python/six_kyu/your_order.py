# Python solution for 'Your order, please' codewars question.
# Level: 6 kyu
# Tags: Fundamentals, Numbers, and Arrays
# Author: Jack Brokenshire
# Date: 11/02/2020

import unittest


def your_order(sentence):
    """
    Your task is to sort a given string. Each word in the string will contain a single number.
    This number is the position the word should have in the result.
    :param sentence: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
    :return: If the input string is empty, return an empty string. The words in the input String
             will only contain valid consecutive numbers.
    """
    words = [(int(i), x) for x in sentence.split() for i in x if i.isdigit()]
    words.sort(key=lambda x: x[0])
    return " ".join(x[1] for x in words)


class TestYourOrder(unittest.TestCase):
    """Class to test 'your_order' function"""

    def test_your_order(self):
        self.assertEqual(your_order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
        self.assertEqual(your_order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
        self.assertEqual(your_order(""), "")


if __name__ == '__main__':
    unittest.main()
