#!/usr/bin/python3

"""
    Basic Flask web application.

    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ” followed by the value of the text variable
                   (replace underscore _ symbols with a space)
"""


from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():

    """ Return a greeting message for the root route. """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def display_hbnb():

    """ Return a message for the /hbnb route. """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_c_text(text):

    """
        Return a message for the /c/<text> route.

        Args:
            text: The text to display after 'C',
                  with underscores replaced by spaces.
    """
    return f"C {escape(text.replace('_', ' '))}"


if __name__ == '__main__':
    # Run the app on port 5000 & listen on all public IP's
    app.run(port=5000, host='0.0.0.0')
