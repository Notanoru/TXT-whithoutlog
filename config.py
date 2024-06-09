import os

API_ID = API_ID = 25120174

API_HASH = os.environ.get("API_HASH", "89a10ea368b634194752731a7c405e30")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7177898659:AAHvM5KKzCAdWsjdG5ApKxU5q4qBXPy9rbg")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5477824201))

LOG = -1009147483647

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5477824201").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


