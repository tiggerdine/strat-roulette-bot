from threading import Thread

import nest_asyncio
from discord import Client, Intents, FFmpegPCMAudio
from flask import Flask, request

from stratroulette.config import BOT_TOKEN, GSI_TOKEN
from stratroulette.gsi import verify_token, is_freezetime, get_map, get_team
from stratroulette.strats import generate_strat

nest_asyncio.apply()

# region {Flask app}
app = Flask(__name__)


@app.post("/")
async def _():
    data = request.get_json()
    bot.loop.run_until_complete(process(data))
    return ""


# endregion


# region {Discord bot}
class StratRouletteBot(Client):
    channel = voice_client = None

    async def on_ready(self):
        self.channel = self.get_channel(1217427654098026601)
        self.voice_client = await self.channel.connect()
        await self.send("Let's play Strat Roulette!")
        await self.play(
            "https://github.com/rafaelreis-hotmart/Audio-Sample-files/raw/master/sample.mp3"
        )

    async def send(self, msg):
        await self.channel.send(msg)

    async def play(self, source):
        self.voice_client.play(
            FFmpegPCMAudio(
                executable="C:/Users/Martin/Downloads/ffmpeg-2024-04-18-git-35ae44c615-essentials_build/bin/ffmpeg.exe",
                source=source,
            )
        )


bot = StratRouletteBot(intents=Intents.default())
# endregion


async def process(data):
    if not verify_token(data, GSI_TOKEN):
        return

    if is_freezetime(data):
        strat = get_strat(data)
        formatted_strat = format_strat(strat)
        await bot.send(formatted_strat)
    # TODO elif is_new_game(data):


def get_strat(data):
    mapp = get_map(data)
    team = get_team(data)
    return generate_strat(mapp, team)


def format_strat(strat):
    return f"# {strat['title']}\n{strat['desc']}"


if __name__ == "__main__":
    t1 = Thread(target=lambda: bot.run(BOT_TOKEN))
    t2 = Thread(target=lambda: app.run())

    t1.start()
    t2.start()
    t1.join()
