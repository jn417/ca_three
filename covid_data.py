
""" This module uses the official Covid data API and extracts relevant data """

from uk_covid19 import Cov19API
import json, requests
from types import *

def national_covid_stats():

    """ This function takes no arguments but extracts data from the covid
    api and returns it as a string """


    all_nations = [
        'areaType=overview'
    ]

    cases = {
         "date": "date",
        "areaName": "areaName",
        "areaCode": "areaCode",
        "newCasesByPublishDate": "newCasesByPublishDate",
        "cumCasesByPublishDate": "cumCasesByPublishDate",
        "newDeaths28DaysByPublishDate": "newDeaths28DaysByPublishDate",

    }

    #instantiating the API object
    api = Cov19API(
        filters=all_nations,
        structure=cases,
        latest_by="newCasesByPublishDate"
    )


    data1 = api.get_json()

    #creating list from dictionary key
    x = data1['data']


    gen_covid = "NATIONALLY." " Number of new deaths: " + str(x[0]['newDeaths28DaysByPublishDate']) + "." \
    " Number of new cases: " + str(x[0]['newCasesByPublishDate']) + "."

    return gen_covid



def exe_covid_stats():

    """ This function takes no arguments but extracts data from the covid
    api and returns it as a string """

    #narrowing down covid data to just Exeter
    exeter = [
        'areaName=Exeter'
    ]

    cases = {
         "date": "date",
        "areaCode": "areaCode",
        "newCasesByPublishDate": "newCasesByPublishDate",
        "cumCasesByPublishDate": "cumCasesByPublishDate",
        "newDeaths28DaysByPublishDate": "newDeaths28DaysByPublishDate",

    }

    #instantiating the API object
    api = Cov19API(
        filters=exeter,
        structure=cases,
        latest_by="newCasesByPublishDate"
    )


    data2 = api.get_json()

    #creating list from dictionary key
    exe_data = data2['data']


    exe_covid = " LOCALLY." + " Number of new deaths: " + str(exe_data[0]['newDeaths28DaysByPublishDate']) + "." + \
    " Number of new cases: " + str(exe_data[0]['newCasesByPublishDate']) + "."

    return exe_covid
