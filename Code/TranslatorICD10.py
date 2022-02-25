# Autor Lorenz Dang
# Dieses Programm benötigt zusätzliche packages, i.e. Selenium Webdriver u. Firefox oder Chrome Browserdriver
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

import csv

#einrichten des Browserdrivers
options = Options()
driver = webdriver.Chrome(options=options, executable_path=os.path.join("..", "ICD_10_Scraper/chromedriver_for_mac"))
wait = WebDriverWait(driver, 1000000)

# Startwebseite wird aufgerufen
driver.get("https://translate.google.com/?hl=en")
time.sleep(5)
with open('/users/lorenz/pycharmprojects/icd_10_scraper/Synonyme.csv') as csvfile:
    readcsv = csv.reader(csvfile, delimiter=';')
    icd10listSynonyms = []
    list = []
    for row in readcsv:
        list.append(str(row[0]) + ";" + str(row[1]))
        #icd10listSynonyms.append(row[0])
        icd10listSynonyms.append(str(row[0]) + ";" + str(row[1]))
   #     print(row[0] + str("\t") + row[1])

newList = []

#icd10listSynonyms = icd10listSynonyms[:20]
f = open("englishSynonyms.csv","w+")
try:
    for s in icd10listSynonyms:
        # driver.find_element_by_css_selector("#sugg-item-de").click()
        # driver.find_element_by_css_selector("#sugg-item-en").click()
        textbox = driver.find_element_by_id("source")
        textbox.clear()
        textbox.send_keys(s[s.index(';'):].replace(';', ''))
        translateButton = driver.find_element_by_css_selector("#gt-submit")
        translateButton.click()
        # x = str(driver.find_element_by_css_selector("#gt-res-dir-ctr").text)
        time.sleep(0.5)
        x = s + ";" + str(driver.find_element_by_css_selector("#gt-res-dir-ctr").text)
        print(x)
        newList.append(x)
        f.write(i + "\n")
except:
    print("There was an error")

f.close()
print("done")

#x = driver.find_element_by_css_selector("#result_box > span").text
#print(x)
