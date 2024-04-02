import configparser
import os

import discord

config = configparser.ConfigParser()
config.read("../config.ini")


class StratRouletteBot(discord.Client):
    async def on_ready(self):
        channel = self.get_channel(1217427654098026600)
        await channel.send("Hello, World!")


bot = StratRouletteBot(intents=discord.Intents.default())
token = config.get("Bot", "token", vars=os.environ)

if __name__ == "__main__":
    bot.run(token)
