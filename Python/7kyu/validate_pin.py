# Python solution for "Regex validate PIN code" codewars question.
# Level: 7 kyu
# Tags: Fundamentals, Regular Expressions, Declarative Programming, Advanced Language Features, and Strings.
# Author: Jack Brokenshire
# Date: 30/03/2020

import unittest


def validate_pin(pin):
    """
    ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly
    6 digits. If the function is passed a valid PIN string, return true, else return false.
    :param pin: a string input with either numbers or characters or both.
    :return: True if valid PIN string otherwise, false.
    """
    return (len(pin) == 4 or len(pin) == 6) and pin.isnumeric()


class TestValidatePin(unittest.TestCase):
    """Class to test "validate_pin" function"""

    def test_validate_pin(self):
        self.assertEqual(validate_pin("1"), False)
        self.assertEqual(validate_pin("12"), False)
        self.assertEqual(validate_pin("123"), False)
        self.assertEqual(validate_pin("12345"), False)
        self.assertEqual(validate_pin("1234567"), False)
        self.assertEqual(validate_pin("-1234"), False)
        self.assertEqual(validate_pin("1.234"), False)
        self.assertEqual(validate_pin("-1.234"), False)
        self.assertEqual(validate_pin("00000000"), False)
        self.assertEqual(validate_pin("a234"), False)
        self.assertEqual(validate_pin(".234"), False)
        self.assertEqual(validate_pin("-123"), False)
        self.assertEqual(validate_pin("-1.234"), False)
        self.assertEqual(validate_pin("1234"), True)
        self.assertEqual(validate_pin("0000"), True)
        self.assertEqual(validate_pin("1111"), True)
        self.assertEqual(validate_pin("123456"), True)
        self.assertEqual(validate_pin("098765"), True)
        self.assertEqual(validate_pin("000000"), True)
        self.assertEqual(validate_pin("123456"), True)
        self.assertEqual(validate_pin("090909"), True)


if __name__ == "__main__":
    unittest.main()
