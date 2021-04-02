"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/2 9:02 下午'
"""
import pytest


@pytest.fixture(scope="session")
def login():
    # yield 前面相当于 setup
    print("这里实现登录操作")
    token = "j;fdkafjadfa"
    # yield 相当于return
    yield
    # yield 后面相当于teardown操作
    print("实现登出操作")


@pytest.fixture()
def connectDB():
    print("连接数据库")
