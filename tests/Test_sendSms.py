#!/usr/bin/python3
# coding: utf8
import unittest
import os
import configparser
from Transilien_Domoticz.transilien import send_sms, format_content

config_name = "conf.cfg"
config_file = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "/Transilien_Domoticz/" + config_name
config = configparser.ConfigParser()
config.read(config_file)
nbr_trains = 2
depart_name = config["default"]["departName"]
host_sms = config["sms"]["host"]
port_sms = config["sms"].getint('port')
password_sms = config["sms"]["password"]
number = config["sms"]["number"].split(',')


class TestSendSms(unittest.TestCase):

    global values
    content = """<?xml version="1.0" encoding="UTF-8"?>\r\n<passages gare="87393405">\r\n<train><date mode="R">26/01/2017 08:38</date>\r\n<num>164674</num>\r\n<miss>PEMU</miss>\r\n<term>87391003</term>\r\n<etat>Retardé</etat>\r\n</train>\r\n<train><date mode="R">26/01/2017 08:52</date>\r\n<num>164576</num>\r\n<miss>PEGU</miss>\r\n<term>87391003</term>\r\n<etat>Supprimé</etat>\r\n</train>\r\n<train><date mode="R">26/01/2017 09:07</date>\r\n<num>164578</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n<etat>Supprimé</etat>\r\n</train>\r\n<train><date mode="R">26/01/2017 09:37</date>\r\n<num>164682</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n</passages>"""
    values, state = format_content(nbr_trains, content, depart_name)

    def test_normal_with_one_number(self):
        self.assertTrue(test_values(values))
        value = send_sms(host_sms, port_sms, password_sms, number, values)
        self.assertEqual("""<html>\n<body>\nMesage SENT!<br/>\n</body>\n</html>""", value[0].decode("utf-8"))
        self.assertFalse(test_values(values))

    def test_normal_with_two_numbers(self):
        value = send_sms(host_sms, port_sms, password_sms, [number[0], number[0]], values)
        self.assertEqual("""<html>\n<body>\nMesage SENT!<br/>\n</body>\n</html>""", value[0].decode("utf-8"))
        self.assertEqual("""<html>\n<body>\nMesage SENT!<br/>\n</body>\n</html>""", value[1].decode("utf-8"))

    def test_wrong_host(self):
        value = send_sms("1.1.0.0", port_sms, password_sms, number, values)
        self.assertEqual('Failed to reach a serverReason: [Errno 60] Operation timed out', value)

    def test_wrong_host_format_content(self):
        value = send_sms("azerty", port_sms, password_sms, number, values)
        self.assertEqual('Failed to reach a serverReason: [Errno 8] nodename nor servname provided, or not known', value)

    def test_wrong_host_format_content2(self):
        value = send_sms(1234, port_sms, password_sms, number, values)
        self.assertEqual('Failed to reach a serverReason: [Errno 65] No route to host', value)

    def test_wrong_port(self):
        value = send_sms(host_sms, 1234, password_sms, number, values)
        self.assertEqual('Failed to reach a serverReason: [Errno 61] Connection refused', value)

    def test_wrong_port2(self):
        value = send_sms(host_sms, "port_sms", password_sms, number, values)
        self.assertEqual('Problem with port number', value)

    def test_wrong_password(self):
        value = send_sms(host_sms, port_sms, "password_sms", number, values)
        self.assertEqual('Request Error code: 400', value)

    def test_wrong_password_format_content(self):
        value = send_sms(host_sms, port_sms, 1234, number, values)
        self.assertEqual('Request Error code: 400', value)

    def test_wrong_values_format_content(self):
        value = send_sms(host_sms, port_sms, password_sms, number, 1234)
        self.assertEqual('Problem with values: need to be a list or a tuple', value)

    def test_wrong_values_format_content2(self):
        value = send_sms(host_sms, port_sms, password_sms, number, "1234")
        self.assertEqual('Problem with values: need to be a list or a tuple', value)

    def test_wrong_values_empty(self):
        value = send_sms(host_sms, port_sms, password_sms, number, "")
        self.assertEqual('Problem with values: Empty', value)

    def test_wrong_values_empty2(self):
        value = send_sms(host_sms, port_sms, password_sms, number, None)
        self.assertEqual('Problem with values: Empty', value)

    def test_wrong_number(self):
        value = send_sms(host_sms, port_sms, password_sms, ["number"], values)
        self.assertEqual("Invalid mobile number: number", value)

    def test_wrong_number2(self):
        value = send_sms(host_sms, port_sms, password_sms, ["06564534098"], values)
        self.assertEqual("Invalid mobile number: 06564534098", value)

    def test_wrong_number3(self):
        value = send_sms(host_sms, port_sms, password_sms, ["06564534098", number[0]], values)
        self.assertEqual("Invalid mobile number: 06564534098", value)

    def test_wrong_number4(self):
        value = send_sms(host_sms, port_sms, password_sms, [number[0], "06564534098"], values)
        self.assertEqual("Invalid mobile number: 06564534098", value)


if __name__ == '__main__':
    unittest.main()
