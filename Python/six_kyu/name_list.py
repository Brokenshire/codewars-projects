# Python solution for 'Format a string of names like 'Bart, Lisa & Maggie'.' codewars question.
# Level: 6 kyu
# Tags: Fundamentals, Strings, Formatting, and Algorithms
# Author: Jack Brokenshire
# Date: 04/02/2020

import unittest


def namelist(names):
    """
    Function which returns a new list with proper formatting between names.
    :param names: an array containing hashes of names
    :return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.
    """
    list = [name['name'] for name in names]
    if len(list) <= 1:
        return ''.join(list)
    else:
        last_two = ' & '.join(list[-2:])
        first = [n + ',' for n in list[:-2]]
        first.append(last_two)
        return ' '.join(first)


class TestNameList(unittest.TestCase):
    """Class to test 'nameList' function"""

    def test_name_list(self):
        self.assertEqual(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]), 'Bart, Lisa & Maggie')
        self.assertEqual(namelist([{'name': 'Bart'}, {'name': 'Lisa'}]), 'Bart & Lisa')
        self.assertEqual(namelist([{'name': 'Bart'}]), 'Bart')
        self.assertEqual(namelist([]), '')


if __name__ == '__main__':
    unittest.main()
