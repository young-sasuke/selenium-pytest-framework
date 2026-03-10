# import time
# class TestLogin:
#
#     def test_linkon(self,setup):
#         setup.find_element('xpath', '//a[text()="Log in"]').click()
#         time.sleep(3)
#
#     def test_email(self,setup):
#         setup.find_element('xpath', '//input[@id="Email"]').send_keys("demo@gamil.com")
#
#     def test_password(self,setup):
#         setup.find_element('xpath', '//input[@id="Password"]').send_keys("password")
#
#     def test_login(self,setup):
#         setup.find_element('xpath', '//input[@class="button-1 login-button"]').click()
#
#




# c_driver.find_element('xpath', '//input[@id="register-button"]').click()



import time

class TestLogin:

    def test_login_link(self, setup):
        setup.find_element('xpath', '//a[text()="Log in"]').click()
        time.sleep(1)

    def test_login_email(self, setup):
        setup.find_element('id', 'Email').send_keys('kumar@gmail.com')

    def test_login_pwd(self, setup):
        setup.find_element('id', 'Password').send_keys('kumar@12345')

















