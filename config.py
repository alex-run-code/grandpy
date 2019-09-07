import os

GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
GOOGLE_API_KEY_MAPS = os.environ.get('GOOGLE_API_KEY_MAPS')
GOOGLE_API_KEY_GEOCODING = os.environ.get('GOOGLE_API_KEY_GEOCODING')

try:
    from config_local import *
except ImportError:
    pass
