
import xml.etree.ElementTree as ET
import pytz
import re
import requests
from datetime import datetime



from modules.randomhelpers import getWebSourceHTML, genErrorHandle
from modules.sqlHandler import sqlMektanixDevilDog
from modules.webquerytools.twitterscaper import getUserTweets


def feedReadMain(chanid, serverid, feed, keyword: str = '', defaultchanneloverride: bool = False, delete: bool = False):
    if doesFeedExist(feed):
        # keywords use OR logic
        databaseKeyword = getKeywordStr(feed)
        if keyword == 'clearkeys':
            writeKeyword('', feed, True)
            output = f"Keyword field cleared for {feed}"
        elif keyword == 'replace:':
            writeKeyword(keyword[8:].strip(), feed, True)
            output = f"Replaced keyword value '{databaseKeyword}' with  [{keyword}]"
        elif keyword == 'deletefeed':
            sqlMektanixDevilDog(purpose="deleterow", table="feeds", queryColumn="callsign", queryField=feed)
            output = (f"Feed {feed} deleted.")
        elif keyword == '<':
            databaseKeyword = getKeywordStr(feed)
            if databaseKeyword == '':
                output = f"Feed {feed} has no keywords assigned to eliminate."
            else:
                if '|' in databaseKeyword:
                    keyword = "|".join(databaseKeyword.split('|')[:-1])
                    writeKeyword(keyword, feed, True)
                    outappend = "Keyword is empty now!" if keyword == '' else f"Keyword value is now {keyword}"
                output = f"Tailing keyword term erased. {outappend}"
        elif keyword:
            writeKeyword(keyword, feed)
            output = f"New keyword written for {feed}! (Now '{databaseKeyword}|{keyword}')"
            
        else:
            output = f"Latest stored post I have for {feed}: {getFeedLink(feed)} \n(Updated semihourly)"
            print(output)
            print(getFeedLink(feed))
    else:
        print(f"CHANID {chanid}")
        print(f"SERVERID {serverid}")
        output = feedSqlWriteNew(feed, chanid, serverid, keyword)
    return(output)


def doesFeedExist(feed) -> bool:
    if sqlMektanixDevilDog(purpose='read', table='feeds', resultColumn='*', queryColumn="callsign", queryField=feed):
        print(f"feedreader: {feed} does exist")
        return True
    else:
        print(f"feedreader: {feed} doesnt exist")
        return False


def feedCheckAll() -> list:
    newNu = []
    allFeeds = sqlMektanixDevilDog(purpose="getall", table="feeds")
    for row in allFeeds:
        readDict = getFeedDict(row[0], row[2]) #gets feed dict with params from sql
        if dateDiffChecker(readDict['date'], row[3], row[2]): #checking if post is new
            if checkForKeyword(readDict['text'], row[0]): #checking for keyword if applicable
                feedSqlWriteUpdate(readDict)
                print(f"new post found for {readDict['callsign']}")
                if isRetweet(readDict['text']):
                    retweet = getRetweet(readDict['text'])
                    readDict['link'] = f"{readDict['callsign']} retweeted {retweet[1]}: {retweet[0]}"
                readDict['link'] = readDict['link'].replace("statuses","status")
                newNu.append(f"{readDict['link']}|{row[8]}|{row[7]}|{row[9]}")
    return(newNu)

def getFeedLink(feed):
    feedGet = sqlMektanixDevilDog(purpose="read", table="feeds", resultColumn="link", queryColumn="callsign", queryField=feed)[0]
    return(feedGet)


def dateDiffChecker(feedDate, sqlDate, type) -> bool:
    newPost = False
    if type == 'rss':
        feedDate = getDateTimeFromFeed(feedDate, type)
    elif type == 'tweet':
        feedDate = feedDate.replace(tzinfo=pytz.UTC)
    sqlDate =  getDateTimeFromFeed(sqlDate, type)
    if feedDate > sqlDate:
        newPost = True

    return(newPost)

def getFeedDict(feed, type: str = 'tweet'):
    if "twitter.com" in feed:
        feed = feed.split('m/')[1]
    if type == 'rss':
        feedDict = getRSSDict(feed) #takes url
    elif type == 'tweet':
        if feed.startswith("@"):
            feed = feed[1:]
        feedDict = getTweetDict(feed) #takes twitter name
    return(feedDict)
    
def getTweetDict(twitter_name: str):
    try:
        tweet = getUserTweets(twitter_name, 1)[0]
        print(f"tweet: {tweet}")
    except Exception as e:
        return(genErrorHandle(e))
    tweetDict = {}
    tweetDict['callsign'] = twitter_name
    print(f'tweet jere\n{tweet}')
    tweetDict['text'] = re.sub(r"’|'|\"", r"\'", tweet.text)
    # tweetDict['text'] = (tweet.text).replace('’','')
    tweetDict['date'] = tweet.created_at
    tweetDict['type'] = 'tweet'
    tweetDict['link'] = f'https://twitter.com/twitter/statuses/{tweet.id}'
    print(f"exiting with tweetDict for {twitter_name}\n{tweetDict}")
    return(tweetDict)

def getRSSDict(url):
    try:
        responseStr = (getWebSourceHTML(url)).content
        responseXML = ET.fromstring(responseStr)
        outerXML = responseXML.find('channel')
        innerXML = outerXML.find('item')
    except Exception as e:
        return(genErrorHandle(e))
    rssDict = {}
    rssDict['callsign'] = url
    rssDict['type'] = 'rss'
    rssDict['text'] = (innerXML.find('title').text).replace("'",r"\'")
    rssDict['date'] = innerXML.find('pubDate').text

    #rssDict['date'] = datetime.strptime((innerXML.find('pubDate').text)[5:-4], "%d %b %Y %H:%M:%S")
    #example incoming str: "Tue, 29 Nov 2022 00:50:50 GMT"
    rssDict['description'] = innerXML.find('description').text
    rssDict['link'] = innerXML.find('link').text
    print(f"exiting with rssDict for {url}\n{rssDict}")
    return(rssDict)

def feedSqlWriteNew(url, chanid, serverid, keyword: str = '', defaultchanoverride: bool = False):
    feedDict = getFeedDict(url)
    if defaultchanoverride:
        defaultchanoverride = 1
    else:
        defaultchanoverride = 0
    if not type(feedDict) is dict:
        return("Error getting data for that one. Check spelling, and if you are sure, the bot is just broke.")
    else:   
        cursorResult = sqlMektanixDevilDog(purpose='insert', table='feeds', 
        insertColumn="(callsign,feedtext,feedtype,lastread,link,keyword,fromchannel,fromserver,fromchanneloverride)", insertData=f"('{feedDict['callsign']}', '{feedDict['text']}', '{feedDict['type']}', '{feedDict['date']}', '{feedDict['link']}', '{keyword}', {chanid}, {serverid}, {defaultchanoverride})")
        dupe = dupeChecker(cursorResult.fetchwarnings())
        if dupe:
            return(f"{url} is already saved.")
        else:
            return(f"New write successful for {url}")



def feedSqlWriteUpdate(feedDict: dict):
    cursorResult = sqlMektanixDevilDog(purpose='update', table='feeds', resultColumn='feedtext,lastread,link', queryColumn='callsign', queryField=(feedDict['callsign']), insertData=f'"{feedDict["text"]}", "{feedDict["date"]}", "{feedDict["link"]}"')


def getDateTimeFromFeed(datestr, type: str = 'rss') -> datetime:
    if type == 'rss':
        feedDate = datetime.strptime(datestr[5:-4], "%d %b %Y %H:%M:%S")
    elif type == 'tweet':
        feedDate = (datetime.strptime(datestr[:-6], "%Y-%m-%d %H:%M:%S")).replace(tzinfo=pytz.UTC)
    return(feedDate)

def dupeChecker(warningResponse) -> bool:
    dupe = False
    if warningResponse is not None:
        if warningResponse[0][1] == 1062:
            dupe = True
    return dupe

def isRetweet(text: str) -> bool:
    if text.startswith('RT @'):
        return True
    else:
        return False

def getRetweet(text: str) -> tuple:
    textUrl = re.search(r'https://t.co/\w+', text).group(0)
    tweeter = re.search(r'RT (@\w+)', text).group(1)
    tweet_r = requests.get(textUrl)
    tweet_url = tweet_r.url
    media_types = ['photo', 'animated_gif']
    media_check = next((media for media in media_types if media in tweet_url), False)
    if media_check:
        tweet_url = tweet_url.split(media_check)[0]
    return(tweet_url, tweeter)



def checkForKeyword(text: str, feedcallsign: str) -> bool:
    keyword = getKeywordStr(feedcallsign)
    if keyword == '': 
        # '' is default for this field in sql
        return True
    else:
        keywords = [term for term in keyword.split('|') if term != '']
        for item in keywords:
            if item in text.lower():
                return True
            else:
                return False


def getKeywordStr(feedcallsign: str) -> str:
    queryResult = (sqlMektanixDevilDog(purpose="read", table="feeds", resultColumn="keyword", queryColumn="callsign", queryField=feedcallsign))
    if queryResult is None:
        keyword = ''
    else:
        keyword = queryResult[0]
    return(keyword)




def writeKeyword(keyword: str, feedcallsign: str, replace: bool = False):
    """
    This writes keywords to the 'keyword' filed in sql. If replace is True, it will replace whatever is there. If it's not (default), it will use an append instead. To clear, keyword = '' and replace = True should be used.
    """
    print("feedcallsign: " + feedcallsign)
    if keyword != '': 
        keyword = '|' + keyword
    if replace:
        purpose = 'update'
        keyword = f'"{keyword}"'
    else: 
        purpose = 'append'
    cursorResult = sqlMektanixDevilDog(purpose=purpose, table='feeds', resultColumn='keyword', queryColumn='callsign', queryField=feedcallsign, insertData=keyword)




# feedSqlWriteNew('https://twitter.com/PlayOverwatch')