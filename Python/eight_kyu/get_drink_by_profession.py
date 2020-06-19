# Python solution for 'L1: Bartender, drinks!' codewars question.
# Level: 8 kyu
# Tags: FUNDAMENTALS, CONDITIONAL STATEMENTS, CONTROL FLOW, BASIC LANGUAGE FEATURES, and STRINGS.
# Author: Jack Brokenshire
# Date: 20/06/2020

import unittest


def get_drink_by_profession(param):
    """
    Recevies a string input and returns the value in the dictionary or beer if not inside.
    :param param: a string value.
    :return: the value inside the dictionary. If not then beer.
    """
    words = {"Jabroni": "Patron Tequila", "School Counselor": "Anything with Alcohol", "Programmer": "Hipster Craft Beer",
             "Bike Gang Member": "Moonshine", "Politician": "Your tax dollars", "Rapper": "Cristal"}
    return words.get(param.title(), "Beer")


class TestGetDrinkByProfession(unittest.TestCase):
    """Class to test 'get_drink_by_profession' function"""

    def test_get_drink_by_profession(self):
        self.assertEqual(get_drink_by_profession("jabrOni"), "Patron Tequila", "'Jabroni' should map to 'Patron Tequila'")
        self.assertEqual(get_drink_by_profession("scHOOl counselor"), "Anything with Alcohol", "'School Counselor' should map to 'Anything with alcohol'")
        self.assertEqual(get_drink_by_profession("prOgramMer"), "Hipster Craft Beer", "'Programmer' should map to 'Hipster Craft Beer'")
        self.assertEqual(get_drink_by_profession("bike ganG member"), "Moonshine", "'Bike Gang Member' should map to 'Moonshine'")
        self.assertEqual(get_drink_by_profession("poLiTiCian"), "Your tax dollars", "'Politician' should map to 'Your tax dollars'")
        self.assertEqual(get_drink_by_profession("rapper"), "Cristal", "'Rapper' should map to 'Cristal'")
        self.assertEqual(get_drink_by_profession("pundit"), "Beer", "'Pundit' should map to 'Beer'")
        self.assertEqual(get_drink_by_profession("Pug"), "Beer", "'Pug' should map to 'Beer'")


if __name__ == '__main__':
    unittest.main()
