# Autor Lorenz Dang
# Dieses Programm benötigt zusätzliche packages, i.e. Selenium Webdriver u. Firefox oder Chrome Browserdriver
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# einrichten des Browserdrivers
options = Options()
# options.set_headless(headless=True)
driver = webdriver.Chrome(options=options, executable_path=os.path.join("..", "ICD_10_Scraper/chromedriver_for_mac"))
wait = WebDriverWait(driver, 120)
# Startwebseite wird aufgerufen
driver.get("http://apps.who.int/classifications/icd10/browse/2016/en")

# diese methode findet links der Überkapitel mit allen römischen Paragraphen
linkliste = driver.find_elements_by_css_selector("td:last-child a")
idliste = []

print(str(linkliste))

def neuladen(driver, url):
   while  str(driver.current_url)!=str(url):
       driver.get(str(url))
       print("current: " + str(driver.current_url) + " url: " + str(url))
       time.sleep(5)

# diese methode zieht mit der get_attribut methode alle römischen paragraphen isoliert raus
for e in linkliste:
    idliste.append(e.get_attribute("data-id"))

print(str(idliste))

# idliste mit allen elementen ohne dem erste, da das erste element 'root' irrelevant ist
idliste = idliste[1:]
#nur zum testen
#idliste = idliste[:1]
fid = []

# diese methode hängt hinter den untenstehenden link alle Elemente von idliste an und sucht so nach den finalen webseiten mit den icd10 codes, nebenbei wird die methode neuladen eingesetzt
# diese neuladenmethode wiederholt den zugriff auf die webpage bei einem timeout
for i in idliste:
    driver.get("http://apps.who.int/classifications/icd10/browse/2016/en/GetConcept?ConceptId=" + str(i))
#    time.sleep(5)
    neuladen(driver, "http://apps.who.int/classifications/icd10/browse/2016/en/GetConcept?ConceptId=" + str(i))
#    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "li a")))
    templist = driver.find_elements_by_css_selector("li a")
    for x in templist:
      #  time.sleep(5)
        l = x.get_attribute("href")
        fid.append(l[l.index('#/'):].replace('#/', ''))
        #fid.append(x.get_attribute("href").replace('#/', ''))

#print(str(templist))
print(str(fid))

end = []
second = []
for i in fid:
    driver.get("http://apps.who.int/classifications/icd10/browse/2016/en/GetConcept?ConceptId=" + str(i))
    neuladen(driver, "http://apps.who.int/classifications/icd10/browse/2016/en/GetConcept?ConceptId=" + str(i))
    end.append("http://apps.who.int/classifications/icd10/browse/2016/en/GetConcept?ConceptId=" + str(i))
    diseasesList = driver.find_elements_by_css_selector("h4, h5")
    for xs in diseasesList:
        element = str(xs.find_element_by_css_selector("a").text) + "; " + str(xs.find_element_by_css_selector("span").text)
        second.append(element)

# nur zum testen
#fid = fid[:1]

print(str(end))
print(str(second))

# schreibt liste in .csv datei
f = open("WHO_ICD10_Codes.csv","w+")
for i in second:
    f.write(str(i) + "\n")

f.close()

print(str("Done!"))
