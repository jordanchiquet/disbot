from whapi import random_article, return_details, search
from modules.webquerytools.googleapi import googleget

def wikihow(howquery: str = None): 
    print("wikihow started")
    try:
        if howquery is None or howquery == "":
            articleid = random_article()
            howresults = dict(return_details(articleid))
        else:
            print("placeholder")
            howresults = dict(search(howquery, 1)[0])
            print(howresults)
        url = howresults['url']
        return(url)
    except:
        try:
            return("nothing on wikihow, trying google...\n" + googleget(howquery))
        except:
            return(None)