import os
import requests

from modules.webquerytools.googleapi import googleget

key = os.environ.get('MERRIAMWEBSTER')

#API MERRIAMWEBSTER

def getmeaning(query):
    print("getmeaning with query: [" + query + "]")
    try:
        meaningurl = "https://www.dictionaryapi.com/api/v3/references/collegiate/json/" + query + "?key=" + key
        response = requests.get(url = meaningurl)
        print("got meaning response")
        print("response:")
        print(response)
        meaningjson = response.json()
        print(meaningjson)
        defcount = len(meaningjson)
        meanings = []
        for x in range(0, min(defcount, 3)):
            form = meaningjson[x]["fl"]
            deflist = meaningjson[x]["shortdef"]
            defrep = {"1": "a", "2": "b", "3": "c", "4": "d", "5": "e" }
            formrep = {"*a": "*1", "*b": "*2", "*c": "*3", "*d": "*4", "*e": "*5"}
            coderep = {"**2": "```**2", "**3": "```**3", "**4": "```**4", "**5": "```**5"}
            forminsertion = ("**" + str(x+1) + ".**  *(" + form.capitalize() + ")*")
            deflist.insert(0, forminsertion)
            for x in enumerate(deflist, 0):
                meanings.append(x)
            meaningstrconv = tuple(map(str, meanings))
            meaningtuplejoin = ["".join(tups) for tups in meaningstrconv]
            meaninglist = []
            for x in meaningtuplejoin:
                y = (x[1] + ". " + x[5:])[:-2].replace("0. ", "")
                y = y.replace(" :", ":\n  ")
                y = y.replace(")*", ")* ```")
                for i, j in defrep.items():
                    y = y.replace(i, j)
                for i, j in formrep.items():
                    y = y.replace(i, j)
                for i, j in coderep.items():
                    y = y.replace(i, j)
                meaninglist.append(y)
            meaninglist.append("```")
            meaningjoin = "\n".join(meaninglist)
    except:
        try:
            result = googleget("what is " + query)
            if result == None:
                meaningjoin = None
            else:
                meaningjoin = ("Couldn't find a meaning in the dictionary, tried google:\n" + result)
        except:
            meaningjoin = None
    return(meaningjoin)
    
