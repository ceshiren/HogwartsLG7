"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/16 8:48 下午'
"""
from time import sleep

from test_appium.pages.app import App


class TestContact:
    def setup(self):
        # 打开应用，进入到首页
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    def test_addcontact(self):
        username = "hogwarts01"
        phonenum = "13911111111"
        self.main.goto_contactlist().goto_addmemberpage() \
            .addmember_bymenual().edit_member(username, phonenum).verify_ok()
