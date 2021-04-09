from selenium import webdriver
from selenium.webdriver.common.by import By

from test_selenium.page.basepage import BasePage
from test_selenium.page.contact_page import ContactPage


class AddMemberPage(BasePage):

    def add_member(self, name):

        # self.driver.find_element(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()
        # 添加姓名、 账号、 手机号
        self.driver.find_element(By.ID, "username").send_keys(name)
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("111")
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys("13199991111")
        # 点击保存
        self.driver.find_element(By.CSS_SELECTOR, ".qui_btn.ww_btn.js_btn_save").click()
        return ContactPage(self.driver)

    def add_member_fail(self, name):
        self.driver.find_element(By.ID, "username").send_keys(name)
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("11122")
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys("13199991111")
        # 点击保存
        self.driver.find_element(By.CSS_SELECTOR, ".qui_btn.ww_btn.js_btn_save").click()
        ele_list = self.driver.find_elements(By.CSS_SELECTOR, ".ww_inputWithTips_tips")
        error_list = [i.text for i in ele_list]
        print(error_list)
        # return ContactPage(self.driver)


    def goto_contact(self):
        pass
