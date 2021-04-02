"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/2 8:05 下午'
"""
import pytest

from pytestdemo.calculator import Calculator


class TestCal:
    def setup(self):
        print("开始计算")

    def teardown(self):
        print("结束计算")

    @pytest.mark.parametrize('a,b,expect',[
        [1,1,2],[100,100,200]
    ])
    def test_add_int(self,a,b,expect):
        cal = Calculator()
        assert expect == cal.add(a, b)

    @pytest.mark.parametrize('a,b,expect', [
        [0.1, 0.1, 0.2], [0.1, 0.2, 0.3]
    ],ids=['float1','float2'])
    def test_add_float(self, a, b, expect):
        cal = Calculator()
        assert expect == round(cal.add(a, b),2)

    def test_div(self):
        cal = Calculator()
        # try:
        #     cal.div(1, 0)
        # except ZeroDivisionError:
        #     print("除数为0")
        with pytest.raises(ZeroDivisionError):
            cal.div(1, 0)
