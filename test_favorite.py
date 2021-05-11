import pytest
from time import sleep

from selenium.webdriver import Chrome
# from selenium.webdriver.common.keys import Keys


@pytest.fixture
def browser():
    driver = Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


"""
Web browser: Chrome
Smoke tests for ss.com
Tests validates:
- opening of ss.com page
- opening of ad
- adding add to favorites
- opening memos tab 
- checking that latest added ad is in memos
"""

def test_add_favorite(browser):
    url = 'https://www.ss.com/en'
    browser.get(url)

    assert 'SS.COM' in browser.title, 'Wrong page!'

    browser.find_element_by_id('mtd_97').click()  # cars
    sleep(2)
    assert 'Cars' in browser.title, 'Wrong section!'

    # browser.find_element_by_xpath("//select[@name='opt[35]']/option[text()='Manual']").click()
    browser.find_element_by_xpath("//select[@name='opt[32]']/option[text()='Coupe']").click()
    sleep(5)

    min_price = browser.find_element_by_id("f_o_8_min")
    min_price.send_keys('3000')
    # minprice = browser.find_element_by_xpath("//table[@id='filter_tbl']/tbody/tr/td[1]/table//tr/td[1]/span/input[@name='topt[8][min]']").get_attribute("value")
    # print('*************min***************', minprice)

    max_price = browser.find_element_by_id("f_o_8_max")
    max_price.send_keys('20000')
    # maxprice = browser.find_element_by_xpath("//table[@id='filter_tbl']/tbody/tr/td[1]/table//tr/td[1]/span/input[@name='topt[8][max]']").get_attribute("value")
    # print('***************max*************', maxprice)

    browser.find_element_by_xpath("//table[@id='filter_tbl']/tbody/tr/td[2]/input[@value='Search']").click()

    browser.find_element_by_xpath("//form[@id='filter_frm']/table[2]/tbody/tr[7]").click()
    sleep(5)

    # price = browser.find_element_by_xpath("//div[@id='msg_div_msg']/table[2]//td[@class='ads_price']//span[@class='ads_price']").get_attribute("innertext")
    # print('***************price*************', price) # can't get price it is not given as value
    # assert minprice <= price <= maxprice  # should check if price is in needed range

    browser.find_element_by_xpath("/html//a[@id='a_fav']").click()  # add to favorites
    sleep(5)

    browser.find_element_by_xpath("/html//a[@id='alert_ok']").click()
    sleep(5)

    browser.find_element_by_xpath("//div[@id='main_table']/span[@class='page_header_menu']/span/b[@class='menu_main']/a[@title='Memo']").click()
    sleep(5)
    memo_row = len(browser.find_elements_by_xpath("//form[@id='filter_frm']/table/tbody/tr"))

    assert int(memo_row) > 1, "No ad's was added!"







