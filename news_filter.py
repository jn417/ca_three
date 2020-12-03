

""" Module to extract general and covid specific news headlines, and urls """


from configparser import ConfigParser
import requests
import json
from flask import Markup


def get_headlines():

    """ This module takes no arguments and returns a list of general news
    headlines gathered from the news api stated in the config file """

    #extracting data from news api
    file = 'config.json'
    config = ConfigParser()
    config.read(file)

    base_url = config['third_parties']['headline_news']
    api_key = config['API_keys']['news']
    country = "gb"
    complete_url = base_url + "country=" + country + "&apiKey=" + api_key
    response = requests.get(complete_url)

    news_dict = response.json()

    articles = news_dict["articles"]

    my_titles = []

    for article in articles:
        my_titles.append(article['title'])


    return my_titles

def get_urls():

    """ This module takes no arguments and returns a list of general news
    urls gathered from the news api stated in the config file """

    #extracting data from news api
    file = 'config.json'
    config = ConfigParser()
    config.read(file)

    base_url = config['third_parties']['headline_news']
    api_key = config['API_keys']['news']
    country = "gb"
    complete_url = base_url + "country=" + country + "&apiKey=" + api_key
    response = requests.get(complete_url)

    news_dict = response.json()

    articles = news_dict["articles"]

    my_urls = []

    for article in articles:
        my_urls.append(article['url'])


    return my_urls
