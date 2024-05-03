from threading import Thread

import nest_asyncio
from discord import Client, Intents, FFmpegPCMAudio
from flask import Flask, request

from stratroulette.config import BOT_TOKEN, CHANNEL_ID, GSI_TOKEN, FFMPEG_EXE
from stratroulette.gsi import GsiData
from stratroulette.strats import generate_strat
from stratroulette.tts import generate

nest_asyncio.apply()

# region {Flask app...}
app = Flask(__name__)


@app.post("/")
async def _():
    json = request.get_json()
    bot.loop.create_task(process(json))
    return "", 202


# endregion


# region {Discord bot...}
class StratRouletteBot(Client):
    channel = voice_client = None

    async def on_ready(self):
        self.channel = self.get_channel(CHANNEL_ID)
        self.voice_client = await self.channel.connect()
        await self.send("Let's play Strat Roulette!")

    async def send(self, msg):
        await self.channel.send(msg)

    async def play(self, source):
        self.voice_client.play(
            FFmpegPCMAudio(
                executable=FFMPEG_EXE,
                source=source,
            )
        )


bot = StratRouletteBot(intents=Intents.default())
# endregion


async def process(json):
    data = GsiData(json)

    if not data.verify_token(GSI_TOKEN):
        return

    if data.is_freezetime():
        strat = get_strat(data)
        await send_text(strat)
        await play_speech(strat)
    # TODO elif is_new_game(data):


def get_strat(data):
    mapp = data.get_map()
    team = data.get_team()
    return generate_strat(mapp, team)


async def send_text(strat):
    text_strat = f"# {strat['title']}\n{strat['desc']}"
    await bot.send(text_strat)


async def play_speech(strat):
    voice_strat = f"{strat['title']}!\n{strat['desc']}"
    speech = generate(voice_strat)
    await bot.play(speech)


if __name__ == "__main__":
    t1 = Thread(target=lambda: bot.run(BOT_TOKEN))
    t2 = Thread(target=lambda: app.run())

    t1.start()
    t2.start()
    t1.join()
