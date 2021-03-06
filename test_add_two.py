import pytest
from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def browser():
    driver = Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_add_two(browser):
    url = 'https://www.ss.com/en'
    browser.get(url)

    assert 'SS.COM' in browser.title, 'Wrong page!'

    browser.find_element_by_id('mtd_97').click()  # cars
    sleep(2)
    assert 'Cars' in browser.title, 'Wrong section!'

    browser.find_element_by_xpath("//select[@name='opt[35]']/option[text()='Manual']").click()
    # browser.find_element_by_xpath("//select[@name='opt[32]']/option[text()='Coupe']").click()
    sleep(5)

    browser.find_element_by_xpath("//table[@id='filter_tbl']/tbody/tr/td[2]/input[@value='Search']").click()

    # select first ad
    browser.find_element_by_xpath("//form[@id='filter_frm']/table[2]/tbody/tr[2]//input[@name='mid[]']").click()
    # select second ad
    browser.find_element_by_xpath("//form[@id='filter_frm']/table[2]/tbody/tr[3]//input[@name='mid[]']").click()
    sleep(5)

    # browser.execute_script("window.scrollTo(0, Y)")

    browser.find_element_by_xpath("/html//a[@id='a_fav_sel']").click()  # add to favorites
    sleep(5)

    browser.find_element_by_xpath("/html//a[@id='alert_ok']").click()
    sleep(5)

    browser.find_element_by_xpath("//div[@id='main_table']/span[@class='page_header_menu']/span/b[@class='menu_main']/a[@title='Memo']").click()
    sleep(5)
    memo_row = len(browser.find_elements_by_xpath("//form[@id='filter_frm']/table/tbody/tr"))

    assert int(memo_row) > 1, "No ad's was added!"
    assert int(memo_row) < 3, "Not all ad's was added!"







