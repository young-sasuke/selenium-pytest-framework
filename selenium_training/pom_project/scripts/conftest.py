import pytest
from selenium import webdriver

@pytest.fixture()
def setup():

    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()

    yield driver

    driver.quit()