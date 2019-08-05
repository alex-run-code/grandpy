#contient les routes
#! /usr/bin/env python
from flask import Flask, render_template, url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
@app.route('/index/')
def home():
    return render_template('pages/index.html')


@app.route('/about/')
def about():
    return render_template('pages/about.html')

@app.route('/donation/')
def donation():
    return render_template('pages/donation.html')

@app.route('/map/')
def map():
    return render_template('pages/map.html')

@app.route('/geocode/')
def geocode():
    return render_template('pages/test_google_geocode.html')

@app.route('/api/')
def api():
    return 'api'


if __name__ == "__main__":
    app.run(debug=True)
