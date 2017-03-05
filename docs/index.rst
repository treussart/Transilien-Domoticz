===================
Transilien-Domoticz
===================

:Last Reviewed: 2017-03-04

This guide is maintained on `github <https://github.com/matleses/Transilien-Domoticz/tree/master/docs>`_.


|Licence| |Code Health| |Coverage Status| |Documentation Status|

+------------------+--------------------+
| Status           | Operating system   |
+==================+====================+
| |Build Status|   | Linux x86\_64      |
+------------------+--------------------+

Hi! Do you need to get the schedule of the French suburban train lines, including with relevant alerts about last minute changes and updates? Well, you are in the right place now! Here is what you need to do:

If you have a SMS gateway, you can send SMS.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Requirements                                                                                                                                                   |
+================================================================================================================================================================+
| \* `Python3 <https://www.python.org/downloads/>`__.                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \* Domoticz.                                                                                                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \* Login for API Transilien `here <https://ressources.data.sncf.com/explore/dataset/api-temps-reel-transilien/>`__ (Requested by email, received in 3 days).   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \* (Optional) A cellphone with an IP fix, connected via WIFI (SMS Gateway).                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

|warning|

It's possible that for a train that has just been cancelled, the API may not display such a removed/cancelled train in the XML, and that no alert is generated.

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


.. toctree::
   :maxdepth: 2
   :caption: Usage

   installing

.. toctree::
   :maxdepth: 2
   :caption: Code

   code/index


