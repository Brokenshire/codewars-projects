# Python solution for "Currency Conversion" codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS, MATHEMATICS, ALGORITHMS, NUMBERS, and ALGEBRA.
# Author: Jack Brokenshire
# Date: 05/04/2020

import unittest


CONVERSION_RATES = {
  "Argentinian Peso": 10,
  "Armenian Dram": 478,
  "Bangladeshi Taka": 1010010,
  "Croatian Kuna": 110,
  "Czech Koruna": 10101,
  "Dominican Peso": 110000,
  "Egyptian Pound": 18,
  "Guatemalan Quetzal": 111,
  "Haitian Gourde": 1000000,
  "Indian Rupee": 63,
  "Japanese Yen": 1101111,
  "Kenyan Shilling": 1100110,
  "Nicaraguan Cordoba": 11111,
  "Norwegian Krone": 1000,
  "Philippine Piso": 110010,
  "Romanian Leu": 100,
  "Samoan Tala": 11,
  "South Korean Won": 10000100011,
  "Thai Baht": 100000,
  "Uzbekistani Som": 8333,
  "Venezuelan Bolivar": 1010,
  "Vietnamese Dong": 101100000101101
}


def convert_my_dollars(usd, currency):
    """
    If a country's currency begins with a consonant, then the conversion rate has been tampered with.
    :param usd: integer of amount of united states dollars.
    :param currency: string of currency to be converted.
    :return: the amount of foreign currency you will receive when you exchange your United States Dollars.
    """
    if currency[0] in "AEIOU":
        return "You now have {} of {}.".format(CONVERSION_RATES[currency] * usd, currency)
    else:
        return "You now have {} of {}.".format(int(str(CONVERSION_RATES[currency]), 2) * usd, currency)


class TestConvertMyDollars(unittest.TestCase):
    """Class to test "convert_my_dollars" function"""

    def test_convert_my_dollars(self):
        self.assertEqual(convert_my_dollars(7, "Armenian Dram"), "You now have 3346 of Armenian Dram.")
        self.assertEqual(convert_my_dollars(322, "Armenian Dram"), "You now have 153916 of Armenian Dram.")
        self.assertEqual(convert_my_dollars(25, "Bangladeshi Taka"), "You now have 2050 of Bangladeshi Taka.")
        self.assertEqual(convert_my_dollars(730, "Bangladeshi Taka"), "You now have 59860 of Bangladeshi Taka.")
        self.assertEqual(convert_my_dollars(37, "Croatian Kuna"), "You now have 222 of Croatian Kuna.")
        self.assertEqual(convert_my_dollars(40, "Croatian Kuna"), "You now have 240 of Croatian Kuna.")
        self.assertEqual(convert_my_dollars(197, "Czech Koruna"), "You now have 4137 of Czech Koruna.")
        self.assertEqual(convert_my_dollars(333, "Czech Koruna"), "You now have 6993 of Czech Koruna.")
        self.assertEqual(convert_my_dollars(768, "Dominican Peso"), "You now have 36864 of Dominican Peso.")
        self.assertEqual(convert_my_dollars(983, "Dominican Peso"), "You now have 47184 of Dominican Peso.")


if __name__ == "__main__":
    unittest.main()
