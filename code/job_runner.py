# Runs the job

from lib.facebook.facebook import Facebookface
import datetime

now = datetime.datetime.now()
fb = Facebookface()


print("############ It is {}     ##########".format(now.strftime("%m/%d/%Y %H:%M")))
print("########### Begin Process ##########")
fb.send_message()
print("########### End Process ##########")