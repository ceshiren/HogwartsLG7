"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/2 8:46 下午'
"""


# yield 关键字， 一般用于生成器
def provider():
    for i in range(0, 10):
        print("start")
        yield i  # 相当于return 操作，返回数据，并且记录了上一次的执行位置，下一次的时候继续执行。
        print("end")


p = provider()
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
