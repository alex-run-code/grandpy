import parserino


def test_getPlace():
    question = 'Grand py, ou se trouve la cathedrale de paris ?'
    question2 = 'Grand py, ou se trouve cathedrale paris ?'
    question3 = 'le louvre'
    question4 = "Grand py, ou se trouve l'adresse d'openclassroom ?"
    assert parserino.getPlace(question) == 'cathedrale de paris'
    assert parserino.getPlace(question2) == ('Grand py, ou se '
                                             'trouve cathedrale paris')
    assert parserino.getPlace(question3) == 'louvre'
    assert parserino.getPlace(question4) == 'de openclassroom'
