# Facebook facing library

from fbchat import Client
from fbchat.models import *
from settings import FACEBOOK_SETTINGS
from lib.reddit.reddit import Reddinterface
import random
import datetime



class Facebookface(object):

    """
    Connects to Facebook using the credentials specified. Creates a dictionary of the 
    users the authenticating user messaged and returns the userID of a desired 
    contact you wish to message. Will then receive data from the Reddit libary
    and message the desired contact with the url and post title.
    """

    def __init__(self):
      self.client = Client(FACEBOOK_SETTINGS.get('email'), FACEBOOK_SETTINGS.get('password'))
      self.session_cookies = self.client.getSession()
      self.client.setSession(self.session_cookies)  
      self.username = FACEBOOK_SETTINGS.get('desired_username')
      self.redditing = Reddinterface()
      self.now = datetime.datetime.now()
      self.prompts = [
            "Neato!", 
            "Check out this thing I think is cool", 
            "How neat is that?", 
            "That's pretty neat!", 
            "Check it",
            "Is this spam good enough?",
            "Can you feel it now, Mr. Krabs?",
            "If you don't like this, the communists win"
            ]

    def get_fb_users(self):
        user_list = [self.client.fetchAllUsers()]
        user_dict = {}
        for user in user_list[0]: # List only predictable when using the zeroth index
            user_dict.update({user.name:user.uid})
        return user_dict[self.username]

    def send_message(self):
        if self.redditing.check_upvotes() is False:
            print("######### Time is {} #########".format(self.now.strftime("%m/%d/%Y %H:%M")))
            print("Will not send duplicate message")
        else:
            self.client.send(Message(text='{} \n\n{}\n{}'.format(random.choice(self.prompts),  self.redditing.get_title(), self.redditing.get_url())), thread_id=self.get_fb_users(), thread_type=ThreadType.USER)
            self.client.logout()
            print("######### Time is {} #########".format(self.now.strftime("%m/%d/%Y %H:%M")))
            print("Message sent to {}".format(self.username))
            print("##############################")
