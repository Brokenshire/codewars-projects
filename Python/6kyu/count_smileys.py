# Python solution for 'Count the smiley faces!' codewars question.
# Level: 6 kyu
# Tags: Fundamentals, Regular Expressions, Declarative Programming, Advanced Language Features, and Strings.
# Author: Jack Brokenshire
# Date: 06/02/2020

import unittest


def count_smileys(arr):
    """
    Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.
    Rules for a smiling face:
    -Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
    -A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
    -Every smiling face must have a smiling mouth that should be marked with either ) or D.
    No additional characters are allowed except for those mentioned.
    :param arr: An array.
    :return: the total number of smiling faces.
    """
    total = 0
    for x in arr:
        if x[0] == ":" or x[0] == ";":
            if x[1] == ")" or x[1] == "D":
                total += 1
            elif x[1] == "-" or x[1] == "~":
                if x[2] == ")" or x[2] == "D":
                    total += 1
    return total


class TestCountSmileys(unittest.TestCase):
    """Class to test 'count_smileys' function"""

    def test_count_smileys(self):
        self.assertEqual(count_smileys([':)', ';(', ';}', ':-D']), 2);
        self.assertEqual(count_smileys([';D', ':-(', ':-)', ';~)']), 3);
        self.assertEqual(count_smileys([';]', ':[', ';*', ':$', ';-D']), 1);
        self.assertEqual(count_smileys([]), 0);
        self.assertEqual(count_smileys([':D',':~)',';~D',':)']), 4);
        self.assertEqual(count_smileys([':)',':(',':D',':O',':;']), 2);
        self.assertEqual(count_smileys([';]', ':[', ';*', ':$', ';-D']), 1);


if __name__ == '__main__':
    unittest.main()
