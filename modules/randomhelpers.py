import re
import sys
import time
import traceback

import bs4 as bs

import urllib.request
from urllib.error import HTTPError, URLError

from datetime import datetime, timedelta
from requests_html import HTMLSession


def genFuncErrorWrapper(func):
    def wrapper(*args, **kwargs):
        try:
            return(func(*args, **kwargs))
        except Exception as e:
            return(genErrorHandle(e, func.__name__))
    return(wrapper)




@genFuncErrorWrapper
def capitalizexindex(s, n):
    return s[:n].lower() + s[n:].capitalize()

@genFuncErrorWrapper
def getFunctionName():
    return sys._getframe(1).f_code.co_name

@genFuncErrorWrapper
def genErrorHandle(exception: Exception, funcName = "[no funcName Found]") -> str:
    exceptionType = type(exception).__name__
    tb = sys.exc_info()[-1]
    stack = traceback.extract_tb(tb, 1)
    functionName = stack[0][2]
    outStr = (f"ERROR:{functionName}:{funcName}:{exceptionType}:{exception}")
    print(outStr)
    return(outStr)

@genFuncErrorWrapper
def getCSTOffsetTime() -> datetime:
    if time.localtime().tm_isdst > 0:
        cstDelta = 5
    else:
        cstDelta = 6
    return(datetime.now() - timedelta(hours=cstDelta))

@genFuncErrorWrapper
def getFirstAlphaIndex(input):
    return(input.find(next(filter(str.isalpha, input))))

@genFuncErrorWrapper
def getNextItem(startItem, itemOwner: list, increment: int):
    nextItem = None
    listLength = len(itemOwner)
    for index, item in enumerate(itemOwner):
        if item == startItem:
            if index < (listLength - 1):
                nextItem = itemOwner[index+increment]
    return(nextItem)

@genFuncErrorWrapper    
def getSpaceList(input: str):
    print(f"getSpaceList called for input: [{input}]")
    output = input.split(" ")
    return(output)

@genFuncErrorWrapper
def getWebSourceHTML(url: str):
    print(f"getWebSourceHTML called for [{url}]")
    source = getWebObject(url).read()
    soup = bs.BeautifulSoup(source, 'html.parser')
    return(soup)




@genFuncErrorWrapper
def getWebObject(url: str):
    print(f"getWebObject called for [{url}]")
    try:
        response = urllib.request.urlopen(url)
        print("got response")
        return response
    except (HTTPError, URLError, TimeoutError) as e:
        print(f"HttpError fors: {url}")
        return(genErrorHandle(e))

@genFuncErrorWrapper
def getUrlContentType(url: str):
    print(f"getUrlContentType called for url: [{url}]")
    response = getWebObject(url)
    try:
        contentType = response.headers['content-type']
        return(contentType)
    except Exception as e:
        return(genErrorHandle(e))

@genFuncErrorWrapper
def listemptystring(listtocheck):
    if listtocheck[0] == "":
        del listtocheck[0]
    return(listtocheck)

@genFuncErrorWrapper
def removefirstindex(thelist):
    del thelist[0]
    return(thelist)

@genFuncErrorWrapper
def getFirstWordGoneString(input: str):
    print("getFirstWordString started with input : ["
    + input + "]")
    spaceList = getSpaceList(input)
    if len(spaceList) > 1:
        spaceList = spaceList[1:]
        firstWordGoneOutput = " ".join(spaceList)
    else:
        firstWordGoneOutput = ""
    return(firstWordGoneOutput)

@genFuncErrorWrapper
def getRegexReturn(query: str, input: str):
    try:
        print("attempting to compile query: [" + query + "]")
        re.compile(query)
    except:
        print("failure to compile query")
        getRegexReturnOut = None
    regexSearch = re.search(query, input)
    getRegexReturnOut = regexSearch
    return(getRegexReturnOut)

@genFuncErrorWrapper
def subEmotes(input: str, substr: str) -> str:
    output = re.sub(r"<.*?\:.*?\:\d+>", substr, input)
    return(output)


@genFuncErrorWrapper
def addition(*args):
    print(sum(args))




def getWebObject2(url: str):
    print(f"getWebObject called for [{url}]")
    response = urllib.request.urlopen(url)
    print("got response")
    return response





# this is a te