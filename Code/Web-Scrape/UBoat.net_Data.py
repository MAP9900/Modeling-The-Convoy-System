#Imports
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time

#Web Scrape Bot
chromedriver_path = '/usr/local/bin/chromedriver'
service = Service(executable_path=chromedriver_path)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://uboat.net/ops/convoys/convoys.php?convoy=ON-134')
wait = WebDriverWait(driver, 5)
table = driver.find_element(By.TAG_NAME, 'table')
data = []
rows = table.find_elements(By.TAG_NAME, 'tr')
for row in rows:
    cells = row.find_elements(By.TAG_NAME, 'td')
    for cell in cells:
        text = cell.text
        if text: 
            convoy, ships_sunk = text.split(' (')
            ships_sunk = ships_sunk[:-1] 
            data.append((convoy, int(ships_sunk)))

df = pd.DataFrame(data, columns=['Convoy', 'Ships Sunk'])
driver.quit()
#print(df.head())
#df.to_excel('UBoat.net_Ships_Sunk_Data.xlsx')