import asyncio
import time
from threading import Thread

from discord import Client, Intents, FFmpegPCMAudio
from flask import Flask, request

from stratroulette.config import BOT_TOKEN, CHANNEL_ID, GSI_TOKEN, GSI_PORT, FFMPEG_EXE
from stratroulette.gsi import Data
from stratroulette.strats import generate_strat
from stratroulette.tts import generate

# region {Flask app...}
app = Flask(__name__)


@app.post("/")
def _():
    json = request.get_json()
    asyncio.run_coroutine_threadsafe(process(json), bot.loop)
    return "", 202


# endregion


# region {Discord bot...}
class StratRouletteBot(Client):
    channel = voice_client = None

    async def on_ready(self):
        self.channel = self.get_channel(CHANNEL_ID)
        self.voice_client = await self.channel.connect()

    async def send(self, content):
        await self.channel.send(content)

    def play(self, source):
        self.voice_client.play(
            FFmpegPCMAudio(
                executable=FFMPEG_EXE,
                source=source,
            )
        )


bot = StratRouletteBot(intents=Intents.default())
# endregion


async def process(json):
    data = Data(json)

    if not data.has_token(GSI_TOKEN):
        return

    if data.is_freezetime():
        strat = generate_strat(data.get_map(), data.get_team())
        await send_strat(strat)
        play_strat(strat, data.is_long_freezetime())


async def send_strat(strat):
    await bot.send(f"# {strat['title']}\n{strat['desc']}")


def play_strat(strat, wait_for_team_intro):
    speech = generate(f"{strat['title']}!\n{strat['desc']}")
    if wait_for_team_intro:
        time.sleep(7)
    bot.play(speech)


if __name__ == "__main__":
    t1 = Thread(target=lambda: bot.run(BOT_TOKEN))
    t2 = Thread(target=lambda: app.run(port=GSI_PORT))

    t1.start()
    t2.start()
    t1.join()
