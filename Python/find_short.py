import unittest 

def find_short(s):
    """Given a string of words, return the length of the shortest word(s)."""
    return min(len(x) for x in s.split())


class TestFindShort(unittest.TestCase):
    """Class to test find_short function"""

    def test_one(self):
        self.assertEqual(find_short("bitcoin take over the world maybe who knows perhaps"), 3)

    def test_two(self):
        self.assertEqual(find_short("turns out random test cases are easier than writing out basic ones"), 3)
    
    def test_three(self):
        self.assertEqual(find_short("lets talk about javascript the best language"), 3)

    def test_four(self):
        self.assertEqual(find_short("i want to travel the world writing code one day"), 1)

    def test_five(self):
        self.assertEqual(find_short("Lets all go on holiday somewhere very cold"), 2)


if __name__ == '__main__':
    unittest.main()