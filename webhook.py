import aiohttp
from discord import Webhook
from flask import Flask, request
import os

from scraper import get_strat

app = Flask(__name__)
token = os.environ.get("STRAT_ROULETTE_WEBHOOK_TOKEN")


@app.route("/", methods=["POST"])
async def post():
    data = request.get_json()
    if is_freezetime(data):
        strat = get_strat("???", "CT")
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.partial(
                1217503787485368461,
                token,
                session=session,
            )
            await webhook.send(strat)
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
