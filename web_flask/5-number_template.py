#!/usr/bin/python3

"""
    Basic Flask web application.

    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ” followed by the value of the text variable
                   (replace underscore _ symbols with a space)
        /python/<text>: display “Python ” followed by the value of the text
                        variable (replace underscore _ symbols with a space).
                        The default value of text is “is cool”.
        /number/<n>: display “n is a number” only if n is an integer
        /number_template/<n>: display a HTML page only if n is an integer:
                              H1 tag: “Number: n” inside the tag BODY
"""


from flask import Flask
from markupsafe import escape
from flask import render_template

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


@app.route("/python/", strict_slashes=False, defaults={'text': 'is cool'})
@app.route("/python/<text>", strict_slashes=False)
def display_python_text(text):

    """
        Return a message for the /python/<text> route.

        Args:
            text: The text to display after 'Python',
                  with underscores replaced by spaces.
                  The default value is 'is cool'.
    """
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def display_number(n):

    """
        Return a message for the /number/<n> route if n is an integer.

        Args:
            n: The integer to display in the message.
    """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def display_number_template(n):

    """
        Return an HTML page for the /number_template/<n> route
        if n is an integer.

        Args:
            n: The integer to display in the HTML page.
    """
    return render_template('number.html', number=n)


if __name__ == '__main__':
    # Run the app on port 5000 & listen on all public IP's
    app.run(port=5000, host='0.0.0.0')
