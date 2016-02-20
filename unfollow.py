__author__ = 'MarkJRust'
import tweepy
import easygui as eg

consumer_key = 	""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def getAndPrintFollowers(twitterHandle):
    users = tweepy.Cursor(api.followers, screen_name=twitterHandle).items()
    userList =[];
    for user in users:
        userList.append(user.screen_name)
    question = "Who do you not want following you anymore? We will block and unblock them to remove the connection"
    title = "Potential Unfollower"
    listOfOptions = userList
    choice = eg.multchoicebox(question , title, listOfOptions)
    return choice

def block(unfollowers):
    for user in unfollowers:
        api.create_block(user)

def unblock(unfollowers):
    for user in unfollowers:
        api.destroy_block(user)

unfollowers = getAndPrintFollowers("MHacks7Test")
eg.msgbox("Done fetching and printing followers")
block(unfollowers)
eg.msgbox("Done blocking users")
unblock(unfollowers)
eg.msgbox("Done unblocking users")








