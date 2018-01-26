# Uses PeeWee to update DB with Twitter IDs
from peewee import *
from settings import *
from datetime import datetime
from lib.psql.models import RedditInfo

dbconnection = DB_SETTINGS.get('db')
dbuser = DB_SETTINGS.get('user')
dbpass = DB_SETTINGS.get('password')
dbhost = DB_SETTINGS.get('host')
psql_db = PostgresqlDatabase(
    dbconnection,
    user=dbuser,
    password=dbpass,
    host=dbhost,
    )

class DB(object):
    """
    Connects to a Postgresl database.
    Searches database for the upvoted post ID
    and returns True/False based on findings

    """

    def __init__(self, post_id, post_title, post_url):
        self.db = psql_db
        self.post_id = post_id
        self.post_title = post_title
        self.post_url = post_url
        


    def open_connection(self):
        self.db.connect()
        return "Connection to {} open.".format(dbconnection)

    def close_connection(self):
        self.db.close()
        return "Connection to {} closed.".format(dbconnection)

    def rollback_txn(self):
        self.db.rollback()

    def post_upvote_info(self):

        # if self.search_posts(self.post_id) is False:
        self.open_connection()
        posting = RedditInfo(
            
            post_id=self.post_id,
            post_url=self.post_url,
            post_title=self.post_title,

        )
        posting.save()

        self.close_connection()

    def search_posts(self, post_id):
        try:
            if RedditInfo.get(RedditInfo.post_id == post_id):
                return True
                
        except:
            return False
            
