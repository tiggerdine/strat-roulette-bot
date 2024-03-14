from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.get("https://strat-roulette.github.io")


def get_strat(mapp, team):
    try:
        driver.find_element(By.XPATH, "//input[@value='{}']".format(mapp)).click()
    except NoSuchElementException:
        driver.find_element(By.XPATH, "//input[@value='null']").click()

    driver.find_element(By.XPATH, "//button[text()='{} Strat']".format(team)).click()
    title = driver.find_element(By.ID, "title")
    desc = driver.find_element(By.ID, "desc")
    return {"title": title.text, "desc": desc.text}


if __name__ == "__main__":
    for i in range(10):
        strat = get_strat("dust2", "T")
        print(strat)

    driver.quit()
