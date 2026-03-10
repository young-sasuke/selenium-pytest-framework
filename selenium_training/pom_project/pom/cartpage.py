import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium_training.pom_project.object_repository.cartpage_locators import CartPageLocators

loc = CartPageLocators()


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def select_country(self, country):

        country_select = self.wait.until(
            EC.presence_of_element_located(loc.country_data)
        )

        select_country = Select(country_select)
        select_country.select_by_visible_text(country)

        time.sleep(2)

    def select_state(self):

        state_select = self.wait.until(
            EC.presence_of_element_located(loc.state_data)
        )

        select_state = Select(state_select)
        select_state.select_by_visible_text("Other (Non US)")

        time.sleep(2)

    def enter_post(self, pincode):

        post = self.wait.until(
            EC.presence_of_element_located(loc.postalcode)
        )

        post.clear()
        post.send_keys(pincode)

        time.sleep(2)

    def click_on_terms(self):

        terms = self.wait.until(
            EC.element_to_be_clickable(loc.terms_service)
        )

        terms.click()

        time.sleep(2)

    def clcik_on_check_out(self):

        checkout = self.wait.until(
            EC.element_to_be_clickable(loc.checkout_btn)
        )

        checkout.click()

        time.sleep(2)