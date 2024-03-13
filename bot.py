import os

import discord
from flask import Flask, request

from scraper import get_strat


class StratRouletteBot(discord.Client):
    async def on_ready(self):
        strat = get_strat("???", "CT")
        channel = self.get_channel(1217427654098026600)
        await channel.send(strat)


bot = StratRouletteBot(intents=None)
token = os.environ.get("STRAT_ROULETTE_BOT_TOKEN")
bot.run(token)

app = Flask(__name__)


@app.route("/", methods=["POST"])
def consume():
    data = request.get_json()
    if is_freezetime(data):
        print("freezetime")
    return ""


def is_freezetime(data):
    return is_long_freezetime(data) or is_short_freezetime(data)


def is_long_freezetime(data):
    try:
        if (
            data["map"]["phase"] == "live"
            and data["round"]["phase"] == "freezetime"
            and data["previously"]["map"]["phase"] in ["warmup", "intermission"]
        ):
            return True
    except KeyError:
        pass


def is_short_freezetime(data):
    try:
        if (
            data["map"]["phase"] == "live"
            and data["round"]["phase"] == "freezetime"
            and data["previously"]["round"]["phase"] == "over"
        ):
            return True
    except KeyError:
        pass
