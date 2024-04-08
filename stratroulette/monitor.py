import unittest

from selenium.webdriver.common.by import By

from stratroulette.strats import driver


class Test(unittest.TestCase):
    def test(self):
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
        teams = ["CT", "T"]

        map_btns = driver.find_elements(By.XPATH, "//input[@name='map']")
        self.assertEqual(len(map_btns), len(maps))
        for btn in map_btns:
            self.assertIn(btn.get_property("value"), maps)

        team_btns = driver.find_elements(By.TAG_NAME, "button")
        self.assertEqual(len(team_btns), len(teams))
        for btn in team_btns:
            self.assertIn(btn.text.removesuffix(" Strat"), teams)


if __name__ == "__main__":
    unittest.main()
