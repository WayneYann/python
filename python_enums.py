"""
Example of using enums in Python 3.4 and higher
"""

from enum import Enum

class DevelopmentSettings(Enum):
    """example enum"""
    DEBUG = True
    DB = "dev"
    DOMAIN = '127.0.0.1:8000'

print(repr(DevelopmentSettings.DEBUG))
print(repr(DevelopmentSettings.DB))
print(repr(DevelopmentSettings.DOMAIN))

