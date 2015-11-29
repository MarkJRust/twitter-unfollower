__author__ = 'MarkJRust'
import tweepy

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def getAndPrintFollowers(twitterHandle):
    users = tweepy.Cursor(api.followers, screen_name=twitterHandle).items()
    for user in users:
        print(user.screen_name)

getAndPrintFollowers("MarkJRust")
print("Done fetching and printing followers")








