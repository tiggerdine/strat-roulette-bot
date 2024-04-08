import unittest

from selenium.webdriver.common.by import By

from stratroulette.strats import driver, find_map_button, find_team_button


class Test(unittest.TestCase):
    def test_maps(self):
        maps = [
            "mirage",
            "cache",
            "inferno",
            "overpass",
            "train",
            "nuke",
            "dust2",
            "null",
        ]

        map_btns = driver.find_elements(By.XPATH, "//input[@name='map']")
        self.assertEqual(len(map_btns), len(maps))

        for mapp in maps:
            find_map_button(mapp)

    def test_teams(self):
        teams = ["CT", "T"]

        team_btns = driver.find_elements(By.TAG_NAME, "button")
        self.assertEqual(len(team_btns), len(teams))

        for team in teams:
            find_team_button(team)


if __name__ == "__main__":
    unittest.main()
