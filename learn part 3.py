from lib2to3.pgen2 import driver
from re import search
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Explicite Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

driver = webdriver.Firefox()

driver.get('https://orteil.dashnet.org/cookieclicker/')
print(driver.title)


linkText = driver.find_element(By.LINK_TEXT, 'Game Development With Python')

linkText.click()

try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'General Pygame Tutorial')))
    element.click()

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'sow-button-19310003')))
    element.click()

except TimeoutException:
    driver.quit()
    pass