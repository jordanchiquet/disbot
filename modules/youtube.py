import re
import urllib.parse
import urllib.request


def youtubesearch(query):
    ytquery = urllib.parse.urlencode({"search_query" : query})
    html_cont = urllib.request.urlopen("http://youtube.com/results?"+ytquery)
    ytresult = re.findall(r'href=\"\/watch\?v=(.{11})', html_cont.read().decode())
    return("https://youtu.be/" + ytresult[0])