import time


from selenium_training.pom_project.object_repository.loginpage_locators import LoginPageLocators

loc =LoginPageLocators()
class LogIn():
    def __init__(self, driver):
        self.driver = driver
    def enter_email(self,email):
        # self.driver.find_element("xpath", '//input[@class="email"]').send_keys(email)
        self.driver.find_element(*loc.email).send_keys(email)

    def enter_password(self,password):
        # self.driver.find_element("xpath", '//input[@id="Password"]').send_keys(password)
        self.driver.find_element(*loc.password).send_keys(password)

    def click_to_login(self):
        # self.driver.find_element("xpath", '//input[@class="button-1 login-button"]').click()
        self.driver.find_element(*loc.login_btn).click()


