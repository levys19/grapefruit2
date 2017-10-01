from flask import Flask, render_template, request
from option import Option
import json
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():

    text = request.form['text']
    cityName = text.upper()
    findCity = Option()
    currTime = datetime.datetime.now().time().hour
    whichMeal = ""
    if currTime >= 6 and currTime <= 11:
        whichMeal = "breakfast"
    elif currTime > 11 and currTime <= 16:
        whichMeal = "lunch"
    elif currTime > 16 and currTime < 22:
        whichMeal = "dinner"
    param = findCity.meal_search(cityName,whichMeal)
    locationData = findCity.get_results(param)
    restauraunt = []
    for items in locationData["businesses"]:
        restaurauntInfo = [items["name"],items["image_url"],items["price"],items["distance"]]
        restauraunt.append(restaurauntInfo)
    for things in restauraunt:
        print(things)
        
    return render_template("choices.html",restauraunt = restauraunt)


if __name__ == "__main__":

    app.run(debug=True)
