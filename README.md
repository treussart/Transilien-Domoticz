Transilien-Domoticz
===================

![Licence](https://img.shields.io/packagist/l/doctrine/orm.svg)
[![Code Health](https://landscape.io/github/matleses/transilien-python/master/landscape.svg?style=flat)](https://landscape.io/github/matleses/transilien-python/master)
[![Coverage Status](https://coveralls.io/repos/github/matleses/transilien-python/badge.png?branch=master)](https://coveralls.io/github/matleses/transilien-python?branch=master)

Status | Operating system
------------ | -------------
![Build Status](https://travis-ci.org/matleses/transilien-python.png?branch=master "Linux Build Status") | Linux x86_64




Hey! You want to get the french train schedules and its states, you are in the good place !

If like me, you use Domoticz and have a cellphone for send SMS or not :

:warning: It's possible that for a deleted train, the API not return the deleted train in the XML , and no alert is emitted.

Requirements
-------------
* [Python3][2].
* Domoticz.
* Login for API Transilien [here][1] (Requested by email, received in 3 days).
* (Optional) A cellphone with an IP fix, connected via WIFI.

Installation
-------------

Create two Virtual Sensors in Domoticz :
* a subType Text for next trains.
* a subType Alert for the state of the trains.


Put your configuration in the file "conf.cfg".

Edit the cron, example :

    crontab -e
Add :

    */5 06-09 * * 1-5 python3 ~/transilien-python/transilien.py --sendSMS --alert
    */5 * * * * python3 ~/transilien-python/transilien.py

**For send SMS :**

Install [SMS Gateway][3] (APK Soft) on your cellphone.

Enable : 
* Listen for HTTP send SMS commands 
* Prevent CPU sleep mode 
* Start gateway automatically after phone boot 

[1]: https://ressources.data.sncf.com/explore/dataset/api-temps-reel-transilien/
[2]: https://www.python.org/downloads/
[3]: https://play.google.com/store/apps/details?id=eu.apksoft.android.smsgateway&hl=fr

Tests
-------------
    
Execution :  (In advance, be sure to have filled the configuration file.)

    ./tests.sh
    
Documentation
-------------

    virtualenv --python=python3.5 .venv
    source .venv/bin/activate
    pip3 install -r requirements.txt
    cd docs
    make html

Usage :
-------------

    usage: transilien.py [-h] [--nbrTrains NBRTRAINS] [--depart DEPART]
                          [--gare GARE] [--sendSMS] [--departName DEPARTNAME]
                          [--gareName GARENAME] [--alert] [--v]

     optional arguments:
       -h, --help            show this help message and exit
       --nbrTrains NBRTRAINS
                             the number of trains to check
       --depart DEPART       the departure's station number
       --gare GARE           the arrival's station number
       --sendSMS             send a SMS
       --departName DEPARTNAME
                             the departure's station name
       --gareName GARENAME   the arrival's station name
       --alert               check if trains have state
       --v                   verbose
