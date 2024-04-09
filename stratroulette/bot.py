from threading import Thread

import discord
import nest_asyncio
from flask import Flask, request

from stratroulette.config import bot_token, gsi_token
from stratroulette.strats import get_strat_if_freezetime

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

t1 = Thread(target=lambda: bot.run(bot_token))
t2 = Thread(target=lambda: app.run())

if __name__ == "__main__":
    t1.start()
    t2.start()
    t1.join()
