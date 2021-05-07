import pytest

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def browser():
    driver = Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_open_ad(browser):
    url = 'https://www.ss.com/en'
    browser.get(url)

    assert 'SS.COM' in browser.title, 'Wrong page!' #test
