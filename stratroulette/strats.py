from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from stratroulette.gsi import is_freezetime, get_map, get_team, verify_token

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.get("https://strat-roulette.github.io")


def get_strat_if_freezetime(data, gsi_token):
    if verify_token(data, gsi_token) and is_freezetime(data):
        mapp = get_map(data)
        team = get_team(data)
        strat = get_strat(mapp, team)
        formatted_strat = format_strat(strat)
        return formatted_strat


def get_strat(mapp, team):
    try:
        find_map_button(mapp).click()
    except NoSuchElementException:
        driver.find_element(By.XPATH, "//input[@value='null']").click()

    find_team_button(team).click()
    title = driver.find_element(By.ID, "title")
    desc = driver.find_element(By.ID, "desc")
    return {"title": title.text, "desc": desc.text}


def find_map_button(mapp):
    return driver.find_element(By.XPATH, "//input[@value='{}']".format(mapp))


def find_team_button(team):
    return driver.find_element(By.XPATH, "//button[text()='{} Strat']".format(team))


def format_strat(strat):
    return "# {}\n{}".format(strat["title"], strat["desc"])


if __name__ == "__main__":
    for i in range(10):
        strat = get_strat("dust2", "T")
        print(strat)

    driver.quit()
