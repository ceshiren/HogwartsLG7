import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from test_selenium.page.add_member_page import AddMemberPage
from test_selenium.page.basepage import BasePage


class MainPage(BasePage):
    # 元素定位封装成了一个元祖
    add_member_ele = (By.CSS_SELECTOR, ".ww_indexImg_AddMember")

    def goto_add_member(self):
        # self.driver.find_element(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()
        self.find(self.add_member_ele).click()
        return AddMemberPage(self.driver)

    def goto_contact(self):
        pass


    def demo(self):
        """
        解元祖示例
        :return:
        """
        a = (1,2) # 1,2
        self.demo2(*a) # = demo2(1,2)

    def demo2(self, a, b):
        print(a, b)