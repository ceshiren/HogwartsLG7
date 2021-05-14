"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/16 8:40 下午'
"""

# 首页的封装
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from test_appium.pages.base_page import BasePage
from test_appium.pages.contactlist_page import ContacListPage


class IndexPage(BasePage):
    # def __init__(self, driver: WebDriver):
    #     self.driver = driver

    def goto_contactlist(self):
        # click [通讯录]
        self.find(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return ContacListPage(self.driver)
