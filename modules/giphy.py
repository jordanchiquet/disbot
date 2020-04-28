import urllib.request as urllib, json

def getgif(gifquery):
    try:
        gifrep = {" ": "+"}
        for i, j in gifrep.items():
                gifquery = gifquery.replace(i, j)
        gifquery = gifquery.lower()
        url = "http://api.giphy.com/v1/gifs/search?q=" + gifquery + "&api_key=bvOBd5u5S23jgz0afMtFCsMZN3GlfIjO&limit=1"
        response = urllib.urlopen(url)
        response = response.read()
        data = json.loads(response)
        result = json.dumps(data, sort_keys = True, indent = 4)
        gifurl = data["data"][0]["images"]["original"]["url"]
        result = gifurl
    except:
        result = "erROR"
    return(result)