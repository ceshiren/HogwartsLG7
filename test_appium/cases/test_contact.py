"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/16 8:48 下午'
"""
from time import sleep
import sys

sys.path.append('..')
from test_appium.pages.app import App


class TestContact:

    def setup_class(self):
        # 打开应用，进入到首页
        self.app = App()

    def setup(self):
        self.main = self.app.start().goto_main()

    def teardown_class(self):
        self.app.stop()

    def test_addcontact(self):
        username = "hogwarts05"
        phonenum = "13911111115"
        self.main.goto_contactlist().goto_addmemberpage() \
            .addmember_bymenual().edit_member(username, phonenum).verify_ok()

    def test_addcontact1(self):
        username = "hogwarts04"
        phonenum = "13911111114"
        self.main.goto_contactlist().goto_addmemberpage() \
            .addmember_bymenual().edit_member(username, phonenum).verify_ok()
