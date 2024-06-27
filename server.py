from flask import Flask, render_template, request
from weather import get_current_weather
import requests
import certifi
from waitress import serve   #waitress is the package which will help serve our app on production

app = Flask(__name__)  # To make a app a falsk app

#Routs to acess on the web

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    # Check for empty strings or string with only spaces
    if not bool(city.strip()):
        # You could render "City Not Found" instead like we do below
        city = "Bangalore"
    weather_data= get_current_weather(city)
     # City is not found by API
    if not weather_data['cod'] == 200:
        return render_template('city-not-found.html')
    return render_template(
        "weahter.html",
        title =  weather_data['name'],
        status = weather_data["weather"][0]["description"].capitalize(),
        temprature = f"{weather_data['main']['temp']:.1f}",
        feels_like = f"{weather_data['main']['feels_like']:.1f}"
    )

if __name__ =="__main__":
    app.run(host="0.0.0.0", port= 8000)



