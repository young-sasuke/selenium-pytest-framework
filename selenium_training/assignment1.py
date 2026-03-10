import time
from selenium import webdriver
driver=webdriver.ChromeOptions()
driver.add_experimental_option("detach",True)

prefs = {
    "profile.password_manager_leak_detection": False

}
driver.add_experimental_option("prefs", prefs)
c_driver=webdriver.Chrome(driver)
c_driver.get("https://www.saucedemo.com/")

c_driver.find_element('xpath','//input[@id="user-name"]').send_keys("standard_user")
c_driver.find_element('xpath','//input[@id="password"]').send_keys("secret_sauce")
c_driver.find_element('xpath','//input[@id="login-button"]').click()

time.sleep(2)
c_driver.find_element('xpath','(//button[@class="btn btn_primary btn_small btn_inventory "])[1]').click()
time.sleep(2)
c_driver.find_element('xpath','//a[ @class="shopping_cart_link"]').click()
time.sleep(2)
c_driver.find_element('xpath','//button[ @id="checkout"]').click()
time.sleep(2)
c_driver.find_element('xpath','//input[@id="first-name"]').send_keys("Uttam")
time.sleep(2)
c_driver.find_element('xpath','//input[@id="last-name"]').send_keys("Anand")
time.sleep(2)
c_driver.find_element('xpath','//input[@id="postal-code"]').send_keys("000000")
time.sleep(2)
c_driver.find_element('xpath','//input[@id="continue"]').click()
time.sleep(2)
c_driver.find_element('xpath','//button[@id="finish"]').click()
time.sleep(2)
c_driver.find_element('xpath','//button[@id="react-burger-menu-btn"]').click()
time.sleep(2)
c_driver.find_element('xpath','//a[@id="logout_sidebar_link"]').click()
time.sleep(2)





