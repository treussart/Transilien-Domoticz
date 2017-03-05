Installation
------------

**Via PIP**

::

    pip install Transilien-Domoticz

Put your configuration in the file “conf.cfg”.

::

    Located in : [Path]/site-packages/Transilien_Domoticz/conf.cfg


Test :
::

   transilien --v

If error = ImportError: No module named parse => Use Python3, not Python2.

For example :
::

   cd ~/
   virtualenv --python=python3.5 .venv
   source .venv/bin/activate
   pip install Transilien-Domoticz
   nano [path]/site-packages/Transilien_Domoticz/conf.cfg
   transilien --v

Edit the cron, example :

::

    crontab -e

Add :

::

    SHELL=/bin/bash
    */5 06-09 * * 1-5 source [/path/to/virtualenv/]bin/activate && transilien --sendSMS --alert
    */5 * * * * source [/path/to/virtualenv/]bin/activate && transilien

**Via Git**

::

    git clone https://github.com/matleses/Transilien-Domoticz.git

Put your configuration in the file “conf.cfg”.

::

    nano Transilien-Domoticz/Transilien_Domoticz/conf.cfg

Edit the cron, example :

::

    crontab -e

Add :

::

    */5 06-09 * * 1-5 [Path]/Transilien-Domoticz/Transilien_Domoticz/transilien.py --sendSMS --alert
    */5 * * * * [Path]/Transilien-Domoticz/Transilien_Domoticz/transilien.py

**In Domoticz**

Create two Virtual Sensors in Domoticz :

- a subType Text for next trains.
- a subType Alert for the status of the trains.

**For sending SMS :**

Install `SMS Gateway`_ (APK Soft) on your cellphone.

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

`Documentation`_
----------------

::

    git clone https://github.com/matleses/Transilien-Domoticz.git
    cd Transilien-Domoticz
    ./docs.sh

You can open with your Web browser the file : docs/_build/html/index.html


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


.. _SMS Gateway: https://play.google.com/store/apps/details?id=eu.apksoft.android.smsgateway&hl=fr
.. _Documentation: http://transilien-domoticz.readthedocs.io/