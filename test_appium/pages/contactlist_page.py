"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/16 8:42 下午'
"""
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from test_appium.pages.add_member_page import AddMemberPage


class ContacListPage(object):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def goto_addmemberpage(self):
        # click [添加成员]
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("添加成员").instance(0));').click()
        return AddMemberPage(self.driver)
