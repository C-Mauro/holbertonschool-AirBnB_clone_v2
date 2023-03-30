#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    Display Hello HBNB
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    display HBNB
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cisfun():
    """ Display C """
    return "C{}".format(text.replace('_', ' '))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Python is cool"""
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def n(n):
    """Displays n if is a integer"""
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
