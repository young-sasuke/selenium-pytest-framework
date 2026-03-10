import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium_training.pom_project.object_repository.simpcomp_page_locators import SimpCompPageLocators

loc = SimpCompPageLocators()

class Simple_Comp:

    def __init__(self, driver):
        self.driver = driver
        self.ac = ActionChains(driver)
        self.wait = WebDriverWait(driver, 30)

    def choose_processor(self):

        # wait until simple computer page loads
        self.wait.until(
            EC.url_contains("simple-computer")
        )

        ele = self.wait.until(
            EC.element_to_be_clickable(loc.processor)
        )

        # scroll to element (important in CI)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", ele)

        ele.click()

        time.sleep(2)

    def click_to_addtocart(self):

        ele = self.wait.until(
            EC.element_to_be_clickable(loc.addtocart_btn)
        )

        self.driver.execute_script("arguments[0].scrollIntoView(true);", ele)

        ele.click()

        time.sleep(2)

    def go_to_home(self):

        self.ac.send_keys(Keys.HOME).perform()

        time.sleep(2)