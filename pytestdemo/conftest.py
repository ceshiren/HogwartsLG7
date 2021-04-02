"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/2 9:19 下午'
"""
import pytest

from calculator import Calculator


@pytest.fixture()
def calculate():
    print("开始计算")
    cal = Calculator()
    yield cal
    print("结束计算")
