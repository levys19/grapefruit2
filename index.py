from flask import Flask, render_template, request
from option import Option
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():

    text = request.form['text']
    cityName = text.upper()
    findCity = Option()
    param = findCity.breakfast_search(cityName)
    locationData = findCity.get_results(param)
    locationNames = []
    for items in locationData["businesses"]:
        locationNames.append(items["name"])
    return str(locationNames)


if __name__ == "__main__":

    app.run(debug=True)
