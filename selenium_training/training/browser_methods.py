import time


import time

'''

*   get()               :   To launch the web-application, we use get()
                SYNTAX  :   driver.get("url")

*   maximize_window()   :   This will maximize the browser window
                SYNTAX  :   driver.maximize_window()

*   minimize_window()   :   This will minimize the browser window
                SYNTAX  :   driver.minimize_window()

*   back()              :   This will go back()
                SYNTAX  :   driver.back()

*   forward()           :   This will go forward
                SYNTAX  :   driver.forward()

*   refresh()           :   This will refresh the page
                SYNTAX  :   driver.refresh()

*   current_url         :   This is a property. It will give the url of the page
                SYNTAX  :   driver.current_url

*   title               :   This is a property. It will give the title of the page
                SYNTAX  :   driver.title

*   name                :   This is a property. It will give the name of the browser we've used in the code
                SYNTAX  :   driver.name

*   close()             :   It will close the browser object
                SYNTAX  :   driver.close()

'''
from selenium import webdriver

import time
# device=webdriver.Chrome()


driver=webdriver.ChromeOptions()
driver.add_experimental_option("detach",True)

c_driver=webdriver.Chrome(driver)

#to lounch the application we required get function
c_driver.get("https://www.myntra.com")

# c_driver.maximize_window()
# time.sleep(2)


# c_driver.refresh()
# c_driver.back()
# c_driver.forward()



print(c_driver.name)
print(c_driver.current_url)

print(c_driver.title)

# c_driver.minimize_window()
# time.sleep(2)

c_driver.save_screenshot("myn.png")

time.sleep(20)
c_driver.close()