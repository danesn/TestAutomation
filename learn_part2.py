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

# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])

# driver = webdriver.Chrome(options=options)

driver = webdriver.Firefox()

driver.get('https://www.techwithtim.net/')
print(driver.title)


try:
    searchInput = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 's')))
    searchInput.send_keys("test")
    searchInput.send_keys(Keys.RETURN)

    time.sleep(10)
    main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'main')))

    # print(main.text)

    time.sleep(10)

    articles = main.find_elements(By.TAG_NAME, 'article')

    print("-----------------------------")

    for article in articles:
        p = article.find_element(By.CLASS_NAME, 'entry-summary')
        print(p.text)
        print("[][][][[]][]]][][][][]]]")
    
    print("-----------------------------")
    # print(len(articles))
    # print(articles[0].text)

    time.sleep(10)

    driver.quit()

except TimeoutException:
    driver.quit()
    pass

