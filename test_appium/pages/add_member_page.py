"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/16 8:43 下午'
"""
#
# from test_appium.pages.editmember_page import EditMemberPage
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class AddMemberPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def addmember_bymenual(self):
        # click [手动输入添加]
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        from test_appium.pages.editmember_page import EditMemberPage
        return EditMemberPage(self.driver)

    def verify_ok(self):
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='添加成功']"))
