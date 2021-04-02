"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/2 8:05 下午'
"""
import allure
import pytest
import yaml


# pip install pyyaml
def get_datas():
    with open("./datas/calc.yml") as f:
        datas = yaml.safe_load(f)
    return datas


# @allure.feature("测试计算器")
class TestCal:

    @pytest.mark.parametrize('a,b,expect', get_datas()['add_int']['datas'])
    # @allure.story("测试相加功能_int")
    def test_add_int(self, calculate, a, b, expect):
        assert expect == calculate.add(a, b)

    @pytest.mark.parametrize('a,b,expect', get_datas()['add_float']['datas'], ids=get_datas()['add_float']['ids'])
    def test_add_float(self, calculate, a, b, expect):
        assert expect == round(calculate.add(a, b), 2)

    def test_div(self, calculate):
        # try:
        #     cal.div(1, 0)
        # except ZeroDivisionError:
        #     print("除数为0")
        with pytest.raises(ZeroDivisionError):
            calculate.div(1, 0)
