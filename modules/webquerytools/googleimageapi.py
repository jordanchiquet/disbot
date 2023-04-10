
import os

# functions from my randomhelpers file in the folder above this; getRegexReturn is currently unused in this file. genErrorHandle is my exception handler that I use in several files. 
from modules.randomhelpers import getRegexReturn, getUrlContentType, genErrorHandle

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
    rawresult = gsource.list(q=query,searchType='image',cx=appapi).execute()

    imglink = resultiterator(rawresult)
    imglinkContentType = getUrlContentType(imglink)
    tryint = 0
    while "ERROR" in imglinkContentType or "image" not in imglinkContentType:
        print(f"non-embeddable image in link [{imglink}]")
        tryint += 1
        print("trying next result [tryint: {}]".format(tryint))
        imglink = resultiterator(rawresult, tryint)
        imglinkContentType = getUrlContentType(imglink)
    print(f"imageget returning: [{imglink}]")
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
