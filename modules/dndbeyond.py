import urllib.request
from bs4 import BeautifulSoup


class dndbeyondsearch:
    def __init__(self, query, category: str = None):
        self.category = category
        if self.category is not None:
            self.category = category.lower()
        self.query = query.replace(" ", "-")
    
    def dndexecute(self):
        if self.category is None:
            return #add func here
        if self.category.startswith("item"):
            return(self.itemsearch())


    def itemsearch(self):
        "http://username:password@example.com/"
        itemurl = "https://www.dndbeyond.com/magic-items/" + self.query
    # try:
        itemget = urllib.request.urlopen(itemurl)
    # except:
        # print("url failed: [" + itemurl + "]")
        # return("inv")
        itemsoup = BeautifulSoup(itemget.read(), 'html.parser')
        print(itemsoup.prettify())


test = dndbeyondsearch("instrument of illusions", "item")
        
test.itemsearch()