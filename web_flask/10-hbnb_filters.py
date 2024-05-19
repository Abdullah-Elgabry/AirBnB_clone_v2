#!/usr/bin/python3
""" Handeling filters """
from flask import Flask
from models import storage
from flask import render_template

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """redering filter | with states"""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(excpt=None):
    """session closing() """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")