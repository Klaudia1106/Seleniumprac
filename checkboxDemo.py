from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
chrome_driver_path = "C:\\Users\\klaud\\Desktop\\Development\\chromedriver.exe"

service = Service(executable_path="C:\\Users\\klaud\\Desktop\\Development\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://demo.seleniumeasy.com/basic-checkbox-demo.html")
time.sleep(2)

checkbox = driver.find_element(By.XPATH, '//*[@id="isAgeSelected"]')
checkbox.click()

check_all= driver.find_element(By.XPATH, '//*[@id="check1"]')
check_all.click()

checkbox4 = driver.find_element(By.XPATH ,'//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[4]/label/input')
checkbox4.click()
checkbox3 = driver.find_element(By.XPATH ,'//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[3]/label/input')
checkbox3.click()
