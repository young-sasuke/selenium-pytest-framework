#
# class TestRegister:
#      def test_reg_link(self, setup):
#          setup.find_element('xpath', '//a[text()="Register"]').click()
#          time.sleep(1)
#
#     def test_gender(self,setup):
#         setup.find_element('xpath', '//input[@id="gender-male"]').click()
#
#     def test_firstname(self,setup):
#         setup.find_element('xpath', '//input[@id="FirstName"]').send_keys("bhaskar")
#
#     def test_lastname(self,setup):
#         setup.find_element('xpath', '//input[@id="LastName"]').send_keys("kumar")
#
#     def test_email(self,setup):
#         setup.find_element('xpath', '//input[@id="Email"]').send_keys("bhaskar@gmail.com")
#
#     def test_pass(self,setup):
#         setup.find_element('xpath', '//input[@id="Password"]').send_keys("pass")
#
#     def test_confirmPassword(self,setup):
#         setup.find_element('xpath', '//input[@id="ConfirmPassword"]').send_keys("cpassword")
#     def test_click(self,setup):
#         setup.find_element('xpath', '//input[@id="register-button"]').click()
#


import time

class TestRegister:

    def test_reg_link(self, setup):
        setup.find_element('xpath', '//a[text()="Register"]').click()
        time.sleep(1)

    def test_gender_btn(self, setup):
        setup.find_element('id', 'gender-male').click()

    def test_fname(self, setup):
        setup.find_element('id', 'FirstName').send_keys('kumar')

    def test_lname(self, setup):
        setup.find_element('id', 'LastName').send_keys('kumarkumar')

    def test_reg_email(self, setup):
        setup.find_element('id', 'Email').send_keys('kumar@gmail.com')

    def test_reg_pwd(self, setup):
        setup.find_element('id', 'Password').send_keys('kumar@12345')

    def test_confirm_pwd(self, setup):
        setup.find_element('id', 'ConfirmPassword').send_keys('kumar@12345')
        time.sleep(2)

