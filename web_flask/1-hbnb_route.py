#!/usr/bin/python3

"""
    Basic Flask web application.

    Routes:

        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
"""


from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():

    """ Return a greeting message for the root route. """

    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def display_hbnb():

    """ Return a message for the /hbnb route. """
    return "HBNB"


if __name__ == '__main__':
    # Run the app on port 5000 & listen for all public IP's
    app.run(port=5000, host='0.0.0.0')
