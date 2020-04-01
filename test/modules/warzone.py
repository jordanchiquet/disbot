import requests

def warzonestats(user):
    trackerkey = "dff84ce3-8767-4b63-9a8b-1c86ae8c57f4"
    trackerurl = "'https://my.callofduty.com/api/papi-client/stats/cod/v1/title/mw/platform/battle/gamer/" + user.split("#")[0] + "%23" + user.split("#")[1] + "/profile/type/mp"
    trackerheaders = {"TRN-Api-Key": trackerkey}
    response = requests.get(url = trackerurl)
    warzonejson = response.json()
    print(warzonejson)

warzonestats("Hotdog94#11957")