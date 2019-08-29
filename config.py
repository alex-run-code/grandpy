import os

GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')

try:
    from config_local import *
except ImportError:
    pass