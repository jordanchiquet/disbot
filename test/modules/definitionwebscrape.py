

import urllib.request
from bs4 import BeautifulSoup
from modules.capitalizexindex import capitalizexindex


def getdefinition(defquery):
    drequest = defquery
    durlfriendly = drequest.replace(" ", "%20")
    dhtml = urllib.request.urlopen("https://www.merriam-webster.com/dictionary/"+durlfriendly)
    dsoup = BeautifulSoup(dhtml.read(), 'html.parser')
    dmetacontentlist = dsoup.findAll("meta")
    dmeaningblock = dmetacontentlist[8]
    dmeaningprefixremove = str(dmeaningblock)[15:]
    if "See the full definition" in dmeaningprefixremove:
        dmeaningprefixremove = dmeaningprefixremove.split("… See the full definition")[0]
    dmeaningcleanup = dmeaningprefixremove.replace(" :", ":")
    if ";" not in dmeaningcleanup:
        dmeaning = (defquery.upper() + ": " + dmeaning)
        return(dmeaning)
    dmeaninglist = dmeaningcleanup.split("; ")
    dmeaningenumerateoutput = []
    for x in enumerate(dmeaninglist, 1):
        dmeaningenumerateoutput.append(x)
    dmeaningstrconv = tuple(map(str, dmeaningenumerateoutput))
    dmeaningtuplejoin = ["".join(tups) for tups in dmeaningstrconv]
    dmeaningcleanuplist1 = []
    for x in dmeaningtuplejoin:
        y = x[1:][:-1]
        y = y.replace(",", " -")
        y = y.replace("'", "")
        y = capitalizexindex(y, 4)
        dmeaningcleanuplist1.append(y)
    dmeaning = "\n".join(dmeaningcleanuplist1)
    return(defquery.upper() + ":\n" + dmeaning)