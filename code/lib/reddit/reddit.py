# Reddit interface

import praw
from settings import REDDIT_SETTINGS

class Reddinterface(object):
    
    def __init__(self):
        self.reddit = praw.Reddit(client_id=REDDIT_SETTINGS.get("client_id"), client_secret=REDDIT_SETTINGS.get("client_secret"), user_agent=REDDIT_SETTINGS.get("user_agent"), username=REDDIT_SETTINGS.get('username'), password=REDDIT_SETTINGS.get('password'))
        self.redditor1 = self.reddit.redditor(REDDIT_SETTINGS.get("username"))
        self.upvote_list = []

    def check_upvotes(self):
        for upv in self.redditor1.upvoted(limit=1):
            if upv.id not in self.upvote_list:
                print("{} recently upvoted".format(upv.title))
                print("Adding {} to the upvote list".format(upv.id))
                self.upvote_list.append(upv.id)
                return upv.url