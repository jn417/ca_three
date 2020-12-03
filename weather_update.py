
""" Module to extract local weather data from the api stated in the
config file """

import requests,json
from configparser import ConfigParser


def kelvin_to_celsius( arg1 ):

    """ Function to convert kelvin to celsius.

    Takes a single flaot as an argument and returns a float itself. """

    celsius = (arg1 - 273.15)

    return "{:.2f}".format(celsius)


def get_weather():

    """ Function to extract weather data, takes no arguments but returns a
    string of local weather information """

    #collecting relevant data
    file = 'config.json'
    config = ConfigParser()
    config.read(file)

    base_url = config['third_parties']['weather_news']
    api_key = config['API_keys']['weather']
    city_name = config['city']['my_city']
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    response = requests.get(complete_url)
    x = response.json()

    #current temparature
    y = x["main"]
    current_temperature = y["temp"]

    #description of current weather
    z = x["weather"]
    weather_description = z[0]["description"]

    local_weather = "The weather is currently " + str(weather_description) + "." + " The temperature is " + \
    str(kelvin_to_celsius(current_temperature)) + " degrees."

    return local_weather
