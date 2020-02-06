# Python solution for 'Dubstep' codewars question.
# Level: 6 kyu
# Tags: Fundamentals, and Strings.
# Author: Jack Brokenshire
# Date: 05/02/2020

import unittest


def song_decoder(song):
    """
    Removes 'WUB' from a string to find the true message of the song.
    :param song: The input consists of a single non-empty string, consisting only of uppercase English letters, the string's length doesn't exceed 200 characters
    :return: the words of the initial song that Polycarpus used to make a dubsteb remix. Separate the words with a space.
    """
    return " ".join(song.replace('WUB', ' ').split())


class TestSongDecoder(unittest.TestCase):
    """Class to test 'song_decoder' function"""

    def test_song_decoder(self):
        self.assertEqual(song_decoder("AWUBBWUBC"), "A B C");
        self.assertEqual(song_decoder("AWUBWUBWUBBWUBWUBWUBC"), "A B C");
        self.assertEqual(song_decoder("WUBAWUBBWUBCWUB"), "A B C");


if __name__ == '__main__':
    unittest.main()
