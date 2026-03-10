
import time
from selenium.webdriver.support.select import Select



from selenium_training.pom_project.object_repository.cartpage_locators import CartPageLocators

loc = CartPageLocators()

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def select_country(self,country):
        # country_select = self.driver.find_element('xpath', '//select[@class="country-input"]')
        country_select = self.driver.find_element(*loc.country_data)
        select_country = Select(country_select)
        select_country.select_by_visible_text(country)

    def select_state(self):
        # state_select = self.driver.find_element('xpath', '//select[@class="state-input"]')
        state_select = self.driver.find_element(*loc.state_data)
        select_state = Select(state_select)
        select_state.select_by_visible_text("Other (Non US)")

    def enter_post(self,pincode):
        # self.driver.find_element('xpath', '//input[@id="ZipPostalCode"]').send_keys(pincode)
        self.driver.find_element(*loc.postalcode).send_keys(pincode)
        time.sleep(2)

    def click_on_terms(self):
        # self.driver.find_element('xpath', '//input[@id="termsofservice"]').click()
        self.driver.find_element(*loc.terms_service).click()
        time.sleep(2)

    def clcik_on_check_out(self):
        # self.driver.find_element('xpath', '//button[@id="checkout"]').click()
        self.driver.find_element(*loc.checkout_btn).click()
        time.sleep(2)