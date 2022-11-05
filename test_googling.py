import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#Explicite Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

#Hover chain
from selenium.webdriver.common.action_chains import ActionChains



options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])



driver = webdriver.Chrome(options=options)
# driver.get("https://the-internet.herokuapp.com/windows")
# # buttonLogin = driver.find_element(By.CLASS_NAME, "radius")
# # time.sleep(5)
# # buttonLogin = driver.find_element(By.CSS_SELECTOR, "#content > div > button")

# get_title = driver.title
# print(get_title)

# newLinkTab = driver.find_element(By.LINK_TEXT, "Click Here")
# newLinkTab.click()

# get_title = newLinkTab.text
# print(get_title)

# # buttonLogin = driver.find_element(By.XPATH, '//*[@id="content"]/div/button')
# # buttonLogin.click()


#####################################

# Implicite wait
# driver.implicitly_wait(10)
# driver.get("https://demoqa.com/login")
# driver.get("https://demoqa.com/books")
# driver.find_element(By.ID, "login").click()

# # confirm button
# buttonClickMeConfirm = driver.find_element(By.ID, "confirmButton")
# buttonClickMeConfirm.click()
# time.sleep(5)
# #driver.switch_to.alert.dismiss()
# driver.switch_to.alert.accept()

# # prompt button
# buttonClickMeConfirm = driver.find_element(By.ID, "promtButton")
# time.sleep(2)
# buttonClickMeConfirm.click()
# time.sleep(2)
# driver.switch_to.alert.send_keys("Learn about automation with python")
# time.sleep(2)
# # driver.switch_to.alert.dismiss()
# driver.switch_to.alert.accept()

#explicite wait
# driver.get("https://demoqa.com/alerts")
# buttonClick = driver.find_element(By.ID, "timerAlertButton")
# buttonClick.click()

# try:
#     WebDriverWait(driver, 10).until(EC.alert_is_present())
#     driver.switch_to.alert.accept()
#     print("Alert di accept")
# except TimeoutException:
#     print("Alert tidak muncul")
#     pass


for i in range (1):

    driver.get("https://tees.co.id/")

    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > div.modal.promo-popup-special.fade.ng-scope.ng-isolate-scope.in')))
        print("Popup muncul")
        driver.find_element(By.CLASS_NAME, 'btn-modal-close').click()
        print("Popup Berhasil diclose")
        print("----------------------")
        
        output = driver.find_element(By.CSS_SELECTOR, 'body > div.wrapper > div > div > app-home > submenu-product-category > div > div > div > div > ul > li:nth-child(4)')
        textJudul = output.text
        print(textJudul)

        if textJudul == "DRINKWARE":
            print("True")

            hover = ActionChains(driver).move_to_element(output)

            hover.perform()
            
            script = "return window.getComputedStyle(document.querySelector('body > div.wrapper > div > div > app-home > submenu-product-category > div > div > div > div > ul > li:nth-child(4) > ul'), ':before').getPropertyValue('content')"
            print(driver.execute_script(script).strip())

            

        else:
            print("False")


    except TimeoutException:
        print("Modal tidak muncul")
        print("----------------------")
        pass

    time.sleep(3)


######################################





# mendapatkan list div
# listDiv = driver.find_elements(By.TAG_NAME, "div")
# print(len(listDiv))

# driver.find_element(By.ID, "username").send_keys("uno")
# driver.find_element(By.NAME, "username").send_keys("hoho")

# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/login")
# elem = driver.find_element(By.CLASS_NAME, "px-4")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)

#driver.close()