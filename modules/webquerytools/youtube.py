from youtube_api import YouTubeDataAPI #youtube-data-api
from randomhelpers import genErrorHandle


import flask
import os
import requests


import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

#API GOOGLE

api_key = os.environ.get('GOOGLE')

renardUserAuth = os.environ.get('RENARDGOOGLEOAUTH')

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





def youtubePlaylist():

    print(f"youtubePlaylist func started.")
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    try:
        # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        client_secrets_file = "D:\\locker\\client_secret_377709616008-f2st1g3297kcngnb1ggfphtd0b7c7gnp.apps.googleusercontent.com.json"

        scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

        state = flask.session['state']
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes, state=state)
        flow.redirect_uri = flask.url_for('oauth2callback', _external=True)

        authorization_response = flask.request.url
        flow.fetch_token(authorization_response=authorization_response)
        # flow.redirect_uri = "http://localhost:8080/"
        credentials = flow.credentials
        flask.session['credentials'] = {
            'token': credentials.token,
            'refresh_token': credentials.refresh_token,
            'token_uri': credentials.token_uri,
            'client_id': credentials.client_id,
            'client_secret': credentials.client_secret,
            'scopes': credentials.scopes}
        print(flask.session)
        # credentials = flow.run_local_server()
        # youtube = googleapiclient.discovery.build(
        #     api_service_name, api_version, credentials=credentials)


        
        
        # try:
        #     print("HEREHEREHERE")
        #     authorization_url, state = flow.authorization_url(
        #     access_type='offline',
        #     include_granted_scopes='true')
        # except (KeyboardInterrupt, Exception) as e:
        #     genErrorHandle(e)
        return flask.redirect(authorization_url)
    except (KeyboardInterrupt, Exception) as e:
        genErrorHandle(e)




redirect = youtubePlaylist()
print(redirect)



# class YTMusic:

#     def __init__(self) -> None:
#         pass

#     def playlistAdd(url, playlist):
