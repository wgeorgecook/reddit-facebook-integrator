# Reddit interface

import praw
from lib.psql.update_db import DB
from settings import REDDIT_SETTINGS

class Reddinterface(object):
    
    def __init__(self):
        self.reddit = praw.Reddit(client_id=REDDIT_SETTINGS.get("client_id"), client_secret=REDDIT_SETTINGS.get("client_secret"), user_agent=REDDIT_SETTINGS.get("user_agent"), username=REDDIT_SETTINGS.get('username'), password=REDDIT_SETTINGS.get('password'))
        self.redditor1 = self.reddit.redditor(REDDIT_SETTINGS.get("username"))
        self.psql = DB(post_id=self.get_id(), post_title=self.get_title(), post_url=self.get_url())


    def check_upvotes(self):
        for upv in self.redditor1.upvoted(limit=1):
           if  self.psql.search_posts(upv.id) is True:
               print("Post already in database. Closing connection.")
               return False
           else:
                self.psql.post_upvote_info()
                return upv.url

           

    def get_url(self):
        for upv in self.redditor1.upvoted(limit=1):
            return upv.url

    def get_title(self):
        for upv in self.redditor1.upvoted(limit=1):
            return upv.title

    def get_id(self):
        for upv in self.redditor1.upvoted(limit=1):
            return upv.id
       

        
"""

Old method


    def check_upvotes(self):
        for upv in self.redditor1.upvoted(limit=1):
            if upv.id not in self.upvote_list:
                print("{} recently upvoted".format(upv.title))
                print("Adding {} to the upvote db".format(upv.id))
                self.upvote_list.append(upv.id)
                return upv.url
"""