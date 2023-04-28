import tweepy #tweepy
import requests

import os

bearerKey = os.environ.get('TWITTERBEARER')

client = tweepy.Client(bearerKey)

def getIdByUsername(username: str):
    try:
        userObj = client.get_user(username=username)
        userid = userObj.data.id
    except tweepy.TweepyException as e:
        print(f"tweepy exception:[{e}]")
        userid = None
    return(userid)

def getUserTweets(username:str, tweetcount: int):
    userid = getIdByUsername(username)
    if userid is None:
        getUserTweetsOutput = ("getUserTweets: error in getting userid from getIdByUsername. see exception detail above.")

    else:
        if tweetcount < 5:
            maxtweets = 5
        else:
            maxtweets = tweetcount
        tweets = client.get_users_tweets(id=userid, max_results=maxtweets, exclude=["replies"], tweet_fields=["created_at"])
        getUserTweetsOutput = tweets.data[:tweetcount+1]


    return(getUserTweetsOutput)



r = requests.get('https://t.co/QSaJQSPCGU')

print(r.url)


