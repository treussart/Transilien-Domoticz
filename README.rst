Transilien-Domoticz
===================

|Licence| |Code Health| |Coverage Status| |Documentation Status|

+------------------+--------------------+
| Status           | Operating system   |
+==================+====================+
| |Build Status|   | Linux x86\_64      |
+------------------+--------------------+

Hi! Do you need to get the schedule of the French suburban train lines,
including with relevant alerts about last minute changes and updates?
Well, you are in the right place now! Here is what you need to do:

If you have a SMS gateway, you can send SMS.

|warning|

It’s possible that for a train that has just been cancelled, the API may
not display such a removed/cancelled train in the XML, and that no alert
is generated.

Requirements
------------

-  `Python3`_.
-  Domoticz.
-  Login for API Transilien `here`_ (Requested by email, received in 3
   days).
-  (Optional) A cellphone with an IP fix, connected via WIFI (`SMS Gateway`_).


Read the documentation on `http://transilien-domoticz.readthedocs.io/ <http://transilien-domoticz.readthedocs.io/>`_.


Usage :
-------

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


.. _Python3: https://www.python.org/downloads/
.. _here: https://ressources.data.sncf.com/explore/dataset/api-temps-reel-transilien/
.. _SMS Gateway: https://play.google.com/store/apps/details?id=eu.apksoft.android.smsgateway&hl=fr


.. |Licence| image:: https://img.shields.io/packagist/l/doctrine/orm.svg
.. |Code Health| image:: https://landscape.io/github/matleses/Transilien-Domoticz/master/landscape.svg?style=flat
   :target: https://landscape.io/github/matleses/Transilien-Domoticz/master
.. |Coverage Status| image:: https://coveralls.io/repos/github/matleses/Transilien-Domoticz/badge.svg?branch=master
   :target: https://coveralls.io/github/matleses/Transilien-Domoticz?branch=master
.. |Documentation Status| image:: https://readthedocs.org/projects/transilien-domoticz/badge/?version=latest
   :target: http://transilien-domoticz.readthedocs.io/?badge=latest
.. |Build Status| image:: https://travis-ci.org/matleses/Transilien-Domoticz.svg?branch=master
   :target: https://travis-ci.org/matleses/Transilien-Domoticz
.. |warning| image:: https://cdn2.iconfinder.com/data/icons/freecns-cumulus/32/519791-101_Warning-128.png
   :target: https://cdn2.iconfinder.com/data/icons/freecns-cumulus/32/519791-101_Warning-128.png