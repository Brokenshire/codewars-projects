# Python solution for 'Disemvowel Trolls' codewars question.
# Level: 7 kyu
# Tags: Fundamentals, Strings, Regular Expressions, Declarative Programming, Advanced Language Features.
# Author: Jack Brokenshire
# Date: 16/02/2020

import unittest


def disemvowel(string):
    """
    Trolls are attacking your comment section! A common way to deal with this situation is to remove all of the vowels
    from the trolls' comments, neutralizing the threat. Your task is to write a function that takes a string and
    return a new string with all vowels removed.
    :param string: A string value input.
    :return: A new string with all vowels removed.
    """
    return "".join(x for x in list(string) if x.lower() not in "aeiou")


class TestDisemvowel(unittest.TestCase):
    """Class to test 'disemvowel' function"""

    def test_disemvowel(self):
        self.assertEqual(disemvowel("This website is for losers LOL!"),
                         "Ths wbst s fr lsrs LL!")


if __name__ == '__main__':
    unittest.main()
