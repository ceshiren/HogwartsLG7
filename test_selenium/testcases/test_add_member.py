import pytest

from test_selenium.page.main_page import MainPage

class TestAddMember:
    def setup_class(self):
        self.main = MainPage()

    @pytest.mark.parametrize("name", ["皮城女警"])
    def test_add_member(self, name):
        """
        用来测试添加成员功能
        :return:
        """
        #    1. 跳转到添加成员页面 2. 添加成员 3. 获取成员列表，做断言验证
                    # AddMemberPage()
        res = self.main.goto_add_member().add_member(name).get_list()
        assert name in res

    def test_add_member_fail(self):
        self.main.goto_add_member().add_member_fail("女警2")