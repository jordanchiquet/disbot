import os

from googleapiclient.discovery import build #google-api-python-client

#API GOOGLE
#API GOOGLEAPP
gapi = os.environ.get('GOOGLE')
appapi = os.environ.get('GOOGLEAPP')
gsource = build("customsearch", 'v1', developerKey=gapi).cse()

def googleget(query):
    print("googleget started with query: [" + query + "]")
    rawresult = gsource.list(q=query, cx=appapi).execute()

    try:
        firstresult = rawresult['items'][0]
        searchresult = firstresult['link']
        print("googleget returning: [" + searchresult + "]")
        return(searchresult)
    except KeyError:
        return(None)