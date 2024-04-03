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
