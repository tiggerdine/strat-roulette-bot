import unittest

from stratroulette.gsi import GsiData


class TestIsFreezetime(unittest.TestCase):
    def test_is_long_freezetime(self):
        # given
        jsons = [
            {
                "map": {"phase": "live"},
                "round": {"phase": "freezetime"},
                "previously": {"map": {"phase": "warmup"}},
            },
            {
                "map": {"phase": "live"},
                "round": {"phase": "freezetime"},
                "previously": {"map": {"phase": "intermission"}},
            },
        ]

        # when/then
        for json in jsons:
            data = GsiData(json)
            self.assertTrue(data.is_freezetime())

    def test_is_not_long_freezetime(self):
        # given
        jsons = [
            {
                "map": {"phase": "bla"},  # Wrong map.phase
                "round": {"phase": "freezetime"},
                "previously": {"map": {"phase": "warmup"}},
            },
            {
                "map": {"phase": "live"},
                "round": {"phase": "bla"},  # Wrong round.phase
                "previously": {"map": {"phase": "intermission"}},
            },
            {
                "map": {"phase": "live"},
                "round": {"phase": "freezetime"},
                "previously": {"map": {"phase": "bla"}},  # Wrong previously.map.phase
            },
            {
                "map": {},  # Missing map.phase
                "round": {"phase": "freezetime"},
                "previously": {"map": {"phase": "warmup"}},
            },
            {},
        ]

        # when/then
        for json in jsons:
            data = GsiData(json)
            self.assertFalse(data.is_freezetime())

    def test_is_short_freezetime(self):
        # given
        json = {
            "map": {"phase": "live"},
            "round": {"phase": "freezetime"},
            "previously": {"round": {"phase": "over"}},
        }

        # when/then
        data = GsiData(json)
        self.assertTrue(data.is_freezetime())

    def test_is_not_short_freezetime(self):
        # given
        jsons = [
            {
                "map": {"phase": "bla"},  # Wrong map.phase
                "round": {"phase": "freezetime"},
                "previously": {"round": {"phase": "over"}},
            },
            {
                "map": {"phase": "live"},
                "round": {"phase": "bla"},  # Wrong round.phase
                "previously": {"round": {"phase": "over"}},
            },
            {
                "map": {"phase": "live"},
                "round": {"phase": "freezetime"},
                "previously": {
                    "round": {"phase": "bla"}
                },  # Wrong previously.round.phase
            },
            {
                "map": {},  # Missing map.phase
                "round": {"phase": "freezetime"},
                "previously": {"round": {"phase": "over"}},
            },
            {},
        ]

        # when/then
        for json in jsons:
            data = GsiData(json)
            self.assertFalse(data.is_freezetime())


class TestGetMap(unittest.TestCase):
    def test_get_map(self):
        for de_map, mapp in {
            "de_mirage": "mirage",
            "de_cache": "cache",
            "de_inferno": "inferno",
        }.items():
            data = GsiData({"map": {"name": de_map}})
            self.assertEqual(mapp, data.get_map())


class TestGetTeam(unittest.TestCase):
    def test_get_team(self):
        for team in ["CT", "T"]:
            data = GsiData({"player": {"team": team}})
            self.assertEqual(team, data.get_team())


class TestVerifyToken(unittest.TestCase):
    def test_verify_token(self):
        for token in ["abc", "def"]:
            data = GsiData({"auth": {"token": token}})
            self.assertTrue(data.verify_token(token))

    def test_do_not_verify_token(self):
        for json in [{"auth": {"token": "def"}}, {"auth": {}}, {}]:
            data = GsiData(json)
            self.assertFalse(data.verify_token("abc"))


if __name__ == "__main__":
    unittest.main()
