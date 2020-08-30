from flask import Flask, render_template, request, Markup
import json
import requests
import datetime

with open('city.json', encoding='utf8') as jsonObj:
    params = json.load(jsonObj)


app = Flask(__name__)

htmlcity = ''
htmlcitydescription = ''
temp = ''
min_temp = ''
max_temp = ''
pressure = ''
humidity = ''
wind_speed = ''
country = ''


def citywalafunc():
    global htmlcity, htmlcitydescription, temp, min_temp, max_temp, pressure, humidity, wind_speed, country
    inputCity = request.form.get('inputwalatext').lower()
    city = ''
    for i in params:
        if inputCity == str(i['name']).lower():
            city = i['name']
        else:
            try:
                langs = i['langs']
                secondCountry = langs[0]
                for j in secondCountry:
                    cityy = str(secondCountry[j])
                    if inputCity == cityy.lower():
                        city = secondCountry[j]
            except KeyError as e:
                pass
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=486eec8ca7376c00cb68660ac79c1c7f'
    r = requests.get(url)
    data = r.json()
    htmlcity = data['name']
    htmlcitydescription = data['weather'][0]['main']
    temp = str(data['main']['temp'] - 273.15).split('.')[0]
    min_temp = str(data['main']['temp_min'] - 273.15).split('.')[0]
    max_temp = str(data['main']['temp_max'] - 273.15).split('.')[0]
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    country = data['sys']['country']


@app.route('/', methods=['GET', 'POST'])
def index():
    time = ''
    dataa = ''
    errormsg = ''
    global htmlcity, htmlcitydescription, temp, min_temp, max_temp, pressure, humidity, wind_speed, country
    if request.method == 'POST':
        try:
            citywalafunc()
            time = str(datetime.datetime.now()).split('.')[0]
            dataa = Markup(f'<div class = "container" id = "weather"><div class = "card text-center" ><div class = "card-header"><h1> {htmlcity} </h1></div ><div class = "card-body" ><h5 class = "card-title"> {htmlcitydescription} </h5><p class = "card-text" > Temprature: {temp} °C </p><p class = "card-text"> Minimum Temprature: {min_temp} °C </p><p class = "card-text"> Maximum Temprature: {max_temp} °C </p><p class = "card-text"> Pressure: {pressure} Pa </p><p class = "card-text"> Humidity: {humidity} </p><p class = "card-text"> Wind Speed: {wind_speed} </p><p class = "card-text"> Country: {country} </p></div ><div class = "card-footer text-muted">Contents Loaded at {time}</div></div></div>')
        except KeyError as e:
            errormsg = Markup('<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>Error!</strong> Enter the Correct City Name.<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>')
    return render_template('index.html', content=dataa, errormsg=errormsg)


app.run(debug=True)
