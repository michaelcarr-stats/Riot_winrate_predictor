import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#from profile_detail import profile
#from match_detail import match

import json # for testing

driver = 0
summonerName = 'CHIKAlNAl'
queryMode = 'Total' # 'Ranked Solo', 'Ranked Flex'/'Ranked Flex 5v5'
summonerData = {}

def initDriver(url = 'https://www.op.gg/summoners/na/COOKIEMONSTER123'):
    # get initial html
    driverpath = os.path.realpath(r'../drivers/chromedriver')

    chrome_options = Options()  
    chrome_options.add_argument("--incognito")  
    # The below ensure selenium does not close.
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(driverpath, options=chrome_options)
    driver.get(url)

    return driver

def init_chapion(url = 'https://www.op.gg/summoners/na/COOKIEMONSTER123/champions'):
    # Need to select ranked but this is okay for now.
    driverpath = os.path.realpath(r'../drivers/chromedriver')

    chrome_options = Options()  
    chrome_options.add_argument("--incognito")  
    # The below ensure selenium does not close.
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(driverpath, options=chrome_options)
    driver.get(url)

    return driver

def refreshFullProfile():
    a = driver.find_element(By.XPATH, '//button[normalize-space()="Update"]')
    # block [1] get last updated time for checking updated click for button
    #a = driver.find_element('class',"update-button")
    #print(a[0].text)

    try:
        ActionChains(driver).click(a).perform()
        print('Profile update successful.')
    except:
        print('Unable to update profile. Rolling back to current statistics.')
    #updatebutton = driver.find_elements_by_id("SummonerRefreshButton")[0]
    
    ## WebDriverWait(driver, 15).until(a != driver.find_elements_by_class_name("LastUpdate")[0].text)
    #WebDriverWait(driver, 10).until(
    #    lambda wd: a != driver.find_elements_by_class_name("LastUpdate")[0].text
    #)
    return True

def get_tr():
    rows = driver.find_elements(By.XPATH, '//tr')

    #for row in rows:
    #    cols = row.find_elements(By.TAG_NAME, 'td')
    #    print(cols.text)

    return rows



driver = init_chapion()
x = get_tr()
