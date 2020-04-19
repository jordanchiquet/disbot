import sys
import requests
import json

def warzonestats(user):
    print("starting warzonestats with provided user: [" + user + "]")
    try:
        loginsession = requests.Session()
        loginsession.get("https://profile.callofduty.com/cod/login")
        tokendict = loginsession.cookies.get_dict()
        xsrf = tokendict["XSRF-TOKEN"]
        print("got xsrf: [" + xsrf + "]")
        logindata = {'username': 'jordanchiq@gmail.com', 'password': 'T3ster12',
                    'remember_me': 'true', '_csrf': xsrf}
        loginsession.post("https://profile.callofduty.com/do_login?new_SiteId=cod", data = logindata)
        trackerurl = "https://my.callofduty.com/api/papi-client/stats/cod/v1/title/mw/platform/battle/gamer/" + user.split("#")[0] + "%23" + user.split("#")[1] + "/profile/type/mp"
        response = loginsession.get(url = trackerurl)
        # rlogged = 
        print("got warzonestats response")
        warzonejson = response.json()
        print(warzonejson)
        level = str(warzonejson["data"]["level"]).split(".")[0]
        kills = str(warzonejson["data"]["lifetime"]["mode"]["br"]["properties"]["kills"]).split(".")[0]
        deaths = str(warzonejson["data"]["lifetime"]["mode"]["br"]["properties"]["deaths"]).split(".")[0]
        suicides = str(warzonejson["data"]["lifetime"]["all"]["properties"]["suicides"]).split(".")[0]
        ratio = str(warzonejson["data"]["lifetime"]["mode"]["br"]["properties"]["kdRatio"])[:4]
        wins = str(warzonejson["data"]["lifetime"]["mode"]["br"]["properties"]["wins"]).split(".")[0]
        top10 = str(warzonejson["data"]["lifetime"]["mode"]["br"]["properties"]["topTen"]).split(".")[0]
        games = str(warzonejson["data"]["lifetime"]["mode"]["br"]["properties"]["gamesPlayed"]).split(".")[0]
        return(level + "|" + kills + "|" + deaths + "|" + suicides + "|" + ratio + "|" + wins + "|" + top10 + "|" + games)
    except:
        return("inv")