# Facebook facing library

from fbchat import Client
from fbchat.models import *

from settings import FACEBOOK_SETTINGS


from lib.reddit.reddit import Reddinterface


class Facebookface(object):

    """
    Connects to Facebook using the credentials specified. Creates a dictionary of the 
    users the authenticating user messaged and returns the userID of a desired 
    contact you wish to message.
    """

    def __init__(self):
      self.client = Client(FACEBOOK_SETTINGS.get('email'), FACEBOOK_SETTINGS.get('password'))  
      self.username = FACEBOOK_SETTINGS.get('desired_username')
      self.redditing = Reddinterface()

    def get_fb_users(self):
        user_list = [self.client.fetchAllUsers()]
        user_dict = {}
        for user in user_list[0]: # List only predictable when using the zeroth index
            user_dict.update({user.name:user.uid})
        return user_dict[self.username]

    def send_message(self):
        self.client.send(Message(text='Check out this thing I think is cool: {}'.format(self.redditing.check_upvotes())), thread_id=self.get_fb_users(), thread_type=ThreadType.USER)
        self.client.logout()

