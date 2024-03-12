from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.get("https://strat-roulette.github.io")

ct_strat_button = driver.find_element(By.XPATH, "//button[text()='CT Strat']")
ct_strat_button.click()

title = driver.find_element(By.ID, "title")
print(title.text)

desc = driver.find_element(By.ID, "desc")
print(desc.text)

driver.quit()
