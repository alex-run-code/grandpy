import requests
import config


def getLocationInfos(place):
    """ return adress, latitude and longitue of place from Google API """
    URL = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?'
    PARAMS = {
        'key': config.GOOGLE_API_KEY_GEOCODING,
        'input': place,
        'inputtype': 'textquery',
        'fields': 'formatted_address,geometry',
        'locationbias': 'circle:1000@42.28,2.66',
    }
    response = requests.get(url=URL, params=PARAMS)
    json_response = response.json()
    address = json_response['candidates'][0]['formatted_address']
    latitude = json_response['candidates'][0]['geometry']['location']['lat']
    longitude = json_response['candidates'][0]['geometry']['location']['lng']
    locationInfos = {
        'address': address,
        'latitude': latitude,
        'longitude': longitude,
    }
    return locationInfos
