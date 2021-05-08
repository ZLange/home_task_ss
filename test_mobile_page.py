# import pytest
# from time import sleep
#
# from selenium.webdriver import Chrome
# from selenium.webdriver.common.keys import Keys
#
# @pytest.fixture
# def browser():
#     driver = Chrome()
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()
#
#
# def test_remove_fav(browser):
#     url = 'https://www.ss.com/en'
#     browser.get(url)
#     browser.Manage().Window.Size = (240, 360)
#
#     assert 'SS.COM' in browser.title, 'Wrong page!'
#
#     browser.find_element_by_id('mtd_97').click()  # cars
#     sleep(2)
#     assert 'Cars' in browser.title, 'Wrong section!'