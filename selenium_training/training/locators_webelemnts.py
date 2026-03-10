# so there are two types of element
# 1.find_element()
#2.find_elements()

# syntax:  driver.find_element("loc name","loc value")
'''
locators: to locate the web elements we use locator
8 types of locator:
1.id
2.name
3.class name
3.tag name
4.link text
5.partial link text
6.partial link text
7.css selector
8.xpath
'''

#
# from selenium import  webdriver
# driver=webdriver.ChromeOptions()
# driver.add_experimental_option("detach",True)
#
# c_driver=webdriver.Chrome(driver)
#
# # c_driver.get("https://demowebshop.tricentis.com/register")
#
#
# # c_driver.get("https://testautomationpractice.blogspot.com/")
# c_driver.get("https://testautomationpractice.blogspot.com/")

'''id'''
#
# username=c_driver.find_element("id","user-name")
# print(username)
# password=c_driver.find_element("id","password")
# print(password)
#
# login=c_driver.find_element("id","login-button")
# # pwd=driver.find_element()
#
# username.send_keys("standard_user")
# password.send_keys("qwertyu")
# login.click()


# c_driver.find_element("id","user-name").send_keys("standard_user")
# c_driver.find_element("id","password").send_keys("secret_sauce")
# c_driver.find_element("id","login-button").click()
# c_driver.find_element("id","react-burger-menu-btn").click()
# c_driver.find_element("id","logout_sidebar_link").click()

'''
css selector
to locate any element using attributes ,we use css selection
 syntax: tagname(attribute_name='attributr_value")
 '''



# c_driver.find_element("css selector","input[data-test='username']").send_keys("standard_user")
# c_driver.find_element("css selector","input[placeholder='Password']").send_keys("secret_sauce")
# c_driver.find_element("css selector","input[data-test='login-button']").click()

#
# c_driver.find_element("css selector",'input[name="Gender"]').click()
# c_driver.find_element("css selector",'input[name="FirstName"]').send_keys("bhaskar")
# c_driver.find_element("css selector",'input[name="LastName"]').send_keys("kumar")
# # c_driver.find_element("css selector","input[data-test='login-button']").click()
# c_driver.find_element("css selector",'input[data-val-required="Email is required."]').send_keys("kumar01020304rtd@gmail.com")
# c_driver.find_element("css selector",'input[name="Password"]').send_keys("kumar0102")
# c_driver.find_element("css selector",'input[name="ConfirmPassword"]').send_keys("kumar0102")
# c_driver.find_element("css selector",'input[name="register-button"]').click()




# c_driver.find_element("css selector",'input[name="Gender"]').click()
# c_driver.find_element("css selector",'input[name="FirstName"]').send_keys("bhaskar")
# c_driver.find_element("css selector",'input[name="LastName"]').send_keys("kumar")







import time




# d_driver=webdriver.Chrome(driver)
# # c_driver=webdriver.Chrome()
# d_driver.get("https://testautomationpractice.blogspot.com/")
# d_driver.find_element("id","name").send_keys("bhaskar")
# time.sleep(2)
# d_driver.find_element("id","email").send_keys("bhaskar@gmail.com")
# time.sleep(2)
# d_driver.find_element("id","phone").send_keys("12345467890")
# time.sleep(2)
# d_driver.find_element("id","textarea").send_keys("bhaskaradd")
# time.sleep(2)







from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


from selenium import  webdriver
driver=webdriver.ChromeOptions()
driver.add_experimental_option("detach",True)

prefs = {
    "profile.password_manager_leak_detection": False

}
driver.add_experimental_option("prefs", prefs)

c_driver=webdriver.Chrome(driver)


# c_driver.get("https://demowebshop.tricentis.com/register")
# c_driver.get("https://www.python.org/downloads/")
# c_driver.get("https://www.iforex.in/tools/live-rates")
# c_driver.get("https://testautomationpractice.blogspot.com/")
# c_driver.get("https://www.myntra.com/")

# c_driver.get("https://www.saucedemo.com/")
# time.sleep(2)

'''
Xpath
'''

# c_driver.find_element('xpath','//input[@id="user-name"]').send_keys("bhaskar")
# c_driver.find_element('xpath','//input[@id="gender-male"]').click()
# c_driver.find_element('xpath','//input[@id="FirstName"]').send_keys("bhaskarkum")
# c_driver.find_element('xpath','//input[@id="LastName"]').send_keys("kumar")
# c_driver.find_element('xpath','//input[@id="Email"]').send_keys("bhaskarkum@gmail.com")
# c_driver.find_element('xpath','//input[@id="Password"]').send_keys("bhaskar")
# c_driver.find_element('xpath','//input[@id="ConfirmPassword"]').send_keys("bhaskar")
# c_driver.find_element('xpath','//input[@id="register-button"]').click()
# c_driver.find_element('xpath', '(//input[@type="text"])[1]').send_keys("bhaskar")
# c_driver.find_element('xpath', '(//input[@type="text"])[2]').send_keys("bhaskar@gmail.com")
# c_driver.find_element('xpath', '(//input[@type="text"])[3]').send_keys("1234567890")

# c_driver.find_element('xpath', '//textarea[@id="textarea"]').send_keys("odisha")
# c_driver.find_element('xpath', '//textarea[@id="textarea"]').send_keys("odisha")




# c_driver.find_element('xpath','(//a[text()="Men"])[1]').click()
# time.sleep(2)
# c_driver.back()
# c_driver.find_element('xpath','(//a[text()="Women"])[1]').click()
# time.sleep(2)
# c_driver.back()
# c_driver.find_element('xpath','(//a[text()="Kids"])[1]').click()
# time.sleep(2)
# c_driver.back()
# c_driver.find_element('xpath','(//a[text()="Home"])[1]').click()
# time.sleep(2)
# c_driver.back()
# c_driver.find_element('xpath','(//a[text()="Beauty"])[1]').click()
# time.sleep(2)
# c_driver.back()
# c_driver.find_element('xpath','(//a[text()="Genz"])[1]').click()
# time.sleep(2)
# c_driver.back()



# c_driver.find_element('xpath','(//a[contains(text(),"Books")])[3]').click()
# c_driver.back()
# c_driver.find_element('xpath','(//a[contains(text(),"Computers")])[3]').click()
# c_driver.back()
# c_driver.find_element('xpath','(//a[contains(text(),"Electronics")])[3]').click()


# c_driver.find_element('xpath','//div[@id="ai-chat-close"]').click()



# c_driver.find_element('xpath','//a[text()="Python 3.13.11"]/../..//a[text()="Release notes"]').click()


# time.sleep(20)


# c_driver.find_element('xpath','(//div[text()="Gold"]/../..//span)[2]').click()

# sell_price=c_driver.find_element('xpath','(//div[text()="Gold"]/../..//span)[2]')

# print(sell_price)
# c_driver.implicitly_wait(30)






# wait_obj=WebDriverWait(c_driver,20)

# c_driver.get(r"C:\Users\KIIT\PycharmProjects\selenium_project\training\main.html")

# c_driver.refresh()



# div[id="ai-fixed-btn"]
# (//div[text()="Gold"]/../..//span)[2]
# time.sleep(20)
# wait_obj.until(ec.visibility_of_element_located(('xpath','//input[@id="nameInput"]')))


# c_driver.find_element('xpath','//input[@id="nameInput"]').send_keys("hello")

#
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
# wait_obj=WebDriverWait()


# wait_obj=WebDriverWait(c_driver,20)




c_driver.get("https://www.saucedemo.com/")







#end to end execution project
c_driver.find_element('xpath','//input[@id="user-name"]').send_keys("standard_user")
c_driver.find_element('xpath','//input[@id="password"]').send_keys("secret_sauce")
c_driver.find_element('xpath','//input[@id="login-button"]').click()




# time.sleep(5)
# alert_obj=c_driver.switch_to.alert
# alert_obj.accept()
# time.sleep(2)



# c_driver.find_element('xpath','(//button[@class="btn btn_primary btn_small btn_inventory "])[1]').click()



