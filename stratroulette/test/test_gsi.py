import unittest

from stratroulette.gsi import is_freezetime, get_map, get_team, verify_token


class TestIsFreezetime(unittest.TestCase):
    def test_is_long_freezetime(self):
        # given
        datas = [
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
        for data in datas:
            self.assertTrue(is_freezetime(data))

    def tset_is_not_long_freezetime(self):
        # given
        datas = [
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
        for data in datas:
            self.assertFalse(is_freezetime(data))

    def test_is_short_freezetime(self):
        # given
        data = {
            "map": {"phase": "live"},
            "round": {"phase": "freezetime"},
            "previously": {"round": {"phase": "over"}},
        }

        # when/then
        self.assertTrue(is_freezetime(data))

    def test_is_not_short_freezetime(self):
        # given
        datas = [
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
        for data in datas:
            self.assertFalse(is_freezetime(data))


class TestGetMap(unittest.TestCase):
    def test_get_map(self):
        for de_map, mapp in {
            "de_mirage": "mirage",
            "de_cache": "cache",
            "de_inferno": "inferno",
        }.items():
            self.assertEqual(mapp, get_map({"map": {"name": de_map}}))


class TestGetTeam(unittest.TestCase):
    def test_get_team(self):
        for team in ["CT", "T"]:
            self.assertEqual(team, get_team({"player": {"team": team}}))


class TestVerifyToken(unittest.TestCase):
    def test_verify_token(self):
        for token in ["abc", "def"]:
            self.assertTrue(verify_token({"auth": {"token": token}}, token))

    def test_do_not_verify_token(self):
        for data in [{"auth": {"token": "def"}}, {"auth": {}}, {}]:
            self.assertFalse(verify_token(data, "abc"))


if __name__ == "__main__":
    unittest.main()
