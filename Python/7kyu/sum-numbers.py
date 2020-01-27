import unittest


def get_sum(a,b):
    """Given two integers a and b, which can be positive or negative,
       find the sum of all the numbers between including them too and return it.
       If the two numbers are equal return a or b."""
    return sum(range(min(a, b), max(a, b) + 1))



class TestSum(unittest.TestCase):
    """Class to test get_sum function"""
    
    def test_sum(self):
        self.assertEqual(get_sum(0,1),1)
        self.assertEqual(get_sum(0,-1),-1)


if __name__ == '__main__':
    unittest.main() 