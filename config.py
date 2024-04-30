import os

API_ID = API_ID = 27184026

API_HASH = os.environ.get("API_HASH", "4c26e2cb6c6d9d57841b3c5ab6bb7605")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7054795757:AAE3qabaPLcBUFnahtaN0q0EeKnYpjguPGU-f48ELUCa0a3c")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 7183515722))

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7183515722").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


