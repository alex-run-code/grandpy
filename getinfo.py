#!/usr/bin/python3

"""
    geosearch.py

    MediaWiki Action API Code Samples
    Demo of `Geosearch` module: Search for wiki pages nearby
    MIT license
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

latitude = str(37.7891838)
longitude = str(-122.4033522)
COORDS =  latitude + '|' + longitude


PARAMS = {
    'action':"query",
    'list':"geosearch",
    'gscoord': COORDS,
    'gsradius':10000,
    'gslimit':10,
    'format':"json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PLACES = DATA['query']['geosearch']

for place in PLACES:
    print(place['title'])