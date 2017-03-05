#!/usr/bin/python3
# coding: utf8
import unittest
from Transilien_Domoticz.transilien import valid_number


class TestValidNumber(unittest.TestCase):
    def test_normal(self):
        self.assertTrue(valid_number("0600000000"))

    def test_normal2(self):
        self.assertTrue(valid_number(" 06 00 00 00 00 "))

    def test_wrong_number(self):
        self.assertFalse(valid_number("06 00 00 0p 00"))

    def test_wrong_number2(self):
        self.assertFalse(valid_number("6 00 00 00 00"))

    def test_wrong_number3(self):
        self.assertFalse(valid_number(" 06 00 00 07 0 00 "))

    def test_wrong_number4(self):
        self.assertFalse(valid_number(" prootoot "))


if __name__ == '__main__':
    unittest.main()
