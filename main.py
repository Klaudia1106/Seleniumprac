from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
chrome_driver_path = "C:\\Users\\klaud\\Desktop\\Development\\chromedriver.exe"

service = Service(executable_path="C:\\Users\\klaud\\Desktop\\Development\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://demo.seleniumeasy.com/basic-first-form-demo.html")
time.sleep(2)
input= driver.find_element(By.XPATH, '//*[@id="user-message"]')
input.send_keys("Hello World")
button = driver.find_element(By.XPATH, '//*[@id="get-input"]/button')
button.click()

sum1= driver.find_element(By.XPATH, '//*[@id="sum1"]')
sum1.send_keys(24)
sum2 = driver.find_element(By.XPATH, '//*[@id="sum2"]')
sum2.send_keys(48)
total = driver.find_element(By.XPATH , '//*[@id="gettotal"]/button')
total.click()
