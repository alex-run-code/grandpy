import requests
import re

def getPlace(question):
    keywords = ['du', 'de', 'des', 'le', 'la', 'les']
    q1 = re.sub('[!?]','', question)
    q2 = re.sub("(l')",'la ', q1)
    q3 = re.sub("(d')",'de ', q2)
    splitedQuestion = q3.split(' ')
    if (any(elem in splitedQuestion for elem in keywords)):
        for item in splitedQuestion:
            if item in keywords:
                index = splitedQuestion.index(item)
                lieu = ' '.join(splitedQuestion[index+1:])
                return lieu.strip()
    else: 
        lieu = ' '.join(splitedQuestion[0:])
        return lieu.strip()



def getInfos(latitude, longitude):
    S = requests.Session()

    URL = "https://en.wikipedia.org/w/api.php"

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
    return (PLACES[0]['title'])


