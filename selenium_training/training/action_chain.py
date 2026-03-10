# for performing the mouse operation we have to use the actionchain class
from turtledemo.minimal_hanoi import hanoi

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


import time
from selenium import webdriver
driver =webdriver.ChromeOptions()
driver.add_experimental_option("detach" ,True)

#
#
# prefs={
#     "download.default_directory":r"C:\Users\KIIT\PycharmProjects\selenium_project\training"
#
# }
#
# prefs = {
#     n"download.default_directory":r"C:\Users\KIIT\PycharmProjects\selenium_project\training",
#     "profile.password_manager_leak_detection": False
#
# }
# driver.add_experimental_option("prefs", prefs)
# driver.add_argument("--disable-notifications")
# # in case of firefox there is set_preference function
#


#
c_driver =webdriver.Chrome(driver)
# driver=webdriver.FirefoxOptions()
# driver.add_experimental_option("detach" ,True)
# driver.set_


# c_driver =webdriver.Firefox(driver)

ac=ActionChains(c_driver)

k=Keys()

c_driver.get("https://demowebshop.tricentis.com/")


'''mouse hovering operations  '''
# men=c_driver.find_element('xpath','//a[text()="Men"]')
# ac.move_to_element(men).perform()
# time.sleep(2)
# women=c_driver.find_element('xpath','//a[text()="Women"]')
# ac.move_to_element(women).perform()
# time.sleep(2)
# kids=c_driver.find_element('xpath','//a[text()="Kids"]')
# ac.move_to_element(kids).perform()
# time.sleep(2)
# home=c_driver.find_element('xpath','//a[text()="Home"]')
# ac.move_to_element(home).perform()



'''     Double click        '''
# ele=c_driver.find_element('xpath','//button[@ondblclick="myFunction1()"]')
# ac.double_click(ele).perform()
#
#
#
# ele1=c_driver.find_element('xpath','//label[text()="Name:"]')
# ac.double_click(ele1).perform()


# ele=c_driver.find_element('xpath','//button[@ondblclick="myFunction1()"]')
# ac.double_click(ele).perform()


# right click
# ac.context_click().perform()
# to right click on the element
'''     Right click        '''
# ele=c_driver.find_element('xpath','//button[@ondblclick="myFunction1()"]')
#
# ac.context_click(ele).perform()


# scrolling operation in selenium
'''     SCROLLING OPERATIONS        '''

# c_driver.get("https://myntra.com")
# ele=c_driver.find_element('xpath','//a[text()=" ONLINE SHOPPING "]')
# ac.scroll_to_element(ele).perform()
# ac.scroll_to_element().perform()

# ac.send_keys(k.HOME).perform()

# ac.send_keys(k.PAGE_UP).perform()
#
# ac.scroll_by_amount(0,2000).perform()
# ac.scroll_by_amount(0,-2000).perform()

#
# ele=c_driver.find_element('xpath','//h2[text()="SVG Elements"]')
# ac.scroll_to_element(ele).perform()
#
#
#


'''drag and drop'''
# dragable=c_driver.find_element('xpath','//div[@id="draggable"]')
# drag=c_driver.find_element('xpath','//div[@id="droppable"]')
#
# ac.drag_and_drop(dragable,drag).perform()
#
# # by offseet
'''drag and drop by offseet'''
# ac.drag_and_drop_by_offset(dragable,50)
#
#
#
# # slider
'''slider'''
# left=c_driver.find_element('xpath','id="slider-range"')
# ac.click_and_hold(left).move_by_offset(50,0).release().perform()

'''cntr+a'''

# ac.key_down(k.CONTROL).send_keys('A').key_up(k.CONTROL).perform()
# c_driver.find_element('xpath', '//input[@id="name"]').send_keys("asdf")

# tab

# ac.send_keys(k.TAB).perform()
# ac.send_keys("asdd@gmail.com").perform()
















# c_driver.find_element('xpath', '//span[text()="Continue with Google"]').click()
parent=c_driver.window_handles
print(parent)

c_driver.find_element('xpath','//a[text()="Google+"]').click()

hand2=c_driver.window_handles
print(hand2)


for handles in hand2:
    c_driver.switch_to.window(handles)
    if "googlelog" in c_driver.current_url:
        c_driver.find_element('xpath','//input[@placeholder="Search blog"]').send_keys("hii")



c_driver.switch_to.window(parent)
# c_driver.find_element('xpath','//a[text()="Youtube+"]').click()


