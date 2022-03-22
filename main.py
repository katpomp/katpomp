import flask
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/')
def whyilovebella():
    return flask.render_template('whyilovebella.html')

@app.route('/')
def aboutme():
    return flask.render_template('aboutme.html')


if __name__ == "__main__":
    app.run()
