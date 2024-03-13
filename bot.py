import os

import discord
from flask import Flask

from scraper import get_strat

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


class StratRouletteBot(discord.Client):
    async def on_ready(self):
        strat = get_strat("???", "CT")
        channel = self.get_channel(1217427654098026600)
        await channel.send(strat)


bot = StratRouletteBot(intents=None)
token = os.environ.get("STRAT_ROULETTE_BOT_TOKEN")
bot.run(token)