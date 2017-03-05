
Installation
------------

**Via PIP**

::

    pip install Transilien-Domoticz

Put your configuration in the file "conf.cfg".

::

    Located in : [Path]/site-packages/Transilien_Domoticz/conf.cfg

Edit the cron, example :

::

    crontab -e
Add :

::

    */5 06-09 * * 1-5 transilien --sendSMS --alert
    */5 * * * * transilien

**Via Git**

::

    git clone https://github.com/matleses/Transilien-Domoticz.git

Put your configuration in the file "conf.cfg".

::

    nano Transilien-Domoticz/conf.cfg

Edit the cron, example :

::

    crontab -e

Add :
::

    */5 06-09 * * 1-5 [Path]/Transilien-Domoticz/transilien.py --sendSMS --alert
    */5 * * * * [Path]/Transilien_Domoticz/transilien.py

**In Domoticz**

Create two Virtual Sensors in Domoticz :

- a subType Text for next trains.
- a subType Alert for the status of the trains.

**For sending SMS :**

Install `SMS
Gateway <https://play.google.com/store/apps/details?id=eu.apksoft.android.smsgateway&hl=fr>`__
(APK Soft) on your cellphone.

Enable :

- Listen for HTTP send SMS commands
- Prevent CPU sleep mode
- Start gateway automatically after phone boot

Tests
-----

Execution : (In advance, be sure to have filled the configuration file.)

::

    git clone https://github.com/matleses/Transilien-Domoticz.git
    cd Transilien-Domoticz
    ./tests.sh

Documentation
-------------

::

    virtualenv --python=python3.5 .venv
    source .venv/bin/activate
    git clone https://github.com/matleses/Transilien-Domoticz.git
    cd Transilien-Domoticz
    pip3 install -r requirements.txt
    cd docs
    make html

Usage
-----

::

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

.. |Licence| image:: https://img.shields.io/packagist/l/doctrine/orm.svg
.. |Code Health| image:: https://landscape.io/github/matleses/Transilien-Domoticz/master/landscape.svg?style=flat
   :target: https://landscape.io/github/matleses/Transilien-Domoticz/master
.. |Coverage Status| image:: https://coveralls.io/repos/github/matleses/Transilien-Domoticz/badge.svg?branch=master
   :target: https://coveralls.io/github/matleses/Transilien-Domoticz?branch=master
.. |Documentation Status| image:: https://readthedocs.org/projects/transilien-domoticz/badge/?version=latest
   :target: http://transilien-domoticz.readthedocs.io/?badge=latest
.. |Build Status| image:: https://travis-ci.org/matleses/Transilien-Domoticz.svg?branch=master
   :target: https://travis-ci.org/matleses/Transilien-Domoticz


