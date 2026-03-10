
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

# prefs = {
#     n"download.default_directory":r"C:\Users\KIIT\PycharmProjects\selenium_project\training",
#     "profile.password_manager_leak_detection": False
#
# }
# driver.add_experimental_option("prefs", prefs)
driver.add_argument("--disable-notifications")
# # in case of firefox there is set_preference function
#
#
c_driver =webdriver.Chrome(driver)
# driver=webdriver.FirefoxOptions()
# driver.add_experimental_option("detach" ,True)
# driver.set_


# c_driver =webdriver.Firefox(driver)


c_driver.get("https://demoqa.com/upload-download")
c_driver.find_element('xpath','//a[@id="downloadButton"]').click()
#
# time.sleep(2)
#
# file1=r"C:\Users\KIIT\PycharmProjects\selenium_project\selenium_training\training\demo.html"




# # we cannot click directly to the input file because after that the command go out of selenium because it open local files thats why selenium doesnot allow that
'''     Uploading single file       '''

# c_driver.find_element('xpath','//input[@id="singleFileInput"]').send_keys(file1)
# c_driver.find_element('xpath','//button[text()="Upload Single File"]').click()




# file2=r"C:\Users\KIIT\PycharmProjects\selenium_project\selenium_training\training\browser_methods.py"

'''     Uploading Multiple files       '''
# c_driver.find_element('xpath','//input[@id="multipleFilesInput"]').send_keys(f'{file1}\n{file2}')
# c_driver.find_element('xpath','//button[text()="Upload Multiple Files"]').click()




















# -----------------------------------------------------------------------------------------------



'''     To download the files in different location     '''


# ## Chrome
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# prefs = {
#     "download.default_directory": r'C:\Users\Ramya\PycharmProjects\selenium_KIIT\files',
#     "download.prompt_for_download":False,
#     "safebrowsing.enabled":True,
#     "plugins.always_open_pdf_externally":True
# }
#
# opts.add_experimental_option("prefs", prefs)
#
# driver = webdriver.Chrome(opts)
# driver.implicitly_wait(10)
#
#
# driver.get("https://demoqa.com/upload-download")
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Download"]').click()

##---------------------------------------------------------------

## Firefox


# from selenium import webdriver
#
# opts = webdriver.FirefoxOptions()
#
# opts.set_preference("browser.download.folderList", 2)
# opts.set_preference("browser.download.dir", r'C:\Users\Ramya\PycharmProjects\selenium_KIIT\locators_')
#
# driver = webdriver.Firefox(opts)
# driver.implicitly_wait(10)
#
#
# driver.get("https://demoqa.com/upload-download")
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Download"]').click()







