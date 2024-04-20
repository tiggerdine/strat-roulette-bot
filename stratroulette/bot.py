from threading import Thread

import discord
import nest_asyncio
from flask import Flask, request

from stratroulette.config import bot_token, gsi_token
from stratroulette.gsi import verify_token, is_freezetime, get_map, get_team
from stratroulette.strats import get_strat

nest_asyncio.apply()

app = Flask(__name__)


@app.post("/")
async def _():
    data = request.get_json()
    strat = get_strat_if_freezetime(data, gsi_token)
    if strat:
        bot.loop.run_until_complete(bot.send(strat))
    return ""


class StratRouletteBot(discord.Client):
    async def on_ready(self):
        await self.send("Let's play Strat Roulette!")

    async def send(self, msg):
        channel = self.get_channel(1217427654098026600)
        await channel.send(msg)


bot = StratRouletteBot(intents=discord.Intents.default())


def get_strat_if_freezetime(data, token):
    if verify_token(data, token) and is_freezetime(data):
        mapp = get_map(data)
        team = get_team(data)
        strat = get_strat(mapp, team)
        formatted_strat = format_strat(strat)
        return formatted_strat


def format_strat(strat):
    return "# {}\n{}".format(strat["title"], strat["desc"])


if __name__ == "__main__":
    t1 = Thread(target=lambda: bot.run(bot_token))
    t2 = Thread(target=lambda: app.run())

    t1.start()
    t2.start()
    t1.join()
