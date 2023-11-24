#Imports
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time

#Used Already

#Web Scrape Bot
def OB_WebScrape():
    chromedriver_path = '/usr/local/bin/chromedriver'
    service = Service(executable_path=chromedriver_path)
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('http://www.convoyweb.org.uk/ob2/index.html')
    wait = WebDriverWait(driver, 5)
    #dropdown_menu = WebDriverWait(driver, 10).until(
        #EC.presence_of_element_located((By.NAME, 'menu'))) 
    driver.switch_to.frame('obside') #Switch to frame with menu
    dropdown = Select(driver.find_element(By.NAME, 'menu'))
    options = dropdown.options
    OB_data = pd.DataFrame()
    for index in range(1, len(options)):
        dropdown_value = options[index].text
        dropdown = Select(driver.find_element(By.NAME, 'menu'))
        dropdown.select_by_index(index)
        time.sleep(3) 
        driver.switch_to.default_content() 
        driver.switch_to.frame('obmain') #Switch to frame with the table
        tables = driver.find_elements(By.TAG_NAME, 'table')
        if len(tables) >= 2:
            correct_table = tables[1] #Ensure the correct table is accessed
        rows = correct_table.find_elements(By.TAG_NAME,'tr')
        data = []
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, 'td')
            cols = [ele.text.strip() for ele in cols]
            data.append(cols)
        df = pd.DataFrame(data[1:], columns=data[0])
        df['OB Convoy Number'] = dropdown_value  
        OB_data = pd.concat([OB_data, df], ignore_index=True)
        driver.switch_to.default_content()
        driver.switch_to.frame('obside') #Switch back to frame with menu to preform the loop
    #OB_data.to_excel('OB_Convoy_Data_1.xlsx')
    driver.quit()
    return OB_data
#print(OB_WebScrape().head()

def OB_Dates():
    chromedriver_path = '/usr/local/bin/chromedriver'
    service = Service(executable_path=chromedriver_path)
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('http://www.convoyweb.org.uk/ob2/index.html')
    wait = WebDriverWait(driver, 5)
    driver.switch_to.frame('obside')  # Switch to frame with menu
    dropdown = Select(driver.find_element(By.NAME, 'menu'))
    options = dropdown.options
    OB_Dates = pd.DataFrame(columns=['Depart_Date', 'Dispersed_Date'])
    for index in range(1, len(options)): #Change len(options) to a number to test the function
        dropdown = Select(driver.find_element(By.NAME, 'menu'))
        dropdown.select_by_index(index)
        time.sleep(3)
        driver.switch_to.default_content()
        driver.switch_to.frame('obmain')  # Switch to frame with the table
        tables = driver.find_elements(By.TAG_NAME, 'table')
        if len(tables) >= 2:
            correct_table = tables[0]
        rows = correct_table.find_elements(By.TAG_NAME, 'tr')
        depart_date = None
        Dispersed_date = None
        for row in rows:
            cell_text = row.find_element(By.TAG_NAME, 'td').text
            if 'Depart' in cell_text:
                depart_date = cell_text.split('on')[-1].strip()
            elif 'Dispersed' in cell_text:
                Dispersed_date = cell_text.split('on')[-1].strip()
        new_row = pd.DataFrame({'Depart_Date': [depart_date], 'Dispersed_Date': [Dispersed_date]})
        OB_Dates = pd.concat([OB_Dates, new_row], ignore_index=True) 
        driver.switch_to.default_content()
        driver.switch_to.frame('obside')  #Switch back to frame with menu to preform the loop
    OB_Dates.to_excel('OB_Convoy_Dates.xlsx')
    driver.quit()
    return OB_Dates
#print(OB_Dates().head()) #Test/Run function


