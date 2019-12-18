import unittest


def longest_consec(strarr, k):
    """Returns the first longest string consisting of k consecutive strings taken in the array."""
    if len(strarr) == 0 or k <= 0 or k > len(strarr):
        return ""
    lst = [''.join(strarr[i:i+k]) for i in range(len(strarr))]
    return max(lst, key= lambda x: len(x))



class TestLongestConsec(unittest.TestCase):
    """Class to test longest_consec function"""
    
    def test_longest_string(self):
        self.assertEqual(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta")
        self.assertEqual(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1), "oocccffuucccjjjkkkjyyyeehh")
        self.assertEqual(longest_consec([], 3), "")
        self.assertEqual(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2), "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
        self.assertEqual(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2), "wlwsasphmxxowiaxujylentrklctozmymu")
        self.assertEqual(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2), "")
        self.assertEqual(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3), "ixoyx3452zzzzzzzzzzzz")
        self.assertEqual(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15), "")
        self.assertEqual(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0), "")


if __name__ == '__main__':
    unittest.main()