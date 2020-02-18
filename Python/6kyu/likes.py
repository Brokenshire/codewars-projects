# Python solution for 'Who likes it?' codewars question.
# Level: 6 kyu
# Tags: Fundamentals, Formatting, Algorithms, and Strings.
# Author: Jack Brokenshire
# Date: 19/02/2020

import unittest


def likes(names):
    """
    You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other
    items. We want to create the text that should be displayed next to such an item.
    Implement a function likes :: [String] -> String, which must take in input array, containing the names of people
    who like an item. For 4 or more names, the number in and 2 others simply increases.
    :param names: A list of names whom like a post.
    :return: Nicely formatted string of people liking a post.
    """
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)


class TestLikes(unittest.TestCase):
    """Class to test 'likes' function"""

    def test_likes(self):
        self.assertEqual(likes([]), 'no one likes this')
        self.assertEqual(likes(['Peter']), 'Peter likes this')
        self.assertEqual(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
        self.assertEqual(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
        self.assertEqual(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')


if __name__ == '__main__':
    unittest.main()
