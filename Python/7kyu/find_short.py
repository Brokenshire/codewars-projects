import unittest 

def find_short(s):
    """Given a string of words, return the length of the shortest word(s)."""
    return min(len(x) for x in s.split())


class TestFindShort(unittest.TestCase):
    """Class to test find_short function"""
    
    def test_length_shortest_words(self):
        self.assertEqual(find_short("bitcoin take over the world maybe who knows perhaps"), 3)
        self.assertEqual(find_short("turns out random test cases are easier than writing out basic ones"), 3)
        self.assertEqual(find_short("lets talk about javascript the best language"), 3)
        self.assertEqual(find_short("i want to travel the world writing code one day"), 1)
        self.assertEqual(find_short("Lets all go on holiday somewhere very cold"), 2)


if __name__ == '__main__':
    unittest.main()