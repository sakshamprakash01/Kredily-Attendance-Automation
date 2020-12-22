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

dayDict = {0:"monday", 1:"tuesday", 2:"wednesday", 3:"thursday", 4:"friday", 5:"saturday", 6:"sunday"}

def log(action, data):
    current_time = datetime.datetime.now()
    rec = [current_time, dayDict[current_time.weekday()], action, data["Email"]]
    with open('logs.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(rec)
    
    print ("\n",rec,"\n")

def readData(Addr):
    data = json.load(open(Addr))
    return data