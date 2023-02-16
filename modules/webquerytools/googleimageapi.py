import json
import requests
import os
import pprint

from googleapiclient.discovery import build #google-api-python-client
#API GOOGLE
# then further down for cx=..
#API GOOGLEIMAGE
from modules.randomhelpers import getRegexReturn

gapi = os.environ.get("GOOGLE")
appapi = os.environ.get("GOOGLEAPP")
gsource = build("customsearch", 'v1', developerKey=gapi).cse()

def imageget(query, filetype: str = None):
    print("imageget (g images) started with query: [" + query + "]")
    if filetype is None or filetype == "nonspecific":
        rawresult = gsource.list(q=query, searchType='image',
                                cx=appapi).execute()
    else:
        rawresult = gsource.list(q=query, searchType='image', fileType=filetype,
                                cx=appapi).execute()
    print(rawresult)
    with open ('test.json', 'w') as f:
        json.dump(rawresult, f, indent=4)

    tryint = 0
    imglink = resultiterator(rawresult, tryint)
    print("here")
    # while getRegexReturn(query=doesntEmbedRegex, input=imglink) is not None:
    #     print("non-discord supported image in link [" + imglink + "] ; iterating")
    #     tryint = tryint + 1
    #     imglink = resultiterator(rawresult, tryint)
    print("imageget returning: [" + imglink + "]")
    getImageResponse(imglink)
    return(imglink)


def resultiterator(rawresult, tryint):
    try:
        result = rawresult['items'][tryint]
        imglink = result['link']
    except KeyError:
        imglink = None
    return(imglink)

def getImageResponse(url):
    response = requests.get(url)
    pprint.pprint(response.headers)
    print(response.status_code)
    return response


doesntEmbedRegex = (
    r"\?cb=|"
    r"&get_thumbnail=1$|"
    # r"cesarsway|"
    r"dynaimage|"
    r"edmunds|"
    r"ikon-images|"
    r"justhannen|"
    r"liquipedia|"
    r"lookaside.fbsbx|"
    r"makingwithmetal|"
    r"wordpress|"
    r"x-raw-image|"
    r"vox-cdn|" #https://cdn.vox-cdn.com/thumbor/X0UpfanPFP4M9ELKV1DNTKSF5U0=/94x0:1158x798/1200x800/filters:focal(94x0:1158x798)/cdn.vox-cdn.com/uploads/chorus_image/image/48839023/bachelormcdonalds.0.0.png
    r"\.svg$"  
)




# ones I don't know why they don't work (embed in discord when not using embed api and directly pasted)
#https://www.cesarsway.com/wp-content/uploads/2015/06/Through-a-Dogs-Eyes-2-300x224.jpg
#https://vox-cdn.com/uploads/chorus_image/image/650/Screen_Shot_2019-10-01_at_10.54.01_AM.0.png



imageget('how do we look to dogs')
