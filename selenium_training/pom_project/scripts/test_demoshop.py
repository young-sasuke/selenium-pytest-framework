

from   selenium_training.pom_project.pom.cartpage import CartPage
from selenium_training.pom_project.pom.homepage import HomePage
from selenium_training.pom_project.pom.loginpage import LogIn
from selenium_training.pom_project.pom.desktoppage import DesktopPage
from selenium_training.pom_project.pom.simple_comp_page import Simple_Comp

import time





from selenium_training.pom_project.generic_utilities.excel_utility import read_excel

data = read_excel()
## {'valid_email': 'steve.jobs123@gmail.com', 'valid_pwd': 'stevejobs', 'country': 'India', 'pincode': 5632014.0, 'sortby': 'Price: Low to High', 'viewas': 'List'}
print(data)

def test_case1(setup):
    hp = HomePage(setup)
    lp = LogIn(setup)
    dp = DesktopPage(setup)
    sp = Simple_Comp(setup)
    cp = CartPage(setup)

    hp.click_login()
    lp.enter_email(data['valid_email'])
    lp.enter_password(data['valid_pwd'])
    lp.click_to_login()
    hp.check_login()
    time.sleep(5)
    hp.hovor_to_computers()
    hp.click_to_desktop()
    dp.Select_sort(data['sortby'])
    dp.Select_view(data['viewas'])
    dp.Scroll_down()
    time.sleep(5)
    dp.Click_to_simplecomputer()
    sp.choose_processor()
    sp.click_to_addtocart()
    sp.go_to_home()
    hp.click_to_soppingcart()
    cp.select_country(data['country'])
    cp.select_state()
    cp.enter_post(data['pincode'])
    cp.click_on_terms()
    cp.clcik_on_check_out()


