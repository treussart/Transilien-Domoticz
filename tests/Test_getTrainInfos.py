#!/usr/bin/python3
# coding: utf8
import unittest
import os
import configparser
from lxml import etree
from Transilien_Domoticz.transilien import get_train_infos

config_name = "conf.cfg"
config_file = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "/Transilien_Domoticz/" + config_name
config = configparser.ConfigParser()
config.read(config_file)
login = config["api"]["login"]
password = config["api"]["password"]
host_api = config["api"]["host"]
gare = config["default"]["gare"]
depart = config["default"]["depart"]


class TestGetTrainInfos(unittest.TestCase):

    @unittest.skip("not for tests")
    def validate_file(self, xsd, xml):
        try:
            xml_schema_document = etree.parse(xsd)
            xmlschema = etree.XMLSchema(xml_schema_document)
            xml_document = etree.fromstring(xml)
        except Exception:
            return False
        return xmlschema.validate(xml_document)

    def test_normal(self):
        value = get_train_infos(host_api, login, password, gare, depart)
        self.assertIn('<?xml version="1.0" encoding="UTF-8"?>', str(value))
        self.assertTrue(self.validate_file("api.xsd", value))

    def test_wrong_host(self):
        value = get_train_infos("1234", login, password, gare, depart)
        self.assertEqual("unknown url type: '1234/gare/" + gare + "/depart/" + depart + "/'", str(value))

    def test_wrong_host2(self):
        value = get_train_infos("http://1234", login, password, gare, depart)
        self.assertEqual('<urlopen error [Errno 65] No route to host>', str(value))

    def test_wrong_host_format_content(self):
        value = get_train_infos(1234, login, password, gare, depart)
        self.assertEqual("unknown url type: '1234/gare/" + gare + "/depart/" + depart + "/'", str(value))

    def test_wrong_login(self):
        value = get_train_infos(host_api, "login", password, gare, depart)
        self.assertEqual("HTTP Error 401: Unauthorized : b''", str(value))

    def test_wrong_password(self):
        value = get_train_infos(host_api, login, "password", gare, depart)
        self.assertEqual("HTTP Error 401: Unauthorized : b''", str(value))

    def test_wrong_gare(self):
        value = get_train_infos(host_api, login, password, "azerty", depart)
        self.assertEqual("HTTP Error 403: Forbidden : b''", str(value))

    def test_wrong_depart(self):
        value = get_train_infos(host_api, login, password, gare, "azerty")
        self.assertEqual("""b\'<?xml version="1.0" encoding="UTF-8"?>\\r\\n<passages gare="%s">\\r\\n</passages>\\r\\n'""" % gare, str(value))
        self.assertTrue(self.validate_file("api.xsd", value))

    def test_wrong_gare_number(self):
        value = get_train_infos(host_api, login, password, 12345, depart)
        self.assertEqual("HTTP Error 403: Forbidden : b''", str(value))

    def test_wrong_depart_number(self):
        value = get_train_infos(host_api, login, password, gare, 12345)
        self.assertEqual("HTTP Error 404: Not Found : b'Unknown arrival station [12345]'", str(value))

    def test__wrong_gare_and_depart_number(self):
        value = get_train_infos(host_api, login, password, 12345, 12345)
        self.assertEqual("HTTP Error 403: Forbidden : b''", str(value))


if __name__ == '__main__':
    unittest.main()
