import configparser
import os

config = configparser.ConfigParser()
config.read("../config.ini")

bot_token = config.get("Bot", "token", vars=os.environ)

webhook_id = config.getint("Webhook", "id")
webhook_token = config.get("Webhook", "token", vars=os.environ)

gsi_token = config.get("GSI", "token")
