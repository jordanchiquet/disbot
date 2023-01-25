import random


from modules.webquerytools.gifgrab import getgif
from modules.webquerytools.googleapi import googleget
from modules.webquerytools.googleimageapi import imageget
from modules.webquerytools.merriamapi import getmeaning
from modules.webquerytools.openaiquery import getdalle
from modules.webquerytools.wikihow import wikihow
from modules.webquerytools.wikipediasearch import wikipediaSearch
from modules.webquerytools.urbandictionary import udget
from modules.webquerytools.youtube import youtubesearch

from modules.webquerytools.webQueryNoneList import noneList

def cmdHandlerWebQueries(cmd: str, query: str):
    print("cmdHandlerWebQueries started")
    cmdMainRes = None
    if cmd == "d":
        cmdMainRes = getmeaning(query)
    elif cmd == "dalle":
        cmdMainRes = getdalle(query)
    elif cmd == "g":
        cmdMainRes = googleget(query)
    elif cmd == "gif":
        cmdMainRes = getgif(query)
    elif cmd == "how":
        cmdMainRes = wikihow(query)
    elif cmd == "img":
        cmdMainRes = imageget(query)
    elif cmd =="ud":
        cmdMainRes = udget(query)
    elif cmd == "yt":
        cmdMainRes = youtubesearch(query)


    if cmdMainRes is None:
        print("cmdHandlerMain got None for cmdMainRes")
        cmdMainRes = random.choice(noneList)
    return(cmdMainRes)

def cmdHandlerTools(cmd: str, paramtext: str = None):
    print("cmdHandlerTools started")
    toolList = ["timer", "math", "roll"]
    pass
    #TODO: these

def cmdHandlerGoofs(cmd:str, paramextra: any = None):
    print("cmdHandlerGoods started")
    goofList=[]

def cmdRandos(cmd: str):
    print("cmdRandos started")
    randoList = ["bird", "cat", "coin", "conch", "dog"]


