from selenium import webdriver
import time
optn=webdriver.ChromeOptions()
optn.add_experimental_option("detach",True)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome(optn)

driver.get("https://www.myntra.com/")
ac=ActionChains(driver)

wait=WebDriverWait(driver,10)

time.sleep(4)
home=driver.find_element('xpath','(//a[text()="Home"])[1]')
ac.move_to_element(home).perform()

# parents = driver.window_handles
# print(parents)

time.sleep(4)

parent=driver.window_handles
driver.find_element('xpath','//a[text()="Ceiling Lamps"]').click()
time.sleep(2)
driver.find_element('xpath','(//li[@class="product-base"])[1]').click()

time.sleep(2)
driver.find_element('xpath','(//li[@class="product-base"])[2]').click()

time.sleep(2)
driver.find_element('xpath','(//li[@class="product-base"])[3]').click()

time.sleep(2)
parents = driver.window_handles
print(parents)
print(type(parents))
for i in parents:
    driver.switch_to.window(i)
    if "buy" in driver.current_url:
        driver.find_element('xpath','//div[text()="ADD TO BAG"]').click()
        time.sleep(2)



driver.switch_to.window(parent[0])

driver.refresh()
time.sleep(4)

driver.find_element('xpath','//span[@class="myntraweb-sprite desktop-iconBag sprites-headerBag"]').click()
wait.until(EC.visibility_of_element_located(('xpath','//span[@class="bulkActionStrip-itemSelected"]')))
print("verified")

