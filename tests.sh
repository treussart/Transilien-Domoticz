#!/usr/bin/env bash

virtualenv --python=python3.5 .venv
source .venv/bin/activate
pip3 install -r test-requirements.txt
export PYTHONPATH=$PYTHONPATH:$(pwd)

coverage3 erase
coverage3 run tests/Test_formatContent.py
coverage3 run -a tests/Test_validNumber.py
coverage3 run -a tests/Test_getTrainInfos.py
coverage3 run -a tests/Test_sendAlertToDomoticz.py
coverage3 run -a tests/Test_sendSms.py
coverage3 run -a tests/Test_sendTextToDomoticz.py

coverage3 run -a Transilien_Domoticz/transilien.py
coverage3 run -a Transilien_Domoticz/transilien.py --sendSMS
coverage3 run -a Transilien_Domoticz/transilien.py --sendSMS --v
coverage3 run -a Transilien_Domoticz/transilien.py --alert
coverage3 run -a Transilien_Domoticz/transilien.py --alert --sendSMS
coverage3 run -a Transilien_Domoticz/transilien.py --alert --sendSMS --v

coverage3 report -i

coverage3 html

#coveralls --output=coverage.json
#coveralls --merge=coverage.json

flake8 .
