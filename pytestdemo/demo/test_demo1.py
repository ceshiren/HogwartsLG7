"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/2 9:06 下午'
"""


def test_search(login):
    # print(f"token is {login}")
    print("搜索111")


def test_cart(login):
    print("购物车1111")


# @pytest.mark.usefixtures('login')
def test_order(login, connectDB):
    # print(login)
    print('下单111 ')
