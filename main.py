import flask
from flask import Flask
from waitress import serve
from os import getenv

app = Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/links')
def whyilovebella():
    return flask.render_template('links.html')

@app.route('/aboutme')
def aboutme():
    return flask.render_template('aboutme.html')

@app.route('/myfriends')
def myfriends():
    return flask.render_template('myfriends.html')