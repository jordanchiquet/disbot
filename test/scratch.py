import urllib.request
from bs4 import BeautifulSoup

def codstats(user):
    print("codstats called")
    url = "https://cod.tracker.gg/warzone/profile/battlenet/" + user.split("#")[0] + "%23" + user.split("#")[1] + "/overview"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    codhtml = urllib.request.urlopen(req)
    codsoup = BeautifulSoup(codhtml.read(), 'html.parser')
    print(codsoup)


codstats("HotDog94#11957")