import functools
import re
import sys
import time
import traceback

from datetime import datetime, timedelta
from requests_html import HTMLSession

def capitalizexindex(s, n):
    return s[:n].lower() + s[n:].capitalize()

def getFunctionName():
    return sys._getframe(1).f_code.co_name

def genErrorHandle(exception: Exception):
    exceptionType = type(exception).__name__
    tb = sys.exc_info()[-1]
    stack = traceback.extract_tb(tb, 1)
    functionName = stack[0][2]
    outStr = (f"ERROR:{functionName}:{exceptionType}:{exception}")
    print(outStr)
    return(outStr)

def genFuncErrorWrapper(func):
    '''Reminder'''
    print("this is happening")
    @functools.wraps(func)
    def wrapper(exception: Exception):
        exceptionType = type(exception).__name__
        tb = sys.exc_info()[-1]
        stack = traceback.extract_tb(tb, 1)
        functionName = stack[0][2]
        outStr = (f"ERROR:{functionName}:{exceptionType}:{exception}")
        print(outStr)
        func(exception)
        return func(exception)
    return(wrapper)



def getFirstAlphaIndex(input):
    return(input.find(next(filter(str.isalpha, input))))

def getNextItem(startItem, itemOwner: list, increment: int):
    nextItem = None
    listLength = len(itemOwner)
    for index, item in enumerate(itemOwner):
        if item == startItem:
            if index < (listLength - 1):
                nextItem = itemOwner[index+increment]
    return(nextItem)

def getCSTOffsetTime() -> datetime:
    if time.localtime().tm_isdst > 0:
        cstDelta = 5
    else:
        cstDelta = 6
    return(datetime.now() - timedelta(hours=cstDelta))

def getWebSource(url: str):
    print(f"getWebSource called for [{url}]")
    try:
        session = HTMLSession()
        response = session.get(url)
        return response
    except Exception as e:
        return(genErrorHandle(e))

def getSpaceList(input: str):
    print(f"getSpaceList called for input: [{input}]")
    output = input.split(" ")
    return(output)

def listemptystring(listtocheck):
    if listtocheck[0] == "":
        del listtocheck[0]
    return(listtocheck)

def removefirstindex(thelist):
    print(f"list before removing first index: {thelist}")
    del thelist[0]
    print(f"list after removing the first index: {thelist}")
    return(thelist)

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

def getRegexReturn(query: str, input: str):
    print("getRegexReturn with query: [" + query + "] and input: [" + input + "]")
    try:
        print("attempting to compile query: [" + query + "]")
        re.compile(query)
    except:
        print("failure to compile query")
        getRegexReturnOut = None
    regexSearch = re.search(query, input)
    getRegexReturnOut = regexSearch
    print("getRegexReturnOut: [" + str(getRegexReturnOut) + "]")
    return(getRegexReturnOut)


def isEmote(input: str) -> bool:
    print(f"isEmote called with input: [{input}]")


def subEmotes(input: str, substr: str) -> str:
    print(f"subEmotes called with input: [{input}]")
    output = re.sub(r"<.*?\:.*?\:\d+>", substr, input)
    print(f"subEmotes output: [{output}]")
    return(output)
