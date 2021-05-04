
import os
import json
from pprint import pprint
#from dateutil.parser import parse as parse_datetime ~~~~ don't think i need this

import requests
from dotenv import load_dotenv
#from pgeocode import Nominatim as Geocoder ~~~~ don't think i need this
#from pandas import isnull ~~~~ don't think i need this

#
# def advice_wrapper(callback):
#     def inner_advice():
#         callback()
#
#     return inner_advice
#
#
# def get_advice():
#     response = requests.get(request_url)
#     parsed_response = json.loads(response.text)
#
# get_advice = advice_wrapper(get_advice)


asking = True

print("Welcome to Shiba of Wisdom!")

vibe = input("Do you wish to ask the Shiba of Wisdom about something or receive fated, random advice? [ask/random]:")
vibee = vibe.lower()
if vibee == "random":
    request_url = "https://api.adviceslip.com/advice"
elif vibee == "ask":
    while asking:
        asking = False
        advicestr = input("What do you wish to ask the Shiba of Wisdom for advice on?:")
        #https://api.adviceslip.com/advice/search/spiders
        request_url = "https://api.adviceslip.com/advice/search/"+advicestr
            ###insert data validation


response = requests.get(request_url)
parsed_response = json.loads(response.text)





        #
        #
        # get_advice()
        #
        # print(parsed_response)


        #if
          #
          # {
          #  "message": {
          #     "type": "notice",
          #     "text": "Advice slip not found."
          #   }
          # }
        # print("The Shiba of Wisdom cannot offer advice on that topic.")
        # print("Try entering a single, correctly spelled topic for advice (no numbers please!)")
        # else:
        #    asking = False




        #f"https://api.weather.gov/points/{geo.latitude},{geo.longitude}"
        #response = requests.get(request_url)
        # if response.status_code != 200:
        #     return None
