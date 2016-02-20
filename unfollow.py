__author__ = 'MarkJRust'
import tweepy
import easygui as eg
import sys

consumer_key = 	""
consumer_secret = ""
access_token = ""
access_token_secret = ""
twitter_handle = "YourHandle"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def getAndPrintFollowers(twitterHandle):
    eg.msgbox("Please wait while all of your followers are loaded")
    users = tweepy.Cursor(api.followers, screen_name=twitterHandle).items()
    userList =[];
    for user in users:
        userList.append(user.screen_name)
    question = "Who do you not want following you anymore? We will block and unblock them to remove the connection"
    title = "Potential Unfollower"
    choice = eg.multchoicebox(question, title, userList)
    return choice

def block(unfollowers):
    try:
        for user in unfollowers:
            api.create_block(user)
    except:
        eg.msgbox("Program killed")
        sys.exit()

def unblock(unfollowers):
    try:
        for user in unfollowers:
            api.destroy_block(user)
    except:
        eg.msgbox("Program killed")
        sys.exit()

unfollowers = getAndPrintFollowers(twitter_handle)
block(unfollowers)
eg.msgbox("Done blocking users, please wait during the unblocking process")
unblock(unfollowers)
eg.msgbox("Done unblocking users, finished")








