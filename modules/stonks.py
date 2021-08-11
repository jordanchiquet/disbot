import yfinance
import json 


class getstock:
    def __init__(self, tickerquery):
        self.tickerquery = tickerquery.upper()

    def getcurrentprice(self):
        print("getting current stock price")
        print(yfinance)
    

getstockinit = getstock("amc")

getstockinit.getcurrentprice()