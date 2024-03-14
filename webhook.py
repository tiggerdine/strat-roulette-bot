import configparser
import os

from discord import SyncWebhook
from flask import Flask, request

from strats import get_strat

config = configparser.ConfigParser()
config.read("config.ini")

app = Flask(__name__)

webhook_id = config.getint("Webhook", "id")
webhook_token = config.get("Webhook", "token", vars=os.environ)
webhook = SyncWebhook.partial(webhook_id, webhook_token)


@app.route("/", methods=["POST"])
def _():
    data = request.get_json()
    if is_freezetime(data):
        mapp = get_map(data)
        team = get_team(data)
        strat = get_strat(mapp, team)
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


if __name__ == "__main__":
    app.run()
