from flask import Flask, render_template, request
from option import Option

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():

    text = request.form['text']
    cityName = text.upper()
    findCity = Option()
    param = findCity.city_search(cityName)
    return str(findCity.get_results(param))


if __name__ == "__main__":

    app.run(debug=True)
