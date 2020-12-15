from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import json
import time
import csv
import datetime
import pprint

dayDict = {0:"monday", 1:"tuesday", 2:"wednesday", 3:"thursday", 4:"friday", 5:"saturday", 6:"sunday"}

def log(action, data):
    current_time = datetime.datetime.now()
    rec = [current_time, dayDict[current_time.weekday()], action, data["Email"]]
    with open('logs.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(rec)
    
    pprint(rec)

def readData(Addr):
    data = json.load(open(Addr))
    return data

def clockIn():
    data = readData('credentials.json')

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get('https://app.kredily.com/login/?_ga=2.193396265.545062843.1608056090-510643525.1608056090')

    emailBox = driver.find_element_by_name('email_address')
    emailBox.send_keys(data["Email"])

    passBox = driver.find_element_by_name('password')
    passBox.send_keys(data["Password"])

    signInButton2 = driver.find_element_by_xpath('//*[@id="signinSubmitBtn"]')
    signInButton2.click()

    webClock = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#clockInBtn')))
    webClock.click()

    time.sleep(10)
    driver.quit()

    log ("Clock-In", data)

def clockOut():
    data = readData('credentials.json')

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get('https://app.kredily.com/login/?_ga=2.193396265.545062843.1608056090-510643525.1608056090')

    emailBox = driver.find_element_by_name('email_address')
    emailBox.send_keys(data["Email"])

    passBox = driver.find_element_by_name('password')
    passBox.send_keys(data["Password"])

    signInButton2 = driver.find_element_by_xpath('//*[@id="signinSubmitBtn"]')
    signInButton2.click()

    webClock = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#clockInBtn')))
    webClock.click()

    time.sleep(10)
    driver.quit()

    log ("Clock-Out", data)