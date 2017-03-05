#!/usr/bin/python3
# coding: utf8
import unittest
import json
import os
import configparser
from transilien import send_alert_to_domoticz, format_content

config_name = "conf.cfg"
config_file = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "/" + config_name
config = configparser.ConfigParser()
config.read(config_file)
nbr_trains = 2
host = config["domoticz"]["host"]
port = config["domoticz"].getint('port')
idx_alert = config["domoticz"]["idx_alert"]
depart_name = config["default"]["departName"]
level = config["domoticz"]["level"]
gare_name = config["default"]["gareName"]


class TestSendAlertToDomoticz(unittest.TestCase):

    def test_normal(self):
        content = """<?xml version="1.0" encoding="UTF-8"?>\r\n<passages gare="87393405">\r\n<train><date mode="R">26/01/2017 08:38</date>\r\n<num>164674</num>\r\n<miss>PEMU</miss>\r\n<term>87391003</term>\r\n<etat>Retardé</etat>\r\n</train>\r\n<train><date mode="R">26/01/2017 08:52</date>\r\n<num>164576</num>\r\n<miss>PEGU</miss>\r\n<term>87391003</term>\r\n<etat>Supprimé</etat>\r\n</train>\r\n<train><date mode="R">26/01/2017 09:07</date>\r\n<num>164578</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n<etat>Supprimé</etat>\r\n</train>\r\n<train><date mode="R">26/01/2017 09:37</date>\r\n<num>164682</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n</passages>"""
        values, state = format_content(nbr_trains, content, depart_name)
        value = send_alert_to_domoticz(host, port, idx_alert, values, level)
        try:
            json.loads(str(value.decode("utf-8")))
        except ValueError as e:
            self.fail('invalid json: ' + e)
        self.assertEqual("""{\n   "status" : "OK",\n   "title" : "Update Device"\n}\n""", value.decode("utf-8"))

    def test_level(self):
        content = """<?xml version="1.0" encoding="UTF-8"?>\r\n<passages gare="87393405">\r\n<train><date mode="R">26/01/2017 08:38</date>\r\n<num>164674</num>\r\n<miss>PEMU</miss>\r\n<term>87391003</term>\r\n<etat>Retardé</etat>\r\n</train>\r\n<train><date mode="R">26/01/2017 08:52</date>\r\n<num>164576</num>\r\n<miss>PEGU</miss>\r\n<term>87391003</term>\r\n<etat>Supprimé</etat>\r\n</train>\r\n<train><date mode="R">26/01/2017 09:07</date>\r\n<num>164578</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n<etat>Supprimé</etat>\r\n</train>\r\n<train><date mode="R">26/01/2017 09:37</date>\r\n<num>164682</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n</passages>"""
        values, state = format_content(nbr_trains, content, depart_name)
        value = send_alert_to_domoticz(host, port, idx_alert, values, -5)
        try:
            json.loads(str(value.decode("utf-8")))
        except ValueError as e:
            self.fail('invalid json: ' + e)
        self.assertEqual("""{\n   "status" : "OK",\n   "title" : "Update Device"\n}\n""", value.decode("utf-8"))
        value = send_alert_to_domoticz(host, port, idx_alert, values, "rte")
        try:
            json.loads(str(value.decode("utf-8")))
        except ValueError as e:
            self.fail('invalid json: ' + e)
        self.assertEqual("""{\n   "status" : "OK",\n   "title" : "Update Device"\n}\n""", value.decode("utf-8"))
        value = send_alert_to_domoticz(host, port, idx_alert, values, 0)
        try:
            json.loads(str(value.decode("utf-8")))
        except ValueError as e:
            self.fail('invalid json: ' + e)
        self.assertEqual("""{\n   "status" : "OK",\n   "title" : "Update Device"\n}\n""", value.decode("utf-8"))
        value = send_alert_to_domoticz(host, port, idx_alert, values, 40)
        try:
            json.loads(str(value.decode("utf-8")))
        except ValueError as e:
            self.fail('invalid json: ' + e)
        self.assertEqual("""{\n   "status" : "OK",\n   "title" : "Update Device"\n}\n""", value.decode("utf-8"))

    def test_idx(self):
        content = """<?xml version="1.0" encoding="UTF-8"?>\r\n<passages gare="87393405">\r\n<train><date mode="R">26/01/2017 08:38</date>\r\n<num>164674</num>\r\n<miss>PEMU</miss>\r\n<term>87391003</term>\r\n<etat>Retardé</etat>\r\n</train>\r\n<train><date mode="R">26/01/2017 08:52</date>\r\n<num>164576</num>\r\n<miss>PEGU</miss>\r\n<term>87391003</term>\r\n<etat>Supprimé</etat>\r\n</train>\r\n<train><date mode="R">26/01/2017 09:07</date>\r\n<num>164578</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n<etat>Supprimé</etat>\r\n</train>\r\n<train><date mode="R">26/01/2017 09:37</date>\r\n<num>164682</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n</passages>"""
        values, state = format_content(nbr_trains, content, depart_name)
        value = send_alert_to_domoticz(host, port, 2900, values, level)
        try:
            json.loads(str(value.decode("utf-8")))
        except ValueError as e:
            self.fail('invalid json: ' + e)
        self.assertEqual("""{\n   "status" : "ERR"\n}\n""", value.decode("utf-8"))
        value = send_alert_to_domoticz(host, port, 'azerty', values, level)
        try:
            json.loads(str(value.decode("utf-8")))
        except ValueError as e:
            self.fail('invalid json: ' + e)
        self.assertEqual("""{\n   "status" : "ERR"\n}\n""", value.decode("utf-8"))

    def test_port(self):
        content = """<?xml version="1.0" encoding="UTF-8"?>\r\n<passages gare="87393405">\r\n<train><date mode="R">26/01/2017 08:38</date>\r\n<num>164674</num>\r\n<miss>PEMU</miss>\r\n<term>87391003</term>\r\n<etat>Retardé</etat>\r\n</train>\r\n<train><date mode="R">26/01/2017 08:52</date>\r\n<num>164576</num>\r\n<miss>PEGU</miss>\r\n<term>87391003</term>\r\n<etat>Supprimé</etat>\r\n</train>\r\n<train><date mode="R">26/01/2017 09:07</date>\r\n<num>164578</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n<etat>Supprimé</etat>\r\n</train>\r\n<train><date mode="R">26/01/2017 09:37</date>\r\n<num>164682</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n</passages>"""
        values, state = format_content(nbr_trains, content, depart_name)
        value = send_alert_to_domoticz(host, '12300', idx_alert, values, level)
        self.assertEqual('Failed to reach a serverReason: [Errno 61] Connection refused', value)
        value = send_alert_to_domoticz(host, 'azerty', idx_alert, values, level)
        self.assertEqual('Problem with port number', value)
        value = send_alert_to_domoticz(host, 1234, idx_alert, values, level)
        self.assertEqual('Failed to reach a serverReason: [Errno 61] Connection refused', value)

    def test_host(self):
        content = """<?xml version="1.0" encoding="UTF-8"?>\r\n<passages gare="87393405">\r\n<train><date mode="R">26/01/2017 08:38</date>\r\n<num>164674</num>\r\n<miss>PEMU</miss>\r\n<term>87391003</term>\r\n<etat>Retardé</etat>\r\n</train>\r\n<train><date mode="R">26/01/2017 08:52</date>\r\n<num>164576</num>\r\n<miss>PEGU</miss>\r\n<term>87391003</term>\r\n<etat>Supprimé</etat>\r\n</train>\r\n<train><date mode="R">26/01/2017 09:07</date>\r\n<num>164578</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n<etat>Supprimé</etat>\r\n</train>\r\n<train><date mode="R">26/01/2017 09:37</date>\r\n<num>164682</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n</passages>"""
        values, state = format_content(nbr_trains, content, depart_name)
        value = send_alert_to_domoticz(1234, port, idx_alert, values, level)
        self.assertEqual('Failed to reach a serverReason: [Errno 65] No route to host', value)
        value = send_alert_to_domoticz('1234', port, idx_alert, values, level)
        self.assertEqual('Failed to reach a serverReason: [Errno 65] No route to host', value)
        value = send_alert_to_domoticz('1.1.0.0', port, idx_alert, values, level)
        self.assertEqual('Failed to reach a serverReason: [Errno 60] Operation timed out', value)

    def test_values(self):
        value = send_alert_to_domoticz(host, port, idx_alert, None, level)
        self.assertEqual('Problem with values: Empty', value)
        value = send_alert_to_domoticz(host, port, idx_alert, "", level)
        self.assertEqual('Problem with values: Empty', value)
        value = send_alert_to_domoticz(host, port, idx_alert, "AZERTY", level)
        self.assertEqual('Problem with values: need to be a list or a tuple', value)
        value = send_alert_to_domoticz(host, port, idx_alert, 1234, level)
        self.assertEqual('Problem with values: need to be a list or a tuple', value)

    def test_values_no_train(self):
        content = """<?xml version="1.0" encoding="UTF-8"?>\r\n<passages gare="87393405">\r\n</passages>"""
        values = format_content(nbr_trains, content, depart_name)[0] + format_content(nbr_trains, content, gare_name)[0]
        value = send_alert_to_domoticz(host, port, idx_alert, values, level)
        try:
            json.loads(str(value.decode("utf-8")))
        except ValueError as e:
            self.fail('invalid json: ' + e)
        self.assertEqual("""{\n   "status" : "OK",\n   "title" : "Update Device"\n}\n""", value.decode("utf-8"))

    def test_wrong_values(self):
        content = '<?xml version="1.0" encoding="UTF-8"?><passages gare="87393405"><train><date mode="R">18/02/2017 14:37</date><num>165626</num><miss></passages>'
        values = format_content(nbr_trains, content, depart_name)[0] + format_content(nbr_trains, content, gare_name)[0]
        value = send_alert_to_domoticz(host, port, idx_alert, values, level)
        try:
            json.loads(str(value.decode("utf-8")))
        except ValueError as e:
            self.fail('invalid json: ' + e)
        self.assertEqual("""{\n   "status" : "OK",\n   "title" : "Update Device"\n}\n""", value.decode("utf-8"))


if __name__ == '__main__':
    unittest.main()
