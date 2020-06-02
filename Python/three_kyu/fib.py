# Python solution for 'The Millionth Fibonacci Kata' codewars question.
# Level: 3 kyu
# Tags: ALGORITHMS, MATHEMATICS, and NUMBERS.
# Author: Jack Brokenshire
# Date: 02/06/2020

import unittest


def matrix_multiply(A, B):
    num_rows, num_cols = len(A), len(B[0])
    C = [[0] * num_cols for _ in range(num_rows)]
    for i in range(num_rows):
        for j in range(num_cols):
            C[i][j] = sum(A[i][k] * B[k][j] for k in range(len(B)))
    return C


def matrix_power(A, n):
    if n == 1:
        return A
    elif n % 2 == 1:
        P = matrix_power(A, (n - 1) / 2)
        P = matrix_multiply(P, P)
        return matrix_multiply(P, A)
    else:
        P = matrix_power(A, n / 2)
        return matrix_multiply(P, P)


def fib(n, negative=None):
    """Calculates the nth Fibonacci number"""
    if negative is None:
        if n < 0:
            negative = True
        else:
            negative = False
    if n == 0:
        return 0
    if negative and n % 2 == 0:
        return - matrix_power([[1, 1], [1, 0]], abs(n))[0][1]
    else:
        return matrix_power([[1, 1], [1, 0]], abs(n))[0][1]


class TestFib(unittest.TestCase):
    """Class to test 'fib' function"""

    def test_fib(self):
        self.assertEquals(fib(0), 0)
        self.assertEquals(fib(1), 1)
        self.assertEquals(fib(2), 1)
        self.assertEquals(fib(3), 2)
        self.assertEquals(fib(4), 3)
        self.assertEquals(fib(5), 5)
        self.assertEquals(fib(1000),
                          43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875)


if __name__ == '__main__':
    unittest.main()
