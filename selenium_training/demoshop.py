import time

from selenium import webdriver

optn = webdriver.ChromeOptions()
optn.add_experimental_option("detach", True)
c_driver = webdriver.Chrome(optn)




from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
c_driver.get("https://demowebshop.tricentis.com/")
c_driver.maximize_window()
from selenium.webdriver.common.action_chains import ActionChains

wait = WebDriverWait(c_driver, 20)









ac=ActionChains(c_driver)

c_driver.find_element("xpath",'//a[text()="Log in"]').click()
c_driver.find_element("xpath",'//input[@class="email"]').send_keys("bhaskar@12gmail.com")

c_driver.find_element("xpath",'//input[@id="Password"]').send_keys("passbhas")
c_driver.find_element("xpath",'//input[@class="button-1 login-button"]').click()



wait.until(EC.visibility_of_element_located(('xpath','//a[@class="ico-logout"]')))


ele=c_driver.find_element("xpath",'(//a[contains(text(),"Computers")])[1]')
ac.move_to_element(ele).perform()
time.sleep(2)




c_driver.find_element("xpath",'(//a[contains(text(),"Desktops")])[1]').click()
time.sleep(4)





sort = c_driver.find_element('xpath', '//select[@id="products-orderby"]')
sort_select = Select(sort)
sort_select.select_by_visible_text("Price: Low to High")
time.sleep(2)




view = c_driver.find_element('xpath', '//select[@id="products-viewmode"]')
view_select = Select(view)
view_select.select_by_visible_text("List")
time.sleep(2)

ac.send_keys(Keys.PAGE_DOWN).perform()
time.sleep(2)

c_driver.find_element('xpath', '(//a[text()="Simple Computer"])[3]').click()
time.sleep(1)



ac.send_keys(Keys.PAGE_DOWN).perform()
time.sleep(4)



time.sleep(2)
c_driver.find_element('xpath','//label[@for="product_attribute_75_5_31_96"]').click()
time.sleep(2)
c_driver.find_element('xpath','//input[@id="add-to-cart-button-75"]').click()
time.sleep(2)

ac.send_keys(Keys.HOME).perform()
time.sleep(2)

c_driver.find_element('xpath','//span[text()="Shopping cart"]').click()
time.sleep(3)



country_select=c_driver.find_element('xpath','//select[@class="country-input"]')
select_country=Select(country_select)
select_country.select_by_visible_text("India")

state_select=c_driver.find_element('xpath','//select[@class="state-input"]')
select_state=Select(state_select)
select_state.select_by_visible_text("Other (Non US)")


c_driver.find_element('xpath','//input[@id="ZipPostalCode"]').send_keys("123456")
time.sleep(2)
c_driver.find_element('xpath','//input[@id="termsofservice"]').click()
time.sleep(2)

c_driver.find_element('xpath','//button[@id="checkout"]').click()
time.sleep(2)




