import os

import selenium
import self as self
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
# options.set_headless(headless=True)
driver = webdriver.Chrome(options=options, executable_path=os.path.join("..", "ICD_10_Scraper/chromedriver_for_mac"))
# Startwebseite wird aufgerufen
driver.get("https://www.jameda.de/erfurt/99084/aerzte/allgemein-u-hausaerzte/plz-fachaerzte/")

# driver.find_elements_by_css_selector('#app > div > div > div.sc-jUpvKA.cqFgQU > div.sc-cgzHhG.fqmUCB > div.sc-cZBZkQ.itEewc > div.sc-gbzWSY.cuZyoA > div.sc-jGxEUC.fbCvQw > button').click()
python_button = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[3]/div[2]/div[2]/div[3]/div[2]/button/span[2]')  # [0]
python_button.click()
