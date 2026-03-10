# Write a scripts to:
# Open https://www.demowebshop.tricentis.com
# Navigate to Books
# Add first book to cart
# Click Shopping Cart
# Verify the product is present in the cart.
#
#
# Write a Selenium scripts to:
# Open https://www.demowebshop.tricentis.com
# Navigate to Electronics
# Use XPath contains() to locate the Cell Phones category
# Click it.
#
#
# Write a Selenium scripts to:
# Open https://the-internet.herokuapp.com/dynamic_loading/1
# Click Start
# Wait until the Hello World text appears
# Print the text.
#
#
# Write a scripts to:
# Open https://the-internet.herokuapp.com/dynamic_controls
# Click Remove
# Wait until Add button becomes clickable
# Click Add
#
#
# Write a Selenium scripts to:
# Open https://demoqa.com/select-menu
# Select "Group 2, option 1" from the Select Value dropdown
# Verify the selected value.
#
#
#
# Write a Selenium scripts to:
# Open https://demoqa.com/select-menu
# Scroll to Standard multi select
# Select Volvo, Saab, and Opel
# Print all selected options.
#
#
# Write a Selenium scripts to:
# Open https://demoqa.com/menu/
# Hover over Main Item 2
# Hover over SUB SUB LIST
# Click Sub Sub Item 1
#
#
# Write a Selenium scripts to:
# Open https://demoqa.com/droppable
# Drag Drag me element
# Drop it on Drop here
# Verify text changes to Dropped!
#
#
# Write a Selenium scripts to:
# Open https://the-internet.herokuapp.com/javascript_alerts
# Click JS Confirm
# Accept the alert
# Verify result text shows You clicked: Ok
#
#
# Write a Selenium scripts to:
# Open https://the-internet.herokuapp.com/upload
# Upload a file from local system
# Click Upload
# Verify uploaded file name.
#
#
# Write a Selenium scripts to:
# Open https://the-internet.herokuapp.com/download
# Download any file
# Verify the file is downloaded in the Downloads folder using Python.
#
#
# Write a scripts to:
# Open https://demowebshop.tricentis.com
# Add any two products from Books
# Navigate to Shopping Cart
# Verify total number of products added is 2.
#
#
# Write a Selenium scripts that:
# Open https://demowebshop.tricentis.com
# Navigate to Books
# Add all books priced below $20 to cart
#
#
# Write the steps to read the data from excel
#
#
# Write the syntax for the xpath to locate the elements using
# 	*	attributes
# 	*	text
# 	*	group indexing
# 	*	contains
#
#
# #########################################################################################################
#
# 1. Which locator is generally the fastest in Selenium?
# 2. Which wait is recommended for handling dynamic elements in Selenium?
# 3. Which Selenium class is used to handle dropdown listboxes?



# id
# Explicit Wait
# Select






from selenium import webdriver
import time
import pytest




# optn = webdriver.ChromeOptions()
# optn.add_experimental_option("detach", True)
# c_driver = webdriver.Chrome(optn)
# c_driver.get("https://demowebshop.tricentis.com/")
#
# time.sleep(3)
# c_driver.find_element('xpath','//a[contains(text(),"Books")]').click()
# time.sleep(3)
# c_driver.find_element('xpath','(//input[@value="Add to cart"])[1]').click()
# time.sleep(3)
# c_driver.find_element('xpath','//span[text()="Shopping cart"]').click()
# time.sleep(3)


# time.sleep(10)



# ------------------------------------------------------------------------------
# Write a Selenium scripts to:
# Open https://www.demowebshop.tricentis.com
# Navigate to Electronics
# Use XPath contains() to locate the Cell Phones category
# Click it.
#

# optn = webdriver.ChromeOptions()
# optn.add_experimental_option("detach", True)
# c_driver = webdriver.Chrome(optn)
# c_driver.get("https://demowebshop.tricentis.com/")
#
# time.sleep(3)
# c_driver.find_element('xpath','//a[contains(text(),"Electronics")]').click()
#
# time.sleep(3)
# c_driver.find_element('xpath','(//div[@class="item-box"])[2]').click()
#
# time.sleep(3)
# c_driver.find_element('xpath','(//div[@class="item-box"])[1]').click()




# --------------------------------------------------------------------------------------------------------------

# Write a Selenium scripts to:
# Open https://the-internet.herokuapp.com/dynamic_loading/1
# Click Start
# Wait until the Hello World text appears
# Print the text.
#



from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By



#

#
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
#
# optn = webdriver.ChromeOptions()
# optn.add_experimental_option("detach", True)
# c_driver = webdriver.Chrome(optn)
#
# wait = WebDriverWait(c_driver, 20)
#
# c_driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
#
# c_driver.find_element('xpath', '//button[text()="Start"]').click()
#
#
# wait.until(EC.text_to_be_present_in_element(
#     (By.XPATH, '//div[@id="finish"]'), "Hello World!"
# ))
#
# text = c_driver.find_element('xpath', '//div[@id="finish"]')
# print(text.text)
#

# ----------------------------------------------------------------------------------

# Write a scripts to:
# Open https://the-internet.herokuapp.com/dynamic_controls
# Click Remove
# Wait until Add button becomes clickable
# Click Add
#
#

# optn = webdriver.ChromeOptions()
# optn.add_experimental_option("detach", True)
# c_driver = webdriver.Chrome(optn)
#
# wait = WebDriverWait(c_driver, 20)
#
# c_driver.get("https://the-internet.herokuapp.com/dynamic_controls")
#
# c_driver.find_element('xpath', '//button[text()="Remove"]').click()
#
#
# add_btn = wait.until(EC.element_to_be_clickable(
#     (By.XPATH, '//button[text()="Add"]')
# ))
#
# c_driver.find_element('xpath', '//button[text()="Add"]').click()



# ---------------------------------------------------------------------------------
# Write a Selenium scripts to:
# Open https://demoqa.com/select-menu
# Select "Group 2, option 1" from the Select Value dropdown
# Verify the selected value.
#
#



# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# import time
#
# optn = webdriver.ChromeOptions()
# optn.add_experimental_option("detach", True)
# c_driver = webdriver.Chrome(optn)
#
# wait = WebDriverWait(c_driver, 20)
#
# c_driver.get("https://demoqa.com/select-menu")
# c_driver.maximize_window()
# time.sleep(2)
#
#
# dropdown = wait.until(EC.element_to_be_clickable(('xpath', '//div[@id="withOptGroup"]')))
# dropdown.click()
#
#
# option = wait.until(EC.element_to_be_clickable(('xpath', '//div[text()="Group 2, option 1"]')))
# option.click()

#
# selected = c_driver.find_element('xpath', '//div[@id="withOptGroup"]//div[contains(@class,"singleValue")]')
# print("Selected:", selected.text)
# assert selected.text == "Group 2, option 1"
# print("Verified!")







# -------------------------------------------------------------------------------------


# Write a Selenium scripts to:
# Open https://demoqa.com/select-menu
# Scroll to Standard multi select
# Select Volvo, Saab, and Opel
# Print all selected options.
#
#
# optn = webdriver.ChromeOptions()
# optn.add_experimental_option("detach", True)
# c_driver = webdriver.Chrome(optn)
#
# wait = WebDriverWait(c_driver, 20)
#
# c_driver.get("https://demoqa.com/select-menu")

#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.action_chains import ActionChains
# import time
#
# optn = webdriver.ChromeOptions()
# optn.add_experimental_option("detach", True)
# c_driver = webdriver.Chrome(optn)
#
# wait = WebDriverWait(c_driver, 20)
#
# c_driver.get("https://demoqa.com/select-menu")
# c_driver.maximize_window()
# time.sleep(2)
#
#
# multi_select = wait.until(EC.presence_of_element_located(
#     ('xpath', '//select[@id="cars"]')
# ))
# c_driver.execute_script("arguments[0].scrollIntoView();", multi_select)
# time.sleep(1)
#
#
# select_obj = Select(multi_select)
#
#
# select_obj.select_by_visible_text("Volvo")
# select_obj.select_by_visible_text("Saab")
# select_obj.select_by_visible_text("Opel")
#
#
# selected_options = select_obj.all_selected_options
# print("Selected options:")
# for option in selected_options:
#     print(option.text)


# ------------------------------------------------------------------------------------------
# Write a Selenium scripts to:
# Open https://demoqa.com/menu/
# Hover over Main Item 2
# Hover over SUB SUB LIST
# Click Sub Sub Item 1




optn = webdriver.ChromeOptions()
optn.add_experimental_option("detach", True)
c_driver = webdriver.Chrome(optn)

wait = WebDriverWait(c_driver, 20)

c_driver.get("https://demoqa.com/select-menu")
# c_driver.maximize_window()
time.sleep(2)




from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
import time

optn = webdriver.ChromeOptions()
optn.add_experimental_option("detach", True)
c_driver = webdriver.Chrome(optn)

wait = WebDriverWait(c_driver, 20)
ac = ActionChains(c_driver)

c_driver.get("https://demoqa.com/menu/")
c_driver.maximize_window()
time.sleep(2)


main_item2 = wait.until(EC.visibility_of_element_located(('xpath', '//a[text()="Main Item 2"]')))
ac.move_to_element(main_item2).perform()
time.sleep(3)


sub_sub_list = wait.until(EC.visibility_of_element_located(('xpath', '//a[text()="SUB SUB LIST »"]')))
ac.move_to_element(sub_sub_list).perform()
time.sleep(3)


sub_sub_item1 = wait.until(EC.element_to_be_clickable(('xpath', '//a[text()="Sub Sub Item 1"]')))
sub_sub_item1.click()



# --------------------------------------
# Write a Selenium scripts to:
# Open https://demoqa.com/droppable
# Drag Drag me element
# Drop it on Drop here
# Verify text changes to Dropped!
#
#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# import time
#
# optn = webdriver.ChromeOptions()
# optn.add_experimental_option("detach", True)
# c_driver = webdriver.Chrome(optn)
#
# wait = WebDriverWait(c_driver, 20)
# ac = ActionChains(c_driver)
#
# c_driver.get("https://demoqa.com/droppable")
# c_driver.maximize_window()
# time.sleep(2)
#
#
# drag = wait.until(EC.visibility_of_element_located(('xpath', '//div[@id="draggable"]')))
#
# drop = wait.until(EC.visibility_of_element_located(('xpath', '//div[@id="droppable"]')))
#
#
# ac.drag_and_drop(drag, drop).perform()
# time.sleep(3)
#
#
# dropped_text = wait.until(EC.text_to_be_present_in_element(('xpath', '//div[@id="droppable"]'), "Dropped!"))
#
# result = c_driver.find_element('xpath', '//div[@id="droppable"]')
# print("Text after drop:", result.text)
#
#
# print("Drag and Drop Verified")




# ---------------------------------------------------------------------------------------------------------------

# Write a Selenium scripts to:
# Open https://the-internet.herokuapp.com/javascript_alerts
# Click JS Confirm
# Accept the alert
# Verify result text shows You clicked: Ok

# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# import time
#
# optn = webdriver.ChromeOptions()
# optn.add_experimental_option("detach", True)
# c_driver = webdriver.Chrome(optn)
#
# wait = WebDriverWait(c_driver, 20)
#
# c_driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# c_driver.maximize_window()
# time.sleep(2)
#
#
# js_confirm = wait.until(EC.element_to_be_clickable(('xpath', '//button[text()="Click for JS Confirm"]')))
# js_confirm.click()
#
#
# wait.until(EC.alert_is_present())
# alert = c_driver.switch_to.alert
# print("Alert text:", alert.text)
# alert.accept()
#
#
# result = wait.until(EC.visibility_of_element_located(('xpath', '//p[@id="result"]')))
# print("Result:", result.text)
#
# assert result.text == "You clicked: Ok", f"not verified"
# print("Verified!")

# ------------------------------------------------------------------------------------------------------------------------------


# Write a Selenium scripts to:
# Open https://the-internet.herokuapp.com/upload
# Upload a file from local system
# Click Upload
# Verify uploaded file name.
#
#
#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# import time
#
# optn = webdriver.ChromeOptions()
# optn.add_experimental_option("detach", True)
# c_driver = webdriver.Chrome(optn)
#
# wait = WebDriverWait(c_driver, 20)
#
# c_driver.get("https://the-internet.herokuapp.com/upload")
# c_driver.maximize_window()
# time.sleep(2)
#
#
# file_input = wait.until(EC.presence_of_element_located(('xpath', '//input[@id="file-upload"]')
# ))
#
#
# file_path = r"C:\Users\KIIT\PycharmProjects\selenium_project\training\myn.png"
# file_input.send_keys(file_path)
#
#
# upload_btn = wait.until(EC.element_to_be_clickable(
#     ('xpath', '//input[@id="file-submit"]')
# ))
# upload_btn.click()
#
#
# uploaded_file = wait.until(EC.visibility_of_element_located(
#     ('xpath', '//div[@id="uploaded-files"]')
# ))
#
# print("Uploaded file:", uploaded_file.text)
#
# print("File Upload Verified!")
