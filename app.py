# contient les routes
# ! /usr/bin/env python
from flask import Flask, render_template, url_for, request
from flask_cors import CORS
import parserino
import config

app = Flask(__name__)
CORS(app)


@app.route('/')
@app.route('/index/')
def home():
    return render_template('pages/index.html', GOOGLE_API_KEY_MAPS=config.GOOGLE_API_KEY_MAPS)


@app.route('/about/')
def about():
    return render_template('pages/about.html')


@app.route('/donation/')
def donation():
    return render_template('pages/donation.html')


@app.route('/geocode/')
def geocode():
    return render_template('pages/test_google_geocode.html')


@app.route('/api/',  methods=['GET', 'POST'])
def api():
    if request.method == 'POST':
        print('request data : {}'.format(request.data))
        toBeParsed = request.data
        toBeParsed = toBeParsed.decode('utf-8')
        print('to be parsed : {}'.format(toBeParsed))
        print('info from data : {}'.format(parserino.getAllInfos(toBeParsed)))
        return parserino.getAllInfos(toBeParsed)
    else:
        return 'nothing has been posted'

if __name__ == "__main__":
    app.run(debug=True)
