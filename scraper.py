import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

reservationHours = []
openSlots = []
#Room Reservation Website
url = "https://calendar.library.ucsc.edu/space/139582"

# Set up the driver for your web browser (e.g., Firefox, Chrome)
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

# Button Clicker

for i in range(7):
    rightButton = driver.find_element(By.XPATH,'/html/body/div[3]/main/div/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/button[2]/i')
    rightButton.click()

driver.implicitly_wait(30)
eightam = driver.find_element(By.XPATH,'/html/body/div[3]/main/div/div/div[2]/div[2]/div[1]/div[2]/div/table/tbody/tr/td[3]/div/div/div/table/tbody/tr/td/div/div[2]/div[5]/a')
eightam.click()

driver.implicitly_wait(30)
ninepm = driver.find_element(By.XPATH,'/html/body/div[3]/main/div/div/div[2]/div[2]/div[1]/div[2]/div/table/tbody/tr/td[3]/div/div/div/table/tbody/tr/td/div/div[2]/div[31]/a')
ninepm.click()

driver.implicitly_wait(30)
tenpm = driver.find_element(By.XPATH,'/html/body/div[3]/main/div/div/div[2]/div[2]/div[1]/div[2]/div/table/tbody/tr/td[3]/div/div/div/table/tbody/tr/td/div/div[2]/div[33]/a')
tenpm.click()

driver.implicitly_wait(30)
elevenpm = driver.find_element(By.XPATH,'/html/body/div[3]/main/div/div/div[2]/div[2]/div[1]/div[2]/div/table/tbody/tr/td[3]/div/div/div/table/tbody/tr/td/div/div[2]/div[35]/a')
elevenpm.click()

driver.implicitly_wait(30)
submit = driver.find_element(By.XPATH,'/html/body/div[3]/main/div/div/div[2]/div[3]/form/fieldset/div[2]/button')
submit.click()

driver.implicitly_wait(30)
cont = driver.find_element(By.XPATH,'/html/body/div[3]/main/div/div/div[2]/div[4]/div[2]/form/div[2]/button')
cont.click()

# INPUT ELEMENTS

driver.implicitly_wait(30)
first_name = driver.find_element(By.XPATH,'/html/body/div[3]/main/div/div/div[2]/div[4]/div[3]/form/div[2]/div[2]/input')
first_name.send_keys("Seth")

driver.implicitly_wait(30)
last_name = driver.find_element(By.XPATH,'/html/body/div[3]/main/div/div/div[2]/div[4]/div[3]/form/div[2]/div[3]/input')
last_name.send_keys("Hahn")

driver.implicitly_wait(30)
email = driver.find_element(By.XPATH,'/html/body/div[3]/main/div/div/div[2]/div[4]/div[3]/form/div[3]/div/input')
email.send_keys("seehahn@ucsc.edu")

driver.implicitly_wait(30)
submit = driver.find_element(By.XPATH,'/html/body/div[3]/main/div/div/div[2]/div[4]/div[3]/form/div[5]/div/button')
submit.click()






bruh = input("oiurengwoirfnwiorfv")

# print(elementColor)
# print(elementColor)
# print(elementColor)
# print(elementColor)
# print(elementColor)
# print(elementColor)
# print(elementColor)
# print(elementColor)


# Click on green elements and sort into an array with respective index split into one hour segments
# for index i:i+4, i+4:i+8, i+8:i+12, ava, mustafa, seth for example 

# for i in range(len(reservationHours)):
#     if i <= 7:
#         #use ava credentials
#     elif i > 7 and i <= 15:
#         #use mustafa credentials
#     elif i > 15:
#         #use seth credentials
#     elif i > 23:
#         break

