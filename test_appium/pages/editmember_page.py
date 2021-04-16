"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/16 8:45 下午'
"""
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class EditMemberPage(object):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def edit_member(self, username, phonenum):
        # edit username

        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '姓名')]/../*[@text='必填']").send_keys(username)
        # edit phonenum
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '手机')]/..//*[@text='必填']").send_keys(phonenum)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()

        from test_appium.pages.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)
