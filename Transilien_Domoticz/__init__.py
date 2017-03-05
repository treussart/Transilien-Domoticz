import platform
import sys
import warnings


if not (3) <= sys.version_info:
    sys.exit(
        'ERROR: Transilien-Domoticz requires Python 3, but found %s.' %
        platform.python_version())

warnings.filterwarnings('ignore', 'could not open display')

__version__ = '0.0.1'
