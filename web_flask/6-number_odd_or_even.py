#!/usr/bin/python3
""" import flask """
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ hello function content """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """hbnb content return"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def addText(text):
    """add variable function starting with 'C' then text"""
    text = text.replace("_", " ")
    return 'C {}'.format(text)


@app.route("/python/", defaults={'text': 'is cool'})
@app.route("/python/<text>", strict_slashes=False)
def pythonText(text):
    """ display 'python' followed by the value 'text'"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def checkIfNum(n):
    """check if n is a number"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def displayHtml(n):
    """render template only if n is a number"""
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def evenOrOdd(n):
    """render template only if n is a number"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
