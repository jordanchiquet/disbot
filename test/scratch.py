import urllib.request

def sky():
    print("sky called")
    url = "https://earthsky.org/tonight"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read()
    print("reqwuesrt succesful")
    print(html)


sky()