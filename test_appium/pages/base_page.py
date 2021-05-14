"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/16 9:38 下午'
"""
# 基类， 完成底层封装，比如常用的一些方法，初始化 driver，find。。。。
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
import logging

root = logging.getLogger()
print(root.handlers)
for h in root.handlers[:]:
    root.removeHandler(h)


class BasePage:
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, value):
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
