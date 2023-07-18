
import os
import requests

# functions from my randomhelpers file in the folder above this; getRegexReturn is currently unused in this file. genErrorHandle is my exception handler that I use in several files. 
from modules.randomhelpers import getRegexReturn, getUrlContentType, genErrorHandle

from googleapiclient.discovery import build 

#getting my api keys... I have them stored as environment variables on the OS
gapi = os.environ.get("GOOGLE")
appapi = os.environ.get("GOOGLEAPP")

# below line is making the google object, basically copy pasted from their docs. 
gsource = build("customsearch", 'v1', developerKey=gapi).cse()


#the main function the bot is actually calling. 
def imageget(query, tryint: int = 0):
    print(f"imageget (g images) started with query: [{query}]")
    rawresult = gsource.list(q=query,searchType='image',cx=appapi).execute()

    imglink, imglinkContentType = get_new_image_tuple(rawresult, tryint)
    print(f"imglinkContentType: {imglinkContentType}")
    print(f"get_need_iteration: {get_need_iteration(imglinkContentType)}")
    r = requests.get(imglink)
    print(f"r.status_code: {r.status_code}")
    print(r.headers)

    while get_need_iteration(imglinkContentType):
        print(f"non-embeddable image in link [{imglink}]")
        tryint += 1
        print("trying next result [tryint: {}]".format(tryint))
        imglink, imglinkContentType = get_new_image_tuple(rawresult, tryint)
    return(imglink)


def get_new_image_tuple(rawresult: dict, tryint: int = 0) -> tuple:
    if tryint < 10:
        imglink = resultiterator(rawresult, tryint)
        imglinkContentType = getUrlContentType(imglink)
    else:
        imglink = "sorry, google did not like that one for some reason."
        imglinkContentType = "image"
    return(imglink, imglinkContentType)

def get_need_iteration(contenttype: str) -> bool:
    skipList = [
    'ERROR',
    'avif'
    ]
    if "image" not in contenttype:
        return True
    for skip in skipList:
        if skip in contenttype:
            return True
    return False



# this actualy gets the result
def resultiterator(rawresult, tryint: int = 0):
    try:
        result = rawresult['items'][tryint]
        imglink = result['link']
    except Exception as e:
        genErrorHandle(e)
        imglink = None
    return(imglink)
