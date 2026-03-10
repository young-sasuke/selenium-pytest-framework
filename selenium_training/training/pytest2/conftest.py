from selenium import webdriver
import time
import pytest
@pytest.fixture(autouse=True,scope="module")
def setup():
    optn = webdriver.ChromeOptions()
    optn.add_experimental_option("detach", True)
    # from selenium.webdriver.common.action_chains import ActionChains

    c_driver = webdriver.Chrome(optn)

    c_driver.get("https://demowebshop.tricentis.com/")
    yield c_driver





# --------------------------------------------------------------------------------------------

'''

pytest_addoption() is used to add custom command-line arguments to pytest.
That means:
    We can define our own options
    User can pass values from terminal
    Pytest makes those values available inside tests and fixtures

Flow:
    User passes value from terminal
    pytest_addoption registers the option
    Pytest stores the value
    request.config.getoption() retrieves it

NOTE    :   pytest_addoption function should be defined only in conftest file.

To execute  :
    Right click --> open in terminal --> pytest test_filename.py -vs --browser=="browser_name"

'''

#
# import time
# import pytest
#
# from selenium import webdriver
#
# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser",
#         action="store",
#         default='chrome',
#         help="Browser to run tests  :   chrome/firefox/edge"
#     )
#
# @pytest.fixture(scope='class')
# def setup(request):
#     browser = request.config.getoption("--browser")
#
#     if browser == 'chrome':
#         driver = webdriver.Chrome()
#     elif browser == 'firefox':
#         driver = webdriver.Firefox()
#     elif browser == 'edge':
#         driver = webdriver.Edge()
#
#     driver.get("https://demowebshop.tricentis.com/")
#     time.sleep(2)
#     yield driver
#     driver.close()
#





