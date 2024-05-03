import configparser
import os

config = configparser.ConfigParser()
config.read("../config/config.ini")

# Discord
BOT_TOKEN = config.get("Discord", "bot_token", vars=os.environ)
CHANNEL_ID = int(config.get("Discord", "channel_id"))

# GSI
GSI_TOKEN = config.get("GSI", "token")

# FFmpeg
FFMPEG_EXE = config.get("FFmpeg", "exe")