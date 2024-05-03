class GsiData:
    data = None

    def __init__(self, data):
        self.data = data

    def is_freezetime(self):
        return self.is_long_freezetime() or self.is_short_freezetime()

    def is_long_freezetime(self):
        try:
            if (
                self.data["map"]["phase"] == "live"
                and self.data["round"]["phase"] == "freezetime"
                and self.data["previously"]["map"]["phase"]
                in ["warmup", "intermission"]
            ):
                return True
        except KeyError:
            pass

    def is_short_freezetime(self):
        try:
            if (
                self.data["map"]["phase"] == "live"
                and self.data["round"]["phase"] == "freezetime"
                and self.data["previously"]["round"]["phase"] == "over"
            ):
                return True
        except KeyError:
            pass

    def get_map(self):
        return str(self.data["map"]["name"]).removeprefix("de_")

    def get_team(self):
        return self.data["player"]["team"]

    def verify_token(self, token):
        try:
            if self.data["auth"]["token"] == token:
                return True
        except KeyError:
            pass
