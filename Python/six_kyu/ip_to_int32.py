# Python solution for 'IPv4 to int32' codewars question.
# Level: 6 kyu
# Tags: FUNDAMENTALS, NETWORKS, ALGORITHMS, BITS, BINARY, NUMBERS, INTEGERS, AND UTILITIES.
# Author: Jack Brokenshire
# Date: 27/07/2020

import unittest
import socket
import struct


def ip_to_int32(ip):
    """
    Take the following IPv4 address: 128.32.10.1 This address has 4 octets where each octet is a single byte (or 8 bits).
    :param ip: string representation of IPv4 address.
    :return: a 32-bit number.
    """
    return struct.unpack("!I", socket.inet_aton(ip))[0]


class TestIpToInt32(unittest.TestCase):
    """Class to test 'ip_to_int32' function"""

    def test_ip_to_int32(self):
        self.assertEqual(ip_to_int32("128.114.17.104") == 2154959208, "wrong integer for ip: 128.114.17.104")
        self.assertEqual(ip_to_int32("0.0.0.0") == 0, "wrong integer for ip: 0.0.0.0")
        self.assertEqual(ip_to_int32("128.32.10.1") == 2149583361, "wrong integer for ip: 128.32.10.1")


if __name__ == "__main__":
    unittest.main()
