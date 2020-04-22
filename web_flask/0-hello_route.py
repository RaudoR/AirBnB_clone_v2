#!/usr/bin/python3
'''start flask server'''
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    '''display text'''
    return ("Hello HBNB!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
