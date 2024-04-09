import configparser
import os

from discord import SyncWebhook
from flask import Flask, request

from stratroulette.strats import get_strat_if_freezetime

config = configparser.ConfigParser()
config.read("../config.ini")
webhook_id = config.getint("Webhook", "id")
webhook_token = config.get("Webhook", "token", vars=os.environ)
gsi_token = config.get("GSI", "token")

app = Flask(__name__)

webhook = SyncWebhook.partial(webhook_id, webhook_token)


@app.post("/")
def _():
    data = request.get_json()
    strat = get_strat_if_freezetime(data)
    if strat:
        webhook.send(strat)
    return ""


if __name__ == "__main__":
    app.run()
