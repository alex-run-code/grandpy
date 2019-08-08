import requests
import re
from bs4 import BeautifulSoup


def getPlace(question):
    keywords = ['du', 'de', 'des', 'le', 'la', 'les']
    q1 = re.sub('[!?]','', question)
    q2 = re.sub("(l')",'la ', q1)
    q3 = re.sub("(d')",'de ', q2)
    q4 = re.sub("(adresse)",'', q3)
    splitedQuestion = q4.split(' ')
    if (any(elem in splitedQuestion for elem in keywords)):
        for item in splitedQuestion:
            if item in keywords:
                index = splitedQuestion.index(item)
                lieu = ' '.join(splitedQuestion[index+1:])
                return lieu.strip()
    else: 
        lieu = ' '.join(splitedQuestion[0:])
        return lieu.strip()

def getLocationInfos(place):
    URL = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?'
    PARAMS = {
        'key': 'AIzaSyBkFah8q7LN6tfLPp04R1HUin3AKex80w4',
        'input' : place,
        'inputtype': 'textquery',
        'fields' : 'formatted_address,geometry'
    }
    response = requests.get(url=URL,params=PARAMS)
    json_response = response.json()
    # {'candidates': [{'formatted_address': 'Champ de Mars, 5 Avenue Anatole France, 75007 Paris, Franţa', 'geometry': {'location': {'lat': 48.85837009999999, 'lng': 2.2944813}, 'viewport': {'northeast': {'lat': 48.85974697989273, 'lng': 2.29610765}, 'southwest': {'lat': 48.85704732010728, 'lng': 2.29251745}}}}], 'status': 'OK'}
    address = json_response['candidates'][0]['formatted_address']
    latitude = json_response['candidates'][0]['geometry']['location']['lat']
    longitude = json_response['candidates'][0]['geometry']['location']['lng']
    locationInfos = {
        'address' : address,
        'latitude' : latitude,
        'longitude' : longitude,
    }
    return locationInfos

def getPage(latitude, longitude):
    URL = "https://fr.wikipedia.org/w/api.php"
    COORDS =  str(latitude) + '|' + str(longitude)
    PARAMS = {
    'action':"query",
    'list':"geosearch",
    'gscoord': COORDS,
    'gsradius':10000,
    'gslimit':10,
    'format':"json"
}
    response = requests.get(url=URL, params=PARAMS)
    json_response = response.json()
    PLACES = json_response['query']['geosearch']
    return(PLACES[0]['pageid'])

def getStory(pageid):
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
    cleanStory = cleanStory.replace('\xa0',' ')
    cleanStory = cleanStory.replace('\n','')
    return(cleanStory)

def getAllInfos(question):
    place = getPlace(question)
    address = getLocationInfos(place)['address']
    latitude = getLocationInfos(place)['latitude']
    longitude = getLocationInfos(place)['longitude']
    pageid = getPage(latitude, longitude)
    story = getStory(pageid)
    allInfos = {
        'place' : place,
        'address' : address,
        'latitude' : latitude,
        'longitude' : longitude,
        'pageid' : pageid,
        'story' : story,
    }
    for item in allInfos:
        print(allInfos[item])

getAllInfos('Ou se trouve la Tour Eiffel')
