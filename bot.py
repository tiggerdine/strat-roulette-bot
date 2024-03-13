import os

import discord


class StratRouletteBot(discord.Client):
    async def on_ready(self):
        channel = self.get_channel(1217427654098026600)
        await channel.send("test")


bot = StratRouletteBot(intents=None)
token = os.environ.get("STRAT_ROULETTE_BOT_TOKEN")
bot.run(token)
