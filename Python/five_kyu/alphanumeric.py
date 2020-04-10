# Python solution for 'Not very secure' codewars question.
# Level: 5 kyu
# Tags: Bugs, Regular Expressions, Declarative Programming, Advanced Language Features, Fundamentals, and Strings
# Author: Jack Brokenshire
# Date: 07/02/2020

import unittest
import re


def alphanumeric(password):
    """
    In this example you have to validate if a user input string is self.assertEqual(alphanumeric. The given string is not
    nil/null/NULL/None, so you don't have to check that. The string has the following conditions to be self.assertEqual(alphanumeric:
        At least one character ("" is not valid)
        Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
        No whitespaces / underscore
    :param password: an input string
    :return: true if the given string only contains letters and digits
    """
    if re.findall('^[a-zA-Z0-9]+$', password):
        return True
    return False


class TestAlphanumeric(unittest.TestCase):
    """Class to test 'alphanumeric' function"""

    def test_alphanumeric(self):
        self.assertEqual(alphanumeric("hello world_"), False)
        self.assertEqual(alphanumeric("PassW0rd"), True)
        self.assertEqual(alphanumeric("     "), False)
        self.assertEqual(alphanumeric("HZkCZWnVmLsz"), True)
        self.assertEqual(alphanumeric("vjVo7INZWzVk7fHCR"), True)
        self.assertEqual(alphanumeric("PcT8rltDegFyEo7BnxLoRlADWS"), True)
        self.assertEqual(alphanumeric("zZWQOgZoPOK/ey3da3HF"), False)
        self.assertEqual(alphanumeric("9\H2W1mWI9E"), False)
        self.assertEqual(alphanumeric("~CkDXFc"), False)
        self.assertEqual(alphanumeric("YIUGN&jLadMfuqRJd94v273L"), False)
        self.assertEqual(alphanumeric("3goec7c4VCVEu3dS<P"), False)
        self.assertEqual(alphanumeric("ihw58LaYz2ylf4tpsCKqiXXoBRgxR"), True)
        self.assertEqual(alphanumeric("&9mrGziQ"), False)
        self.assertEqual(alphanumeric("]E"), False)
        self.assertEqual(alphanumeric("6<7"), False)
        self.assertEqual(alphanumeric("lbiCZb+cP"), False)
        self.assertEqual(alphanumeric("5dkwx2mVwZT9dmqFc"), True)
        self.assertEqual(alphanumeric("YnBvMbAWxktBRvS8s"), True)
        self.assertEqual(alphanumeric("sPp9YHUFztvLJ3D09wVTB8WUrO"), True)
        self.assertEqual(alphanumeric("Vg8sJv"), True)
        self.assertEqual(alphanumeric("dRjQ02WNkhEc8IWGHqrnnGNU"), True)
        self.assertEqual(alphanumeric(">vH"), False)
        self.assertEqual(alphanumeric("jVrUTxNyuxiyr"), True)
        self.assertEqual(alphanumeric("BXrF"), True)
        self.assertEqual(alphanumeric("wW 4U4"), False)
        self.assertEqual(alphanumeric("tpb2zxpZWFUNRvispkWmOh"), True)
        self.assertEqual(alphanumeric("t9hiuKKlkjBprleaXT"), True)
        self.assertEqual(alphanumeric("]HAPsJNXcZK8lS"), False)
        self.assertEqual(alphanumeric("qIXaCjSi'OzE1Z"), False)
        self.assertEqual(alphanumeric("I4csVW9sqPe3sO6OJr22pOh"), True)
        self.assertEqual(alphanumeric("Dd945P9bm99bU4sXhFTNuG Hc59fH"), False)
        self.assertEqual(alphanumeric("gN4UV4cHGt6MgaRw{strMThPxR"), False)
        self.assertEqual(alphanumeric("KDA4u6KX3UG1LE2g6KaXu"), True)
        self.assertEqual(alphanumeric("I:xspw0CyIDbLboRuAqsYL"), False)
        self.assertEqual(alphanumeric("LTVB2(T"), False)


if __name__ == '__main__':
    unittest.main()
