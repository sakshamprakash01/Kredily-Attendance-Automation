from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time

options = Options()
options.headless = True
driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)
wait = WebDriverWait(driver, 10)
driver.get('https://app.kredily.com/login/?_ga=2.193396265.545062843.1608056090-510643525.1608056090')
print("waiting 3 sec")
time.sleep(3)
driver.quit()