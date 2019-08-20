from grandpyapp import parserino
import requests


class LocInfoResponse:

    @staticmethod
    def json():
        results = {
            'candidates': [{
                'formatted_address': 'Champ de Mars, 5 Avenue Anatole France, 75007 Paris, Franţa', 
                'geometry': {
                    'location': {
                        'lat': 48.85837009999999, 
                        'lng': 2.2944813}, 'viewport': {
                            'northeast': {
                                'lat': 48.85974697989273, 
                                'lng': 2.29610765
                                }, 
                            'southwest': {
                                'lat': 48.85704732010728, 
                                'lng': 2.29251745
                                }
                            }
                        }
                    }], 
                'status': 'OK'
                }
        return results


def test_getLocationInfos(monkeypatch):

    def mock_get(*arg, **kwargs):
        return LocInfoResponse

    monkeypatch.setattr(requests, "get", mock_get)
    goodAnswer = {
        'address': 'Champ de Mars, 5 Avenue Anatole France, 75007 Paris, Franţa', 
        'latitude': 48.85837009999999, 
        'longitude': 2.29448139999, 
        'longitude': 2.2944813
        }
    assert parserino.getLocationInfos('Tour Eiffel') == goodAnswer


class PageResponse:

    @staticmethod
    def json():
        results = {
                    'batchcomplete': '', 
                    'query': {
                        'geosearch': [{
                            'pageid': 1359783, 
                            'ns': 0, 
                            'title': 'Tour Eiffel', 
                            'lat': 48.858296, 
                            'lon': 2.294479, 
                            'dist': 8.2, 
                            'primary': ''
                            }]
                        } 
                    }      
        return results

def test_getPage(monkeypatch):

    def mock_get(*arg, **kwargs):
        return PageResponse 

    monkeypatch.setattr(requests, 'get', mock_get)
    assert parserino.getPage(48.85837009999999, 2.29448139999) == 1359783

class StoryResponse:

    @staticmethod
    def json():
        f= open("fakewiki.html","r", encoding="utf8" )
        fakepage = f.read()
        f.close()
        results = {
                    'parse': {
                        'text': {
                            '*': fakepage, 
                            }
                        } 
                    }      
        return results


def test_getStory(monkeypatch):

    def mock_get(*arg, **kwargs):
        return StoryResponse 

    monkeypatch.setattr(requests, 'get', mock_get)
    goodAnswer = (
    "Contestée par certains à l'origine, la tour Eiffel fut d'abord, "
    "à l'occasion de l'exposition universelle de 1889, la vitrine du savoir-faire "
    "technique français. Plébiscitée par le public dès sa présentation à l'exposition, "
    "elle a accueilli plus de 200 millions de visiteurs depuis son inauguration[o 2]. "
    "Sa taille exceptionnelle et sa silhouette immédiatement reconnaissable en ont "
    "fait un emblème de Paris.")

    assert parserino.getStory(685616) == goodAnswer

class PageidfromplaceResponse:

    @staticmethod
    def json():
        results = {
                    'batchcomplete': '', 
                    'query': {
                        'search': [{
                            'pageid': 1359783, 
                            'ns': 0, 
                            'title': 'Tour Eiffel', 
                            'lat': 48.858296, 
                            'lon': 2.294479, 
                            'dist': 8.2, 
                            'primary': ''
                            }]
                        } 
                    }      
        return results

def test_getPageidFromPlace(monkeypatch):

    def mock_get(*arg, **kwargs):
        return PageidfromplaceResponse 

    monkeypatch.setattr(requests, 'get', mock_get)
    assert parserino.getPageidFromPlace('tour eiffel') == 1359783