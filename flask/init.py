from flask import Flask, redirect, url_for, render_template
import requests, json

app = Flask(__name__)

city = ''
weatherApiKey = 'xxxxx'
weatherBaseUrl = 'http://api.openweathermap.org/data/2.5/weather'

@app.route("/")
def home():
    getLocation()
    weatherDetails = getWeatherForCity()

    return render_template("index.html", place=weatherDetails['city'],
    currentTemp=weatherDetails['currentTemp'],
    minTemp=weatherDetails['minTemp'],
    maxTemp=weatherDetails['maxTemp'],
    pressure=weatherDetails['pressure'],
    humidity=weatherDetails['humidity']
    )

# get location from ip address
def getLocation():
    response = requests.get('http://ipinfo.io')
    responsePythonObject = json.loads(response.text)
    global city
    city = responsePythonObject['city']
    print(city)

# get weather info for a city
def getWeatherForCity():
    weatherUrl = weatherBaseUrl + '?q=' + city + '&appid=' + weatherApiKey
    response = requests.get(weatherUrl)
    weatherObject = json.loads(response.text)
    
    mainWeatherInfo = weatherObject['main']

    weatherDesc = weatherObject['weather'][0]['description']
    
    currentTemp = mainWeatherInfo['temp']
    minTemp = mainWeatherInfo['temp_min']
    maxTemp = mainWeatherInfo['temp_max']
    pressure = mainWeatherInfo['pressure']
    humidity = mainWeatherInfo['humidity']

    place = weatherObject['name']

    weatherDetails = {
        'city': place,
        'currentTemp': currentTemp - 273.15,
        'minTemp': minTemp - 273.15,
        'maxTemp': maxTemp - 273.15,
        'pressure': pressure,
        'humidity': humidity
    }
    
    return weatherDetails

    
if __name__ == "__main__":
    app.run(debug=True)

