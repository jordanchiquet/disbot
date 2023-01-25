from youtube_api import YouTubeDataAPI #youtube-data-api
import os

#API GOOGLE

api_key = os.environ.get('GOOGLE')
yt = YouTubeDataAPI(api_key)


def youtubesearch(query):
    print("youtubesearch started with query [" + query + "]")
    search = yt.search(q=query, max_results=1)
    if search == []:
        result = None
    elif search[0]["video_id"]:
        vidurl = search[0]["video_id"]
        result = "https://youtu.be/" + vidurl
    else:
        result = None
    #TODO: return more vid metadata for embed
    print("youtubesearch returning: [" + str(result) + "]")
    return(result)


# class YTMusic:

#     def __init__(self) -> None:
#         pass

#     def playlistAdd(url, playlist):
