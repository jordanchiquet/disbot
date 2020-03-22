from googleapiclient.discovery import build #google-api-python-client

gapi = "AIzaSyDse_e2vwSyvENfJiYM_oQNDOA06dR4a3g"
gsource = build("customsearch", 'v1', developerKey=gapi).cse()

async def imageget(msg):
    rawresult = gsource.list(q=msg[5:], searchType='image',
                             cx='016515025707600383118:gqogcmpp7ka').execute()
    try:
        firstresult = rawresult['items'][0]
        imgresult = firstresult['link']
        return(imgresult)
    except KeyError:
        return("how you say? not any image find for that image")
