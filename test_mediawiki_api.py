import requests
import mediawiki_api


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
    """ test the function getStory """

    def mock_get(*arg, **kwargs):
        """ return the results from method
        json of class PageResponse
        """
        return PageResponse

    monkeypatch.setattr(requests, 'get', mock_get)
    assert mediawiki_api.getPage(48.85837009999999, 2.29448139999) == 1359783


class StoryResponse:

    @staticmethod
    def json():
        f = open("fakewiki.html", "r", encoding="utf8")
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
    """ test the function getStory """

    def mock_get(*arg, **kwargs):
        """ return the results from method
        json of class StoryResponse
        """
        return StoryResponse

    monkeypatch.setattr(requests, 'get', mock_get)
    goodAnswer = (
        "Contestée par certains à l'origine, la tour Eiffel "
        "fut d'abord, à l'occasion de l'exposition universelle "
        "de 1889, la vitrine du savoir-faire technique français. "
        "Plébiscitée par le public dès sa présentation à l'exposition, "
        "elle a accueilli plus de 200 millions de visiteurs "
        "depuis son inauguration[o 2]. Sa taille exceptionnelle "
        "et sa silhouette immédiatement reconnaissable en ont "
        "fait un emblème de Paris.")

    assert mediawiki_api.getStory(685616) == goodAnswer


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
    """ test the function getPageidFromPlace """

    def mock_get(*arg, **kwargs):
        """ return the results from method
        json of class PageidfromplaceResponse
        """
        return PageidfromplaceResponse

    monkeypatch.setattr(requests, 'get', mock_get)
    assert mediawiki_api.getPageidFromPlace('tour eiffel') == 1359783


class StoryExtractResponse:

    @staticmethod
    def json():
        results = {
                    'batchcomplete': '',
                    'query': {
                        'pages': {
                            '1359783': {
                                'pageid': 1359783,
                                'ns': 0,
                                'title': 'Tour Eiffel',
                                'lat': 48.858296,
                                'lon': 2.294479,
                                'dist': 8.2,
                                'primary': '',
                                'extract': 'La tour Eiffel est une tour de '
                                'fer puddlé de 324 mètres de hauteur (avec '
                                'antennes)...',
                                }
                            }
                        }
                    }
        return results


def test_getStoryExtract(monkeypatch):
    """ test the function getStoryExtract """

    def mock_get(*arg, **kwargs):
        """ return the results from method
        json of class StoryExtractResponse
        """
        return StoryExtractResponse

    monkeypatch.setattr(requests, 'get', mock_get)
    assert mediawiki_api.getStoryExtract(1359783) == (
                                                'La tour Eiffel est une '
                                                'tour de fer puddlé de 324 '
                                                'mètres de hauteur (avec '
                                                'antennes)...')
