class Data:
    json = None

    def __init__(self, json):
        self.json = json

    def is_freezetime(self):
        return self.is_long_freezetime() or self.is_short_freezetime()

    def is_long_freezetime(self):
        try:
            if (
                self.json["map"]["phase"] == "live"
                and self.json["round"]["phase"] == "freezetime"
                and self.json["previously"]["map"]["phase"]
                in ["warmup", "intermission"]
            ):
                return True
        except KeyError:
            pass

    def is_short_freezetime(self):
        try:
            if (
                self.json["map"]["phase"] == "live"
                and self.json["round"]["phase"] == "freezetime"
                and self.json["previously"]["round"]["phase"] == "over"
            ):
                return True
        except KeyError:
            pass

    def get_map(self):
        return str(self.json["map"]["name"]).removeprefix("de_")

    def get_team(self):
        return self.json["player"]["team"]

    def has_token(self, token):
        try:
            if self.json["auth"]["token"] == token:
                return True
        except KeyError:
            pass
