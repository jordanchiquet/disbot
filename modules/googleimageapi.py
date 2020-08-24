from googleapiclient.discovery import build #google-api-python-client

gapi = "AIzaSyDse_e2vwSyvENfJiYM_oQNDOA06dR4a3g"
gsource = build("customsearch", 'v1', developerKey=gapi).cse()

def imageget(query, filetype: str = None):
    if filetype is None or filetype == "nonspecific":
        rawresult = gsource.list(q=query, searchType='image',
                                cx='016515025707600383118:gqogcmpp7ka').execute()
    else:
        if filetype == "gif":
            rawresult = gsource.list(q=query, searchType='image', fileType=filetype,
                                    cx='016515025707600383118:gqogcmpp7ka').execute()
        else:        
            rawresult = gsource.list(q=query, searchType='image', fileType=filetype,
                                    cx='016515025707600383118:gqogcmpp7ka').execute()
    tryint = 0
    imglink = resultiterator(rawresult, tryint)
    while imglink.endswith(".svg") or imglink.endswith("&get_thumbnail=1"):
        print("svg or facebook image in link [" + imglink + "] ; iterating")
        tryint = tryint + 1
        imglink = resultiterator(rawresult, tryint)
    print(imglink)
    return(imglink)


def resultiterator(rawresult, tryint):
    try:
        result = rawresult['items'][tryint]
        imglink = result['link']
    except KeyError:
        imglink = "how you say? not any image find for that image"
    return(imglink)


imageget("me and my friends looking at u")