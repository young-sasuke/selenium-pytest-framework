import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium_training.pom_project.object_repository.homepage_locators import HomePageLocators

loc = HomePageLocators()


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.ac = ActionChains(driver)
        self.wait = WebDriverWait(driver, 10)

    def click_login(self):
        # self.driver.find_element("xpath", '//a[text()="Log in"]').click()
        self.driver.find_element(*loc.login_link).click()
        time.sleep(4)

    def check_login(self):
        # self.wait.until(EC.visibility_of_element_located(('xpath', '//a[@class="ico-logout"]')))
        self.wait.until(EC.visibility_of_element_located(loc.logout_link))
        time.sleep(2)

    def hovor_to_computers(self):
        # ele = self.driver.find_element("xpath", '(//a[contains(text(),"Computers")])[1]')
        ele = self.driver.find_element(*loc.computers)
        self.ac.move_to_element(ele).perform()
        time.sleep(2)

    def click_to_desktop(self):
        # self.driver.find_element("xpath", '(//a[contains(text(),"Desktops")])[1]').click()
        ele = self.wait.until(EC.element_to_be_clickable(loc.desktops))
        ele.click()
        time.sleep(4)

    def click_to_soppingcart(self):
        # self.driver.find_element('xpath', '//span[text()="Shopping cart"]').click()
        self.driver.find_element(*loc.shopping_cart).click()
        time.sleep(3)