from grandpyapp import parser


def test_getPlace():
    question = 'Grand py, ou se trouve la cathedrale de paris ?'
    assert parser.getPlace(question) == 'cathedrale de paris ?'

def test_getInfo():
    latitude = str(37.7891838)
    longitude = str(-122.4033522)
    assert parser.getInfos(latitude, longitude) == 'Wikimedia Foundation'



