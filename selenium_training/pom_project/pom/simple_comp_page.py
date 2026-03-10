import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium_training.pom_project.object_repository.simpcomp_page_locators import SimpCompPageLocators

loc =SimpCompPageLocators()
class Simple_Comp:
    def __init__(self, driver):
        self.driver = driver
        self.ac = ActionChains(driver)

    def choose_processor(self):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
    
        ele = WebDriverWait(self.driver,10).until(
        EC.element_to_be_clickable(loc.processor)
        )
        ele.click()
        time.sleep(2)

    def click_to_addtocart(self):
        # self.driver.find_element('xpath', '//input[@id="add-to-cart-button-75"]').click()
        self.driver.find_element(*loc.addtocart_btn).click()
        time.sleep(2)

    def go_to_home(self):

        self.ac.send_keys(Keys.HOME).perform()
        time.sleep(2)