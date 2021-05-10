
import os
import json
from pprint import pprint
import requests
import random
from PIL import Image, ImageFont, ImageDraw
import shutil

#advice code

def advice_search(pointer):
#don't forget a docstring
    global parsed_response
    global advicestr
    searching = True
    while searching:
        if pointer == "random":
            request_url = "https://api.adviceslip.com/advice"
            searching = False
        elif pointer == "ask":
            advicestr = input("What do you wish to ask the Shiba of Wisdom for advice on?:")
            #https://api.adviceslip.com/advice/search/spiders
            if advicestr == "random":
                request_url = "https://api.adviceslip.com/advice"
                searching = False
            else:
                request_url = f"https://api.adviceslip.com/advice/search/{advicestr}"

        response = requests.get(request_url)
        parsed_response = json.loads(response.text)

        if 'message' in parsed_response:
            print(f"The Shiba of Wisdom cannot offer advice about {advicestr}. Please try again.")
        else:
            searching = False



print("Welcome to Shiba of Wisdom!")
checking = True
while checking:
    advice_type = input("Do you wish to ask the Shiba of Wisdom about something or receive fated, random advice? [ask/random]:")
    advice_types = ['ask','random']
    if advice_type not in advice_types:
        print("Please enter 'ask' if you want specific advice, or enter 'random'.")
    else:
        checking = False

advice_search(advice_type)

if advice_type == 'random':
    your_advice = parsed_response['slip']['advice']

else:
    advice_num = int(parsed_response["total_results"])
    if advice_num > 1:
        #love
        rand_advice = random.randint(0,advice_num-1)
        your_advice = parsed_response["slips"][rand_advice]['advice']
    else:
        #avocado
        your_advice = parsed_response["slips"][0]["advice"]



print(your_advice)
print("- The Shiba of Wisdom")
print("")
print("You can view your Shiba of Wisdom in the shibas folder in this directory.")
#maybe add extra part here to keep track of all your historical advice?

#shiba image code

request_url = "http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true"
response = requests.get(request_url)
parsed_response = json.loads(response.text)
shibalink = parsed_response[0]
if advice_type == 'random':
    shibafilename = "random_"+shibalink.split("/")[-1]
else:
    shibafilename = advicestr+ "_"+shibalink.split("/")[-1]


#GETTING SHIBA IMAGE FROM REQUESTS
picresponse = requests.get(shibalink, stream=True)


#writing advice on shiba
#play around with size
#advice_font = ImageFont.truetype('FONT ADDRESS',200)



#SAVING SHIBA IMAGE
#save in separate folder than final shibas of wisdom
picresponse.raw.decode_content = True
with open(shibafilename,'wb') as f:
    shutil.copyfileobj(picresponse.raw,f)
