import urllib.request as r
from bs4 import BeautifulSoup as bs

def udget(query):
    print(f"udget with query: [{query}]")
    try:
        query = query.replace(" ", "%20")
        udhtml = r.urlopen(f"https://www.urbandictionary.com/define.php?term={query}")
        udsoup = bs(udhtml.read(), 'html.parser')
        udmeaning = udsoup.findAll("div", "meaning")
        result = udmeaning[0].get_text().replace("\n","").replace("&apos","'")
    except:
        result = f"can't find '{query}' my friend"
    return(result)
    
