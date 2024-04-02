import configparser
import os
from threading import Thread

import discord
from flask import Flask

config = configparser.ConfigParser()
config.read("../config.ini")

app = Flask(__name__)


@app.post("/")
async def _():
    # FIXME RuntimeError: Timeout context manager should be used inside a task
    await bot.send("...")
    return ""


class StratRouletteBot(discord.Client):
    async def on_ready(self):
        await self.send("Let's play Strat Roulette!")

    async def send(self, msg):
        channel = self.get_channel(1217427654098026600)
        await channel.send(msg)


bot = StratRouletteBot(intents=discord.Intents.default())
token = config.get("Bot", "token", vars=os.environ)

t1 = Thread(target=lambda: bot.run(token))
t2 = Thread(target=lambda: app.run())

if __name__ == "__main__":
    t1.start()
    t2.start()
    t1.join()
    t2.join()
