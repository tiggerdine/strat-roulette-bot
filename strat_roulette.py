from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.get("https://strat-roulette.github.io")

ct_strat_button = driver.find_element(By.XPATH, "//button[text()='CT Strat']")


# TODO get_strat(map, side)
def get_strat(map):
    try:
        driver.find_element(By.XPATH, "//input[@value='{}']".format(map)).click()
    except NoSuchElementException:
        driver.find_element(By.XPATH, "//input[@value='null']").click()

    ct_strat_button.click()
    title = driver.find_element(By.ID, "title")
    desc = driver.find_element(By.ID, "desc")
    return {"title": title.text, "desc": desc.text}


for i in range(3):
    strat = get_strat("dust2")
    print(strat)

driver.quit()
