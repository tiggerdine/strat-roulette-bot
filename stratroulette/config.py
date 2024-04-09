import configparser
import os

config = configparser.ConfigParser()
config.read("../config/config.ini")
bot_token = config.get("Bot", "token", vars=os.environ)
gsi_token = config.get("GSI", "token")
