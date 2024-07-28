#!/usr/bin/python3

"""Basic Flask web application."""


from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():

    """Return a greeting message."""

    return "Hello HBNB!"


if __name__ == '__main__':
    # Run the app on port 5000 & listen for all public IP's
    app.run(debug=True, port=5000, host='0.0.0.0')
