# Python solution for 'Welcome!' codewars question.
# Level: 8 kyu
# Tags: FUNDAMENTALS, HASHES, DATA STRUCTURES, amd OBJECTS.
# Author: Jack Brokenshire
# Date: 22/05/2020

import unittest


def greet_welcome(language):
    """
    Greets a given language in their language otherwise uses Welcome.
    :param language: string determining language to greet.
    :return: A greeting - if you have it in your database. It should default to English if the language is not in the
             database, or in the event of an invalid input.
    """
    database = {'english': 'Welcome',
                'czech': 'Vitejte',
                'danish': 'Velkomst',
                'dutch': 'Welkom',
                'estonian': 'Tere tulemast',
                'finnish': 'Tervetuloa',
                'flemish': 'Welgekomen',
                'french': 'Bienvenue',
                'german': 'Willkommen',
                'irish': 'Failte',
                'italian': 'Benvenuto',
                'latvian': 'Gaidits',
                'lithuanian': 'Laukiamas',
                'polish': 'Witamy',
                'spanish': 'Bienvenido',
                'swedish': 'Valkommen',
                'welsh': 'Croeso'}
    if language not in database:
        return "Welcome"
    return database[language]


class TestGreetWelcome(unittest.TestCase):
    """Class to test 'greet_welcome' function"""

    def test_greet_welcome(self):
        self.assertEqual(greet_welcome('english'), 'Welcome')
        self.assertEqual(greet_welcome('dutch'), 'Welkom')
        self.assertEqual(greet_welcome('IP_ADDRESS_INVALID'), 'Welcome')
        self.assertEqual(greet_welcome(''), 'Welcome')
        self.assertEqual(greet_welcome(2), 'Welcome')


if __name__ == '__main__':
    unittest.main()
