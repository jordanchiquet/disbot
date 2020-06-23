import re
import urllib.parse
import urllib.request


def youtubesearch(query):
    print("starting youtube search with query: [" + query + "]")
    ytquery = urllib.parse.urlencode({"search_query" : query})
    html_cont = urllib.request.urlopen("http://youtube.com/results?"+ytquery)
    print("got youtube result")
    print("--------------")
    print(html_cont)
    ytresult = re.findall(r'href=\"\/watch\?v=(.{11})', html_cont.read().decode())
    return("https://youtu.be/" + ytresult[0])