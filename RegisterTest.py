from lib2to3.pgen2 import driver
from re import search
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Parameter/input variable
email = "popo@gmail.com"
mobilePhone = "082111358962"
password = "popoPOPO99123"
firstName = "Popopipi"
LastName = "Pupupupu"
cityAndProvince = "KOTA JAKARTA BARAT"


# Browse the Web and Wait until the web loads properly
driver = webdriver.Firefox()
driver.get('https://www.cermati.com/app/gabung')
driver.implicitly_wait(10)

# Input email
input = driver.find_element(By.NAME, "email")
input.send_keys(email)
# Input mobile phone
input = driver.find_element(By.NAME, "mobilePhone")
input.send_keys(mobilePhone)
# Input password
input = driver.find_element(By.NAME, "password")
input.send_keys(password)
# Input confirm password
input = driver.find_element(By.NAME, "confirmPassword")
input.send_keys(password)
# Input first name
input = driver.find_element(By.NAME, "firstName")
input.send_keys(firstName)
# Input last name
input = driver.find_element(By.NAME, "lastName")
input.send_keys(LastName)
# Input city and province
input = driver.find_element(By.ID, "cityAndProvince")
input.send_keys(cityAndProvince)

# Handling automate popup to make sure auto complete disappear
input.click()
time.sleep(4)
buttonConfirm = driver.find_element(By.CLASS_NAME, "btn--action_kallT")
buttonConfirm.click()
time.sleep(2)

# Click confirm button
buttonConfirm.click()

time.sleep(5)

driver.quit()