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


def test_add_favorite(browser):
    url = 'https://www.ss.com/en'
    browser.get(url)

    assert 'SS.COM' in browser.title, 'Wrong page!'

    browser.find_element_by_id('mtd_97').click()  # cars
    sleep(2)
    assert 'Cars' in browser.title, 'Wrong section!'

    browser.find_element_by_xpath("//select[@name='opt[35]']/option[text()='Manual']").click()
    sleep(5)

    browser.find_element_by_xpath("//form[@id='filter_frm']/table[2]/tbody/tr[5]").click()
    sleep(5)

    browser.find_element_by_xpath("/html//a[@id='a_fav']").click() # add to favorites
    sleep(5)

    browser.find_element_by_xpath("/html//a[@id='alert_ok']").click()
    sleep(5)

    browser.find_element_by_xpath(
        "//div[@id='main_table']/span[@class='page_header_menu']/span/b[@class='menu_main']/a[@title='Memo']").click()
    sleep(5)
    memo_row = len(browser.find_elements_by_xpath("//form[@id='filter_frm']/table/tbody/tr"))

    assert int(memo_row) > 1, "No ad's are added!"






