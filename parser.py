import requests

def getPlace(question):
    keywords = ['du', 'de', 'des', 'le', 'la', 'les']
    testsplit = question.split(' ')
    # print(testsplit)
    for item in testsplit:
        # print(item)
        if item in keywords or item.startswith("l'") or item.startswith("d'"):
            index = testsplit.index(item)
            if item in keywords:
                lieu = ' '.join(testsplit[index+1:])
            else:
                lieu = ' '.join(testsplit[index:])
            # print(lieu)
            return lieu
            break

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


