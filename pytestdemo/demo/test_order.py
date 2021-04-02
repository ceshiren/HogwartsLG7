"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/2 9:41 下午'
"""
import pytest


@pytest.mark.run(order=2)
def test_foo():
    assert True


@pytest.mark.last
def test_last():
    print("last")


@pytest.mark.first
def test_bar():
    assert True
