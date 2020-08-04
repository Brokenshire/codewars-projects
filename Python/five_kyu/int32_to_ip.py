# Python solution for 'int32 to IPv4' codewars question.
# Level: 5 kyu
# Tags: ALGORITHMS, NETWORKS, BITS, BINARY, AND UTILITIES.
# Author: Jack Brokenshire
# Date: 04/08/2020

import unittest
import ipaddress


def int32_to_ip(int32):
    """
    Takes an unsigned 32 bit number and returns a string representation of its IPv4 address.
    :param int32: 32 bit integer value.
    :return: string representation of int32 value.
    """
    return str(ipaddress.IPv4Address(int32))


class TestInt32ToIp(unittest.TestCase):
    """Class to test 'int32_to_ip' function"""

    def test_int32_to_ip(self):
        self.assertEqual(int32_to_ip(2154959208), "128.114.17.104")
        self.assertEqual(int32_to_ip(0), "0.0.0.0")
        self.assertEqual(int32_to_ip(2149583361), "128.32.10.1")


if __name__ == "__main__":
    unittest.main()
