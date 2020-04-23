#!/usr/bin/python3
'''start flask server'''
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/", strict_slashes=False)
def hello_world():
    '''display text'''
    return ("Hello HBNB!")


@app.route('/hbnb')
def HBNB():
    '''deisplay text'''
    return ("HBNB")


@app.route('/c/<text>')
def c(text):
    '''display C followed by text'''
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/')
@app.route('/python/<text>')
def python(text="is cool"):
    '''display Python, followed by text'''
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    '''display n only if its an integer'''
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    '''display a HTML page'''
    return render_template('5-number.html', number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
