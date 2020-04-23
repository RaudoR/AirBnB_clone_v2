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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
