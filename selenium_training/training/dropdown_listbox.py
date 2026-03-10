# from select import select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


import time
from selenium import webdriver
driver =webdriver.ChromeOptions()
driver.add_experimental_option("detach" ,True)
c_driver=webdriver.Chrome(driver)
ac=ActionChains(c_driver)

k=Keys()

# c_driver.get(r"C:\Users\KIIT\PycharmProjects\selenium_project\resources\demo.html")
c_driver.get("https://www.irctc.co.in/nget/train-search")



time.sleep(8)
c_driver.find_element('xpath','//span[text()="LOWER BERTH/SR.CITIZEN"]').click()





listbox=c_driver.find_element('xpath','//Select[@id="standard_cars"]')
select1=select_obj=Select(listbox)

'''
select by index
'''
# select_obj.select_by_index(5)
'''
# select by value
'''
# select_obj.select_by_value("bmw")
'''
# select by text
'''
# select_obj.select_by_visible_text("Ford")


# single select

'''
multiple select listbox
'''

# multi_list=c_driver.find_element('xpath','//Select[@id="multiple_cars"]')
# select2=Select(multi_list)

# ## select_by_index
# select2.select_by_index(1)
# select2.select_by_index(2)

# -------------------------------------------------------------
# ## deselect_by_index
# select2.deselect_by_index(1)
# time.sleep(1)

# ------------------------------------------------------------

# ## select_by_value

# time.sleep(3)
# select_obj.select_by_value("aud")
# select_obj.select_by_value("bmw")

# --------------------------------------------------------------
# select_obj.select_by_visible_text("BMW")
# select_obj.select_by_visible_text("Land Rover")
# select_obj.deselect_by_index(1)


# deselect by visible text
# select_obj.deselect_by_visible_text("BMW")

# select_obj.deselect_all()

'''     
is_multiple :   
'''
# print(select1.is_multiple)
# print(select2.is_multiple)
#
# all_option=select2.all_selected_options
# print(all_option)

#
# for ele in all_option:
#     print(ele.text)



# first=select2.first_selected_option
# print(first.text)

# options
'''
all_selected_options
'''
#
# allelements=select2.options
# print(allelements)



# for i in allelements:
#     print(i.text)








# -------------------------------------------------------------------------------

'''     NORMAL LISTBOXES        '''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://www.irctc.co.in/nget/train-search")
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="OK"]').click()
# time.sleep(2)
#
# driver.find_element('xpath', '(//div[@role="button"])[1]').click()
# time.sleep(2)
#
# driver.find_element('xpath', '//span[text()="Vistadome Chair Car (VC)"]').click()
# time.sleep(2)
#
# driver.find_element('xpath', '(//div[@role="button"])[2]').click()
# time.sleep(2)
#
# driver.find_element('xpath', '//span[text()="TATKAL"]').click()
