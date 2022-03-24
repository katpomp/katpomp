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


#if __name__ == "__main__":
#    serve(app, host=getenv('HOST'), port=getenv('PORT'))
