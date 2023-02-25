
import requests
import os
import pprint

# functions from my randomhelpers file in the folder above this; getRegexReturn is currently unused in this file. genErrorHandle is my exception handler that I use in several files. 
from modules.randomhelpers import getRegexReturn, genErrorHandle

from googleapiclient.discovery import build 

#getting my api keys... I have them stored as environment variables on the OS
gapi = os.environ.get("GOOGLE")
appapi = os.environ.get("GOOGLEAPP")

# below line is making the google object, basically copy pasted from their docs. 
gsource = build("customsearch", 'v1', developerKey=gapi).cse()


#the main function the bot is actually calling. 
def imageget(query):
    print(f"imageget (g images) started with query: [{query}]")

    # The below line creates an object called rawresult which consists of:
    #   the nested 'list' object from 'gsource' object created above, given three paramaters 
    #       the function 'execute()' within that 'list' object is then called.
    rawresult = gsource.list(q=query, searchType='image',
                                cx=appapi).execute()

    # resuable function i made for getting results
    imglink = resultiterator(rawresult)


    # the below is currently commented out but was a section I used briefly to iterate until I got an image discord would embed. I currently have it off for a long-term debugging project. 
    # while getRegexReturn(query=doesntEmbedRegex, input=imglink) is not None:
    #     print(f"non-discord supported image in link [{imglink}"]; iterating")
    #     tryint += 1
    #     imglink = resultiterator(rawresult, tryint)


    print(f"imageget returning: [{imglink}]")

    # getImageResponse is purely for debug purposes 
    # getImageResponse(imglink)

    # V this is the line that feeds the bot the link it will use V #
    return(imglink)


# this actualy gets the result
def resultiterator(rawresult, tryint: int = 0):
    try:
        result = rawresult['items'][tryint]
        imglink = result['link']
    except Exception as e:
        genErrorHandle(e)
        imglink = None
    return(imglink)

#testing function
def getImageResponse(url):
    response = requests.get(url)
    pprint.pprint(response.headers)
    print(response.status_code)
    return response
