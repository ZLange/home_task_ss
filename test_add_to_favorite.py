# import pytest
# from selenium import webdriver
# from selenium.common.exceptions import InvalidSessionIdException
# from selenium.webdriver.common.keys import Keys
# from time import sleep
#
# # needed webpage
# url = 'https://www.ss.com/en'
#
# page = webdriver.Chrome()  # create Chrome session/ chromedriver needs to be in the same folder where run from
# page.implicitly_wait(30)
# page.get(url)
#
# """
# Web browser: Chrome
# Smoke tests for ss.com
# Tests validates:
# - opening of ss.com page
# - opening of ad
# - adding add to favorites
# - opening memos tab
# - checking that latest added ad is in memos
# """
#
#
# def test_open_url():
#     page.maximize_window()
#
#     assert 'SS.COM' in page.title, 'Page opened'
#
#     sleep(2)
#     page.close()
#
# # def test_open_add():
# #     # page.maximize_window()
# #     button = page.find_element_by_xpath('//*[@id="mtd_97"]')
# #     # button = page.find_element_by_id('mtd_97')
# #     button.click()
# #
# #     assert 'Cars' in page.title, 'Page opened'
# #
# #     sleep(5)
# #     page.close()
#
