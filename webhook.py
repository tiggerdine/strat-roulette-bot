from discord import SyncWebhook
from flask import Flask, request
import os

from strats import get_strat

app = Flask(__name__)

token = os.environ.get("STRAT_ROULETTE_WEBHOOK_TOKEN")
webhook = SyncWebhook.partial(1217503787485368461, token)


@app.route("/", methods=["POST"])
async def handle():
    data = request.get_json()
    if is_freezetime(data):
        map = get_map(data)
        team = get_team(data)
        strat = get_strat(map, team)
        webhook.send(strat)
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


def get_map(data):
    return str(data["map"]["name"]).removeprefix("de_")


def get_team(data):
    return data["player"]["team"]
