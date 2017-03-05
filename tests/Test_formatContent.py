#!/usr/bin/python3
# coding: utf8
import unittest
import os
import configparser
from Transilien_Domoticz.transilien import format_content

config_name = "conf.cfg"
config_file = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "/Transilien_Domoticz/" + config_name
config = configparser.ConfigParser()
config.read(config_file)
nbr_trains = 2
depart_name = config["default"]["departName"]


class TestFormatContent(unittest.TestCase):

    def test_normal(self):
        content = """<?xml version="1.0" encoding="UTF-8"?>\r\n<passages gare="87393405">\r\n<train><date mode="R">18/02/2017 17:07</date>\r\n<num>165546</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 17:37</date>\r\n<num>165650</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 18:07</date>\r\n<num>165554</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 18:37</date>\r\n<num>165658</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 19:07</date>\r\n<num>165562</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 19:37</date>\r\n<num>165666</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 20:07</date>\r\n<num>165570</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 20:37</date>\r\n<num>165674</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 21:07</date>\r\n<num>165578</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 21:37</date>\r\n<num>165682</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 22:07</date>\r\n<num>165586</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n</passages>\r\n"""
        values, state = format_content(nbr_trains, content, depart_name)
        self.assertEqual(depart_name + "_:_18/02/2017_17:07", values[0])
        self.assertEqual(depart_name + "_:_18/02/2017_17:37", values[1])
        self.assertFalse(state)
        self.assertEqual(len(values), 2)

    def test_normal_with_state(self):
        content = """<?xml version="1.0" encoding="UTF-8"?>\r\n<passages gare="87393405">\r\n<train><date mode="R">26/01/2017 08:38</date>\r\n<num>164674</num>\r\n<miss>PEMU</miss>\r\n<term>87391003</term>\r\n<etat>Retardé</etat>\r\n</train>\r\n<train><date mode="R">26/01/2017 08:52</date>\r\n<num>164576</num>\r\n<miss>PEGU</miss>\r\n<term>87391003</term>\r\n<etat>Supprimé</etat>\r\n</train>\r\n<train><date mode="R">26/01/2017 09:07</date>\r\n<num>164578</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n<etat>Supprimé</etat>\r\n</train>\r\n<train><date mode="R">26/01/2017 09:37</date>\r\n<num>164682</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n</passages>"""
        values, state = format_content(nbr_trains, content, depart_name)
        self.assertEqual(depart_name + "_:_26/01/2017_08:38_Retardé", values[0])
        self.assertEqual(depart_name + "_:_26/01/2017_08:52_Supprimé", values[1])
        self.assertTrue(state)

    def test_no_content(self):
        content = ""
        values, state = format_content(nbr_trains, content, depart_name)
        self.assertIn("ParseError : no element found:", values[0])
        self.assertFalse(state)

    def test_wrong_content(self):
        content = '<?xml version="1.0" encoding="UTF-8"?><passages gare="87393405"><train><date mode="R">18/02/2017 14:37</date><num>165626</num><miss></passages>'
        values, state = format_content(nbr_trains, content, depart_name)
        self.assertIn("ParseError : mismatched tag:", values[0])
        self.assertFalse(state)

    def test_wrong_content2(self):
        content = """<?xml version="1.0" encoding="UTF-8"?>\r\n<train><date mode="R">26/01/2017 08:38</date>\r\n<num>164674</num>\r\n<miss>PEMU</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">26/01/2017 08:52</date>\r\n<num>164576</num>\r\n<miss>PEGU</miss>\r\n<term>87391003</term>\r\n<etat>Supprimé</etat>\r\n<train><date mode="R">26/01/2017 09:07</date>\r\n<num>164578</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n<etat>Supprimé</etat>\r\n</train>\r\n<train><date mode="R">26/01/2017 09:37</date>\r\n<num>164682</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n</passages>"""
        values, state = format_content(nbr_trains, content, depart_name)
        self.assertIn("ParseError : junk after document element:", values[0])
        self.assertFalse(state)

    def test_no_train(self):
        content = """<?xml version="1.0" encoding="UTF-8"?>\r\n<passages gare="87393405">\r\n</passages>"""
        values, state = format_content(nbr_trains, content, depart_name)
        self.assertEqual('No train', values[0])
        self.assertTrue(state)

    def test_first_normal_second_with_state(self):
        content = """<?xml version="1.0" encoding="UTF-8"?>
    <passages gare="87393405">
    <train><date mode="R">26/01/2017 08:38</date>
    <num>164674</num>
    <miss>PEMU</miss>
    <term>87391003</term>
    </train>
    <train><date mode="R">26/01/2017 08:52</date>
    <num>164576</num>
    <miss>PEGU</miss>
    <term>87391003</term>
    <etat>Supprimé</etat>
    </train>
    <train><date mode="R">26/01/2017 09:07</date>
    <num>164578</num>
    <miss>POGI</miss>
    <term>87391003</term>
    <etat>Supprimé</etat>
    </train>
    <train><date mode="R">26/01/2017 09:37</date>
    <num>164682</num>
    <miss>POMI</miss>
    <term>87391003</term>
    </train>
    </passages>"""
        values, state = format_content(nbr_trains, content, depart_name)
        self.assertEqual(depart_name + "_:_26/01/2017_08:38", values[0])
        self.assertEqual(depart_name + "_:_26/01/2017_08:52_Supprimé", values[1])
        self.assertTrue(state)

    def test_number_trains_to_zero(self):
        content = """<?xml version="1.0" encoding="UTF-8"?>\r\n<passages gare="87393405">\r\n<train><date mode="R">18/02/2017 17:07</date>\r\n<num>165546</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 17:37</date>\r\n<num>165650</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 18:07</date>\r\n<num>165554</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 18:37</date>\r\n<num>165658</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 19:07</date>\r\n<num>165562</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 19:37</date>\r\n<num>165666</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 20:07</date>\r\n<num>165570</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 20:37</date>\r\n<num>165674</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 21:07</date>\r\n<num>165578</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 21:37</date>\r\n<num>165682</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 22:07</date>\r\n<num>165586</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n</passages>\r\n"""
        values, state = format_content(0, content, depart_name)
        self.assertEqual(len(values), 1)
        self.assertEqual(depart_name + "_:_18/02/2017_17:07", values[0])
        self.assertFalse(state)

    def test_number_trains_to_one(self):
        content = """<?xml version="1.0" encoding="UTF-8"?>\r\n<passages gare="87393405">\r\n<train><date mode="R">18/02/2017 17:07</date>\r\n<num>165546</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 17:37</date>\r\n<num>165650</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 18:07</date>\r\n<num>165554</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 18:37</date>\r\n<num>165658</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 19:07</date>\r\n<num>165562</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 19:37</date>\r\n<num>165666</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 20:07</date>\r\n<num>165570</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 20:37</date>\r\n<num>165674</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 21:07</date>\r\n<num>165578</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 21:37</date>\r\n<num>165682</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 22:07</date>\r\n<num>165586</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n</passages>\r\n"""
        values, state = format_content(1, content, depart_name)
        self.assertEqual(len(values), 1)
        self.assertEqual(depart_name + "_:_18/02/2017_17:07", values[0])
        self.assertFalse(state)

    def test_number_trains_too_much(self):
        content = """<?xml version="1.0" encoding="UTF-8"?>\r\n<passages gare="87393405">\r\n<train><date mode="R">18/02/2017 17:07</date>\r\n<num>165546</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 17:37</date>\r\n<num>165650</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 18:07</date>\r\n<num>165554</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 18:37</date>\r\n<num>165658</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 19:07</date>\r\n<num>165562</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 19:37</date>\r\n<num>165666</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 20:07</date>\r\n<num>165570</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 20:37</date>\r\n<num>165674</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 21:07</date>\r\n<num>165578</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 21:37</date>\r\n<num>165682</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 22:07</date>\r\n<num>165586</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n</passages>\r\n"""
        values, state = format_content(30, content, depart_name)
        self.assertEqual(len(values), 11)
        self.assertEqual(depart_name + "_:_18/02/2017_17:07", values[0])
        self.assertFalse(state)

    def test_special_chars_in_depart_name(self):
        content = """<?xml version="1.0" encoding="UTF-8"?>\r\n<passages gare="87393405">\r\n<train><date mode="R">18/02/2017 17:07</date>\r\n<num>165546</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 17:37</date>\r\n<num>165650</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 18:07</date>\r\n<num>165554</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 18:37</date>\r\n<num>165658</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 19:07</date>\r\n<num>165562</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 19:37</date>\r\n<num>165666</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 20:07</date>\r\n<num>165570</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 20:37</date>\r\n<num>165674</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 21:07</date>\r\n<num>165578</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 21:37</date>\r\n<num>165682</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 22:07</date>\r\n<num>165586</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n</passages>\r\n"""
        values, state = format_content(nbr_trains, content, '%-&#@^*¨')
        self.assertEqual('%-&#@^*¨' + "_:_18/02/2017_17:07", values[0])
        self.assertFalse(state)

    def test_number_in_depart_name(self):
        content = """<?xml version="1.0" encoding="UTF-8"?>\r\n<passages gare="87393405">\r\n<train><date mode="R">18/02/2017 17:07</date>\r\n<num>165546</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 17:37</date>\r\n<num>165650</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 18:07</date>\r\n<num>165554</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 18:37</date>\r\n<num>165658</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 19:07</date>\r\n<num>165562</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 19:37</date>\r\n<num>165666</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 20:07</date>\r\n<num>165570</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 20:37</date>\r\n<num>165674</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 21:07</date>\r\n<num>165578</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 21:37</date>\r\n<num>165682</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 22:07</date>\r\n<num>165586</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n</passages>\r\n"""
        values, state = format_content(nbr_trains, content, 1234)
        self.assertEqual('1234' + "_:_18/02/2017_17:07", values[0])
        self.assertFalse(state)

    def test_number_in_content(self):
        values, state = format_content(nbr_trains, 1234, depart_name)
        self.assertIn("Problem with content , can't be a int", values[0])
        self.assertFalse(state)

    def test_number_trains_to_string(self):
        content = """<?xml version="1.0" encoding="UTF-8"?>\r\n<passages gare="87393405">\r\n<train><date mode="R">18/02/2017 17:07</date>\r\n<num>165546</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 17:37</date>\r\n<num>165650</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 18:07</date>\r\n<num>165554</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 18:37</date>\r\n<num>165658</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 19:07</date>\r\n<num>165562</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 19:37</date>\r\n<num>165666</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 20:07</date>\r\n<num>165570</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 20:37</date>\r\n<num>165674</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 21:07</date>\r\n<num>165578</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 21:37</date>\r\n<num>165682</num>\r\n<miss>POMI</miss>\r\n<term>87391003</term>\r\n</train>\r\n<train><date mode="R">18/02/2017 22:07</date>\r\n<num>165586</num>\r\n<miss>POGI</miss>\r\n<term>87391003</term>\r\n</train>\r\n</passages>\r\n"""
        values, state = format_content('test', content, depart_name)
        self.assertEqual(depart_name + "_:_18/02/2017_17:07", values[0])
        self.assertFalse(state)


if __name__ == '__main__':
    unittest.main()
