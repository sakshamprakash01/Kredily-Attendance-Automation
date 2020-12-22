from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import json
import time
import csv
import datetime
import fileUtils

def clockOut():
    data = fileUtils.readData('credentials.json')

    options = Options()
    options.headless = True
    driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)
    #driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get('https://app.kredily.com/login/?_ga=2.193396265.545062843.1608056090-510643525.1608056090')

    emailBox = driver.find_element_by_name('email_address')
    emailBox.send_keys(data["Email"])

    passBox = driver.find_element_by_name('password')
    passBox.send_keys(data["Password"])

    signInButton2 = driver.find_element_by_xpath('//*[@id="signinSubmitBtn"]')
    signInButton2.click()

    webClock = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#clockInBtn')))
    #webClock.click()

    time.sleep(10)
    driver.quit()

    fileUtils.log("Clock-Out", data)

if __name__ == "__main__":
    clockOut()