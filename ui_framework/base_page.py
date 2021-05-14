# 基类， 完成底层封装，比如常用的一些方法，初始化 driver，find。。。。
# 实现底层封装，它也可以被复用，所以这段代码属于框架层

import logging

import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

root = logging.getLogger()
print(root.handlers)
for h in root.handlers[:]:
    root.removeHandler(h)


class BasePage:
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    # 如果添加的功能越来越多， find 方法会无限增长
    # 如果 find 方法代码增加非常的话，会很难维护
    # 解决：可以利用装饰器进行功能增强，把黑名单放到装饰器，增强 find 方法
    def find(self, by, value):
        # 黑名单处理逻辑
        logging.info(by)
        logging.info(value)
        return self.driver.find_element(by, value)

    def swipe_find(self, text, num=3):
        # num = 3
        for i in range(0, num):
            if i == num - 1:
                raise NoSuchElementException(f"找了{num - 1}没有找到元素")
            try:
                return self.find(MobileBy.XPATH, f"//*[@text='{text}']")
            except:
                print("未找到，滑动")
                # 'width', 'height'
                size = self.driver.get_window_size()
                width = size['width']
                height = size['height']

                startx = width / 2
                starty = height * 0.8
                endx = startx
                endy = height * 0.3

                duration = 2000  # 2s
                self.driver.swipe(startx, starty, endx, endy, duration)

    # 关键字驱动代码
    # 功能：可以解析关键字文件，对文件中的字符串进行一一处理，从而实现关键字操作
    # 多个 step 之间，如果调用了 self.driver.findelement ，就会触发隐式等待，就不会使用 sleep
    def run_steps(self, path, function_name):
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        steps = data.get(function_name)
        # 每一个 step 的格式是 {'action': ,'by': , 'value':}
        for step in steps:
            # 如果键的值是 click 的话，代表想要点击元素
            if step.get("action") == "click":
                self.find(step.get("by"), step.get("value")).click()
            # 封装了输入框关键字
            elif step.get("action") == "send_keys":
                self.find(step.get("by"), step.get("value")).send_keys(step.get("content"))
