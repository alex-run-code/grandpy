import requests
from bs4 import BeautifulSoup


# get Page id from Coord
def getPage(latitude, longitude):
    """ return wikipedia pageid from latitude and longitude """
    URL = "https://fr.wikipedia.org/w/api.php"
    COORDS = str(latitude) + '|' + str(longitude)
    PARAMS = {
        'action': "query",
        'list': "geosearch",
        'gscoord': COORDS,
        'gsradius': 10000,
        'gslimit': 10,
        'format': "json",
        'prop': 'info',
    }
    response = requests.get(url=URL, params=PARAMS)
    json_response = response.json()
    PLACES = json_response['query']['geosearch']
    return(PLACES[0]['pageid'])


# getpageid from place
def getPageidFromPlace(place):
    """ return wikipedia pageid from the name of the place """
    URL = "https://fr.wikipedia.org/w/api.php"
    PARAMS = {
        'action': "query",
        'list': "search",
        'srsearch': place,
        'format': "json",
        'prop': 'info',
    }
    response = requests.get(url=URL, params=PARAMS)
    json_response = response.json()
    pageid = json_response['query']['search'][0]['pageid']
    return(pageid)


def getStory(pageid):
    """ parse the html of the wikipedia page based on pageid
    return the begining of the first section
    """
    URL = "https://fr.wikipedia.org/w/api.php"
    PARAMS = {
        'action': "parse",
        'pageid': pageid,
        'format': "json",
    }
    response = requests.get(url=URL, params=PARAMS)
    json_response = response.json()
    html = json_response['parse']['text']['*']
    soup = BeautifulSoup(html, "html.parser")
    headlines = soup.findAll("span", {"class": "mw-headline"})
    afterFirstHeadline = headlines[0].find_all_next('p')
    cleanStory = afterFirstHeadline[0].get_text()
    cleanStory = cleanStory.replace('\xa0', ' ')
    cleanStory = cleanStory.replace('\n', '')
    return(cleanStory)


def getStoryExtract(pageid):
    """ extract the begining of the introduction of a wikipedia page
        based on page id
    """
    URL = "https://fr.wikipedia.org/w/api.php"
    PARAMS = {
        'action': "query",
        'pageids': pageid,
        'format': "json",
        'prop': 'extracts',
        'explaintext': 1,
        'exsentences': 2,
    }
    response = requests.get(url=URL, params=PARAMS)
    json_response = response.json()
    story = json_response['query']['pages'][str(pageid)]['extract']
    return(story)
