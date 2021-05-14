"""
mitmdump -s 参数示例
"""

"""
Basic skeleton of a mitmproxy addon.

Run as follows: mitmproxy -s anatomy.py
"""
from mitmproxy import ctx


class AD:
    def __init__(self):
        self.num = 0

    def request(self, flow):
        self.num = self.num + 1
        ctx.log.info("我们看到了 %d 流水" % self.num)

# 插件机制，必须要使用addons 变量，
# 使用列表，存放相关的实例对象
addons = [
    AD()
]