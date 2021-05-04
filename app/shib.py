
import os
import json
from pprint import pprint

import requests
from PIL import Image, ImageFont, ImageDraw
import shutil



request_url = "http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true"
response = requests.get(request_url)
parsed_response = json.loads(response.text)
shibalink = parsed_response[0]
shibafilename = shibalink.split("/")[-1]

picresponse = requests.get(shibalink, stream=True)

picresponse.raw.decode_content = True
with open(shibafilename,'wb') as f:
    shutil.copyfileobj(picresponse.raw,f)





# shiba_image = Image.open(BytesIO(response.content))

# shiba_pic_filepath = os.path.join(os.path.dirname(__file__), "..","shibas","shibainu.jpg")
#
# with open(shiba_pic_filepath, )

# picfile = open(,"wb")
# picfile.write(picresponse.content)
# picfile.close()

###save shiba image as a temp image
#urllib.request.urlretrieve(shibalink, "local_shiba.jpg

    #
    # receipt_filepath = os.path.join(os.path.dirname(__file__), "..", "receipts", f"{receipt_id}.txt")
    #
    # with open(receipt_filepath, "w") as receipt_file:
    #     for line in receipt:
    #         for anotherline in line:
    #             receipt_file.write(f"\n {anotherline}")
