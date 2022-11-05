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

#Action chain
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get('https://orteil.dashnet.org/cookieclicker/')
driver.implicitly_wait(10)

englishLanguage = driver.find_element(By.ID, "langSelect-EN")
englishLanguage.click()

cookie = driver.find_element(By.ID, "bigCookie")
scoreCookies = driver.find_element(By.ID, "cookies")
itemPriceClicker = driver.find_element(By.ID, "productPrice0")

actions = ActionChains(driver)


example = scoreCookies.text.split(" ")[0]
print(example[0])


for i in range(5000):
    # print(scoreCookies.text)
    print(i)
    actions.click(cookie)
    actions.perform()


    valueScoreCookies = int(scoreCookies.text.split(" ")[0])
    valuePriceClicker = int(itemPriceClicker.text)

    if valueScoreCookies >= valuePriceClicker:
        upgrade_actions = ActionChains(driver)
        upgrade_actions.move_to_element(itemPriceClicker)
        upgrade_actions.click()
        upgrade_actions.perform()