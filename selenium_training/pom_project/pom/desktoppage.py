import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from selenium_training.pom_project.object_repository.desktoppage_locators import DesktopLocators

loc = DesktopLocators()

class DesktopPage():

    def __init__(self, driver):
        self.driver = driver
        self.ac = ActionChains(driver)
        self.wait = WebDriverWait(driver, 20)

    def Select_sort(self, sortby):
        sort = self.wait.until(
            EC.presence_of_element_located(loc.sort_drpdwn)
        )
        sort_select = Select(sort)
        sort_select.select_by_visible_text(sortby)
        time.sleep(2)

    def Select_view(self, viewby):
        view = self.wait.until(
            EC.presence_of_element_located(loc.viewas_drpdwn)
        )
        view_select = Select(view)
        view_select.select_by_visible_text(viewby)
        time.sleep(2)

    def Scroll_down(self):
        self.ac.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)

    def Click_to_simplecomputer(self):

        ele = self.wait.until(
            EC.element_to_be_clickable(loc.simp_comp)
        )

        # Scroll to element (important for Jenkins/headless)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", ele)

        time.sleep(2)

        # JS click for CI stability
        self.driver.execute_script("arguments[0].click();", ele)

        time.sleep(2)