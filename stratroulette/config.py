import configparser
import os

config = configparser.ConfigParser()
config.read("../config/config.ini")

# Discord
BOT_TOKEN = config.get("Discord", "bot_token", vars=os.environ)
CHANNEL_ID = int(config.get("Discord", "channel_id"))

# GSI
GSI_TOKEN = config.get("GSI", "token")
GSI_PORT = config.get("GSI", "port")

# FFmpeg
FFMPEG_EXE = config.get("FFmpeg", "exe")

# TTS
TTS = config.get("TTS", "tts")
ELEVENLABS_API_KEY = config.get("TTS", "elevenlabs_api_key", vars=os.environ)
