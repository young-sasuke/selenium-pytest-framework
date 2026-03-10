
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


from selenium_training.pom_project.object_repository.desktoppage_locators import DesktopLocators

loc = DesktopLocators()

class DesktopPage():
    def __init__(self, driver):
        self.driver = driver
        self.ac = ActionChains(driver)
    def Select_sort(self,sortby):
        # sort = self.driver.find_element('xpath', '//select[@id="products-orderby"]')
        sort = self.driver.find_element(*loc.sort_drpdwn)
        sort_select = Select(sort)
        sort_select.select_by_visible_text(sortby)
        time.sleep(2)

    def Select_view(self,viewby):
        # view = self.driver.find_element('xpath', '//select[@id="products-viewmode"]')
        view = self.driver.find_element(*loc.viewas_drpdwn)
        view_select = Select(view)
        view_select.select_by_visible_text(viewby)
        time.sleep(2)

    def Scroll_down(self):
        self.ac.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)

    def Click_to_simplecomputer(self):
        # self.driver.find_element('xpath', '(//a[text()="Simple Computer"])[2]').click()
        self.driver.find_element(*loc.simp_comp).click()
        time.sleep(1)


