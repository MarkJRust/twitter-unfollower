__author__ = 'MarkJRust'
import tweepy
from Tkinter import *
import tkMessageBox
import Tkinter


consumer_key = 	""
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
        CBs = Checkbutton(topWindow, text=user.screen_name)
        CBs.pack()


#def getSelectedCheckboxes():


topWindow = Tkinter.Tk()
Lb1= Listbox(topWindow)

getAndPrintFollowers("MHacks7Test")
#getSelectedCheckboxes()

Lb1.pack()
topWindow.mainloop()
print("Done fetching and printing followers")








