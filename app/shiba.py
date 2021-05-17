
import os
import json
from pprint import pprint
import requests
import random
from PIL import Image, ImageFont, ImageDraw
import shutil
import textwrap

#advice code


def get_advice(amount):
    """
    Selects random advice from API response given a user input that returned more than 1 advice slip

    Params: amount is the number of advice slips the API generated

    Examples: get_advice(6)
    """
    global your_advice
    if amount > 1:
        #love
        rand_advice = random.randint(0,amount-1)
        your_advice = parsed_response["slips"][rand_advice]['advice']
    else:
        #avocado
        your_advice = parsed_response["slips"][0]["advice"]


def shiba_file_name(type,shibalink,advicestr):
    """
    Returns name of the shiba image file that indicates what type of advice the user asked for and helps organize images.

    Params: the type of advice the user asked for ["random" or "ask"]

    Examples: shiba_file_name("ask")
    """
    global shibafilename
    if type == 'random':
        shibafilename = "random_"+ shibalink.split("/")[-1]
    elif type == "ask":
        shibafilename = advicestr+ "_"+ shibalink.split("/")[-1]

    return shibafilename


if __name__ == "__main__":

    print("Welcome to Shiba of Wisdom!")
    checking = True
    while checking:
        advice_type = input("Do you wish to ask the Shiba of Wisdom about something or receive fated, random advice? [ask/random]:")
        advice_types = ['ask','random']
        if advice_type not in advice_types:
            print("Please enter 'ask' if you want specific advice, or enter 'random'.")
        else:
            checking = False

    searching = True
    while searching:
        if advice_type == "random":
            request_url = "https://api.adviceslip.com/advice"
            searching = False
        elif advice_type == "ask":
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


    if advice_type == 'random':
        your_advice = parsed_response['slip']['advice']

    elif advice_type == 'ask':
        advice_num = int(parsed_response["total_results"])
        get_advice(advice_num)




    #shiba image code

    request_url = "http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    shibalink = parsed_response[0]
    if advice_type == "random":
        advicestr = ""
    shiba_file_name(advice_type,shibalink,advicestr)

    shiba_pic_filepath = os.path.join(os.path.dirname(__file__), "..", "Shiba Images", shibafilename)

    #GETTING SHIBA IMAGE FROM REQUESTS
    picresponse = requests.get(shibalink, stream=True)


    #SAVING SHIBA IMAGE
    #save in separate folder than final shibas of wisdom
    picresponse.raw.decode_content = True
    with open(shiba_pic_filepath,'wb') as f:
        shutil.copyfileobj(picresponse.raw,f)

    notext_shiba = Image.open(shiba_pic_filepath)
    width, height = notext_shiba.size

    font_filepath = os.path.join(os.path.dirname(__file__),"..","JAPAB___.TTF")
    relative_font = int(height/20)
    #relative_length = int(width*.2)
    title_font = ImageFont.truetype(font_filepath,relative_font)
    editable_shiba = ImageDraw.Draw(notext_shiba)

    font_color = (255,255,255)
    border_color = (0,0,0)

    offset = 2

    test_width = int(width*.035)


    for chunk in textwrap.wrap(your_advice, width=test_width):
        editable_shiba.text((5,offset),chunk,fill=font_color,stroke_fill = border_color,font=title_font,stroke_width = 1)
        offset += title_font.getsize(chunk)[1]


    editable_shiba.text((5,height*(9/10)),"~ Shiba of Wisdom",fill=font_color,stroke_fill = border_color,font=title_font,stroke_width = 1)



    text_shibafilename = "final_"+shibafilename
    text_shiba_filepath = os.path.join(os.path.dirname(__file__), "..", "Shibas of Wisdom", text_shibafilename)
    notext_shiba.save(text_shiba_filepath)


    print("")
    print(your_advice)
    print("- The Shiba of Wisdom")
    print("")
    print("You can view your Shiba of Wisdom in the Shibas of Wisdom folder in this directory.")
    print("")

    notext_shiba.show()
