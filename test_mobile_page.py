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


def test_remove_fav(browser):
    url = 'https://m.ss.com/en'
    browser.get(url)

    assert 'SS.COM' in browser.title, 'Wrong page!'

    browser.find_element_by_xpath("//div[@id='main']//a[@href='/en/transport/']/div[@class='cat2']").click()
    sleep(2)
    assert 'Transport' in browser.title, 'Wrong section!'

    browser.find_element_by_xpath("//div[@id='main']//a[@href='/en/transport/cars/']").click()
    sleep(2)
    assert 'Cars' in browser.title, 'Wrong section!'

    browser.find_element_by_xpath("//div[@id='main']//a[@href='/en/transport/cars/mercedes/']").click()
    sleep(2)
    assert 'Mercedes' in browser.title, 'Wrong section!'

    browser.find_element_by_xpath("//div[@id='main']//a[@href='/en/transport/cars/mercedes/clk-class/']").click()
    sleep(2)
    assert 'CLK-class' in browser.title, 'Wrong section!'
