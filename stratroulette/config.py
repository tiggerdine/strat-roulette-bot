import configparser
import os

config = configparser.ConfigParser()
config.read("../config/config.ini")

BOT_TOKEN = config.get("Bot", "token", vars=os.environ)
GSI_TOKEN = config.get("GSI", "token")
