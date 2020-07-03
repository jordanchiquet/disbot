import re
import urllib.parse
import urllib.request

from youtube_api import YouTubeDataAPI #youtube-data-api

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