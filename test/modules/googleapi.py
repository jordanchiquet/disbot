from googleapiclient.discovery import build #google-api-python-client

gapi = "AIzaSyDse_e2vwSyvENfJiYM_oQNDOA06dR4a3g"
gsource = build("customsearch", 'v1', developerKey=gapi).cse()

def googleget(query):
    print("googleget started with query: [" + query + "]")
    rawresult = gsource.list(q=query, cx='016515025707600383118:gqogcmpp7ka').execute()

    try:
        print("rawresult: [" + str(rawresult) + "]")
        firstresult = rawresult['items'][0]
        print("firstresult: [" + str(firstresult) + "]")
        searchresult = firstresult['link']
        print("madeithere")
        print("searchresultaaa: [" + searchresult + "]")
        return(searchresult)
    except KeyError:
        return("how you say? not any resultfind for find for that result to find the search find")