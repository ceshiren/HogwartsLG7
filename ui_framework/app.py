"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/16 8:38 下午'
"""

# app 包含了 appium 初始化操作，这个操作在各业务线都能复用，所以 app 的代码可以是框架的一部分


from appium import webdriver

from test_appium.pages.base_page import BasePage
from ui_framework.page.index_page import IndexPage


class App(BasePage):
    def start(self):
        if self.driver == None:
            print("driver == None, 创建driver")
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "hogwarts"
            # Mac/Linux: adb logcat |grep -i activitymanager (-i忽略大小写)
            # Windows:  adb logcat |findstr /i activitymanager
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".view.WelcomeActivityAlias"
            # 防止清空缓存-比如登录信息
            caps["noReset"] = "true"
            # 最重要的一步，与server 建立连接
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            # 隐式等待 5 秒
            self.driver.implicitly_wait(25)
        else:
            print("复用driver")
            self.restart()
        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        self.driver.quit()

    def goto_main(self):
        # 页面的入口方法
        return IndexPage(self.driver)
