import re
import urllib.parse
import urllib.request

from youtube_api import YouTubeDataAPI

api_key = 'AIzaSyDse_e2vwSyvENfJiYM_oQNDOA06dR4a3g'
yt = YouTubeDataAPI(api_key)


def youtubesearch(query):
    search = yt.search(q=query, max_results=1)
    print(search)
    if search == []:
        result = "perhaps there is web net error but no vid found"
    elif search[0]["video_id"]:
        vidurl = search[0]["video_id"]
        result = "https://youtu.be/" + vidurl
    else:
        result = "perhaps there is web net error but no vid found"
    return(result)
    # print("starting youtube search with query: [" + query + "]")
    # ytquery = urllib.parse.urlencode({"search_query" : query})
    # html_cont = urllib.request.urlopen("http://youtube.com/results?"+ytquery)
    # print("got youtube result")
    # print("--------------")
    # print(html_cont)
    # print(html_cont.read())
    # ytresult = re.findall(r'href=\"\/watch\?v=(.{11})', html_cont.read().decode())
    # ytfinal = "https://youtu.be/" + ytresult[0]
    # print("ytfinal: [" + ytfinal + "]")
    # return(ytfinal) 

youtubesearch("dog")