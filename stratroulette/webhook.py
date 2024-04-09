from discord import SyncWebhook
from flask import Flask, request

from stratroulette.config import webhook_id, webhook_token, gsi_token
from stratroulette.strats import get_strat_if_freezetime

app = Flask(__name__)

webhook = SyncWebhook.partial(webhook_id, webhook_token)
webhook.send("Let's play Strat Roulette!")


@app.post("/")
def _():
    data = request.get_json()
    strat = get_strat_if_freezetime(data, gsi_token)
    if strat:
        webhook.send(strat)
    return ""


if __name__ == "__main__":
    app.run()
