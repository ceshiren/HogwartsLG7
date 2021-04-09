import time

from selenium import webdriver


class BasePage:
    """
    封装页面通用方法，比如driver的实例化
    """
    def __init__(self, base_driver = None):
        """
        :param base_driver: 传入driver 实例对象
        """
        # 如果 base_driver 是初始值None，那么就会实例化driver
        if base_driver is not None:
            self.driver = base_driver
        else:
            # 使用浏览器复用模式
            chrome_arg = webdriver.ChromeOptions()
            # 加入调试地址
            chrome_arg.debugger_address = '127.0.0.1:9222'
            # 实例化driver对象
            self.driver = webdriver.Chrome(options=chrome_arg)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            # 隐式等待，会在每次find 操作的时候，轮询查找该元素，超时报错
            self.driver.implicitly_wait(3)

    def find(self, locator):
        # 解元祖的操作
        return self.driver.find_element(*locator)