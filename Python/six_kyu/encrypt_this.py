# Python solution for 'Encrypt this!' codewars question.
# Level: 6 kyu
# Tags: FUNDAMENTALS, STRINGS, REGULAR EXPRESSIONS, DECLARATIVE PROGRAMMING, ADVANCED LANGUAGE FEATURES, ARRAYS,
#       CIPHERS, ALGORITHMS, CRYPTOGRAPHY, and SECURITY.
# Author: Jack Brokenshire
# Date: 02/05/2020

import unittest


def encrypt_this(text):
    """
    Your message is a string containing space separated words. You need to encrypt each word in the message using the
    following rules: The first letter needs to be converted to its ASCII code. The second letter needs to be switched
    with the last letter Keepin' it simple: There are no special characters in input.
    :param text: a string input to be encrypted.
    :return: the encrypted string which follows the parameters above.
    """
    result = []
    for word in text.split():
        word = list(word)
        word[0] = str(ord(word[0]))
        if len(word) > 2:
            word[1], word[-1] = word[-1], word[1]
        result.append("".join(word))
    return " ".join(result)


class TestEncryptThis(unittest.TestCase):
    """Class to test 'encrypt_this' function"""

    def test_encrypt_this(self):
        tests = [
            ("", ""),
            ("A wise old owl lived in an oak", "65 119esi 111dl 111lw 108dvei 105n 97n 111ka"),
            ("The more he saw the less he spoke", "84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp"),
            ("The less he spoke the more he heard", "84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare"),
            ("Why can we not all be like that wise old bird",
             "87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri"),
            ("Thank you Piotr for all your help", "84kanh 121uo 80roti 102ro 97ll 121ruo 104ple"),
        ]

        for t in tests:
            inp, exp = t
            self.assertEqual(encrypt_this(inp), exp)


if __name__ == '__main__':
    unittest.main()
