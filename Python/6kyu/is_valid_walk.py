# Python solution for 'Take a Ten Minute Walk' codewars question.
# Level: 6 kyu
# Tags: Fundamentals and Arrays.
# Author: Jack Brokenshire
# Date: 11/03/2020

import unittest


def is_valid_walk(walk):
    """
    You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early
    to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens
    with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter
    strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block in a
    direction and you know it takes you one minute to traverse one city block.
    :param walk: a list of one-letter string directions.
    :return: true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!)
             and will, of course, return you to your starting point. Return false otherwise.
    """
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')


class TestIsValidWalk(unittest.TestCase):
    """Class to test 'is_valid_walk' function"""

    def test_is_valid_walk(self):
        self.assertEqual(is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']), 'should return True');
        self.assertEqual(not is_valid_walk(['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']),
                         'should return False');
        self.assertEqual(not is_valid_walk(['w']), 'should return False');
        self.assertEqual(not is_valid_walk(['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's']), 'should return False');


if __name__ == '__main__':
    unittest.main()
