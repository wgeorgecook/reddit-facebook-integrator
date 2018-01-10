# DB Models
from peewee import *
from settings import *


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

class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = psql_db

class RedditInfo(BaseModel):
    post_url = CharField(max_length=255)
    post_title = CharField(max_length=255)
    post_id = CharField(max_length=50)
