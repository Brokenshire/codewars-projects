# Python solution for 'Check the exam' codewars question.
# Level: 8 kyu
# Tags: FUNDAMENTALS, ARRAYS, NUMBERS, and BASIC LANGUAGE FEATURES.
# Author: Jack Brokenshire
# Date: 11/07/2020

import unittest


def check_exam(arr1, arr2):
    """
    Marks an exam checking whether the students answers to the solution.
    :param arr1: array of strings containing correct solutions.
    :param arr2: array of strings containing student answers.
    :return: the score for this array of answers, giving +4 for each correct answer, -1 for each incorrect answer,
             and +0 for each blank answer(empty string).
    """
    score = 0
    for x in range(len(arr1)):
        if arr1[x] == arr2[x]:
            score += 4
        elif arr1[x] != arr2[x] and arr2[x] != "":
            score -= 1
    if score < 0:
        return 0
    return score


class TestCheckExam(unittest.TestCase):
    """Class to test 'check_exam' function"""

    def test_check_exam(self):
        self.assertEqual(check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]), 6)
        self.assertEqual(check_exam(["a", "a", "c", "b"], ["a", "a", "b",  ""]), 7)
        self.assertEqual(check_exam(["a", "a", "b", "c"], ["a", "a", "b", "c"]), 16)
        self.assertEqual(check_exam(["b", "c", "b", "a"], ["",  "a", "a", "c"]), 0)


if __name__ == '__main__':
    unittest.main()
