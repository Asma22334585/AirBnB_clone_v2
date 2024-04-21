#!/usr/bin/python3
""" starts a Flask web application:"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def d_route():
    """default_route"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cfun(text):
    """c what"""
    return "C {}".format(text.replace('_', ' '))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text='is cool'):
    """python is cool"""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def numberN(n):
    """ n is a number """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ HTML page if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """n is Odd OR Even"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
