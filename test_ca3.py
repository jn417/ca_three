""" This module contains the unit tests for the function in my other
modules. """

import unittest
from weather_update import get_weather
from news_filter import get_headlines, get_urls
from covid_data import national_covid_stats, exe_covid_stats

def test_weather():

    assert isinstance(get_weather(), str)

def test_news():

    assert isinstance(get_headlines(), list)
    assert isinstance(get_urls(), list)

def test_covid_data():

    assert isinstance(national_covid_stats(), str)
    assert isinstance(exe_covid_stats(), str)
