#Imports
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time

#Web Scrape Bot
def HX_WebScrape():
    chromedriver_path = '/usr/local/bin/chromedriver'
    service = Service(executable_path=chromedriver_path)
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('http://www.convoyweb.org.uk/hx/index.html')
    wait = WebDriverWait(driver, 5)
    #dropdown_menu = WebDriverWait(driver, 10).until(
        #EC.presence_of_element_located((By.NAME, 'menu')))
    driver.switch_to.frame('hxside') #Switch to frame with menu
    dropdown = Select(driver.find_element(By.NAME, 'menu'))
    options = dropdown.options
    HX_data = pd.DataFrame()
    for index in range(1, len(options)): #Change len(options) to a number to test the function
        dropdown_value = options[index].text
        dropdown = Select(driver.find_element(By.NAME, 'menu'))
        dropdown.select_by_index(index)
        time.sleep(3) 
        driver.switch_to.default_content() 
        driver.switch_to.frame('hxmain') #Switch to frame with the table
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
        df['HX Convoy Number'] = dropdown_value  
        HX_data = pd.concat([HX_data, df], ignore_index=True)
        driver.switch_to.default_content()
        driver.switch_to.frame('hxside') #Switch back to frame with menu to preform the loop
    #HX_data.to_excel('HX_Convoy_Data_1.xlsx')
    driver.quit()
    return HX_data
print(HX_WebScrape().head()) #Test/Run function

def HX_Dates():
    chromedriver_path = '/usr/local/bin/chromedriver'
    service = Service(executable_path=chromedriver_path)
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('http://www.convoyweb.org.uk/hx/index.html')
    wait = WebDriverWait(driver, 5)
    driver.switch_to.frame('hxside')  # Switch to frame with menu
    dropdown = Select(driver.find_element(By.NAME, 'menu'))
    options = dropdown.options
    HX_Dates = pd.DataFrame(columns=['Depart_Date', 'Arrive_Date'])
    for index in range(1, len(options)): #Change len(options) to a number to test the function
        dropdown = Select(driver.find_element(By.NAME, 'menu'))
        dropdown.select_by_index(index)
        time.sleep(3)
        driver.switch_to.default_content()
        driver.switch_to.frame('hxmain')  # Switch to frame with the table
        tables = driver.find_elements(By.TAG_NAME, 'table')
        if len(tables) >= 2:
            correct_table = tables[0]
        rows = correct_table.find_elements(By.TAG_NAME, 'tr')
        depart_date = None
        arrive_date = None
        for row in rows:
            cell_text = row.find_element(By.TAG_NAME, 'td').text
            if 'Depart' in cell_text:
                depart_date = cell_text.split('on')[-1].strip()
            elif 'Arrive' in cell_text:
                arrive_date = cell_text.split('on')[-1].strip()
        new_row = pd.DataFrame({'Depart_Date': [depart_date], 'Arrive_Date': [arrive_date]})
        HX_Dates = pd.concat([HX_Dates, new_row], ignore_index=True) 
        driver.switch_to.default_content()
        driver.switch_to.frame('hxside')  #Switch back to frame with menu to preform the loop
    #HX_Dates.to_excel('HX_Convoy_Dates.xlsx')
    driver.quit()
    return HX_Dates
print(HX_Dates().head()) #Test/Run function
