import re
import google_api
import mediawiki_api

def getPlace(question):
    keywords = ['du', 'de', 'des', 'le', 'la', 'les']
    q1 = re.sub('[!?]', '', question)
    q2 = re.sub("(l')", 'la ', q1)
    q3 = re.sub("(d')", 'de ', q2)
    q4 = re.sub("(adresse)", '', q3)
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


def getAllInfos(question):
    place = getPlace(question)
    locationInfos = google_api.getLocationInfos(place)
    # pageid = getPage(latitude, longitude)
    pageid = mediawiki_api.getPageidFromPlace(place)
    story = mediawiki_api.getStoryExtract(pageid)
    link = 'https://fr.wikipedia.org/?curid=' + str(pageid)
    allInfos = {
        'place': place,
        'address': locationInfos['address'],
        'latitude': locationInfos['latitude'],
        'longitude': locationInfos['longitude'],
        'pageid': pageid,
        'story': story,
        'link': link,
    }
    return(allInfos)