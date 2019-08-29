import requests
import google_api


class LocInfoResponse:

    @staticmethod
    def json():
        results = {
            'candidates': [{
                'formatted_address': 'Champ de Mars, 5 Avenue Anatole France, '
                '75007 Paris, Franţa',
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
        'address': 'Champ de Mars, 5 Avenue Anatole France, '
        '75007 Paris, Franţa',
        'latitude': 48.85837009999999,
        'longitude': 2.29448139999,
        'longitude': 2.2944813
        }
    assert google_api.getLocationInfos('Tour Eiffel') == goodAnswer