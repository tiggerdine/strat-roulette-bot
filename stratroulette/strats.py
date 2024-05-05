from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

BLACKLIST = ["Double or Nothing"]

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.get("https://strat-roulette.github.io")


def generate_strat(mapp, team):
    try:
        find_map_button(mapp).click()
    except NoSuchElementException:
        driver.find_element(By.XPATH, "//input[@value='null']").click()

    team_button = find_team_button(team)
    while True:
        team_button.click()
        title = driver.find_element(By.ID, "title")
        if title not in BLACKLIST:
            desc = driver.find_element(By.ID, "desc")
            break
    return {"title": title.text, "desc": desc.text}


def find_map_button(mapp):
    return driver.find_element(By.XPATH, "//input[@value='{}']".format(mapp))


def find_team_button(team):
    return driver.find_element(By.XPATH, "//button[text()='{} Strat']".format(team))
