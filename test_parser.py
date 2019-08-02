from grandpyapp import parser

def test_getPlace():
    question = 'Grand py, ou se trouve la cathedrale de paris ?'
    assert parser.getPlace(question) == 'cathedrale de paris ?'

    




