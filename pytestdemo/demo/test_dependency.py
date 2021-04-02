"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/2 9:47 下午'
"""
import pytest


@pytest.mark.dependency()
@pytest.mark.xfail(reason="deliberate fail")
def test_a():
    assert False


@pytest.mark.dependency()
def test_b():
    pass


@pytest.mark.dependency(depends=["test_a"])
def test_c():
    pass


@pytest.mark.dependency(depends=["test_b"])
def test_d():
    pass


@pytest.mark.dependency(depends=["test_b", "test_c"])
def test_e():
    pass
