# 雪球的首页 page
# 可以直接继承 basepage ，调用已经封装好的 UI 操作
# By.XPATH == "xpath"

import yaml
from ui_framework.base_page import BasePage
class IndexPage(BasePage):
    # 进入行情页面
    def goto_market(self):
        # self.find("xpath", "//*[@text='行情']").click()
        # # data 格式 {'goto_market': [{'action': 'click', 'by': 'xpath', 'value': "//*[@text='行情']"}]}
        # # 函数名：[{'action': ,'by': , 'value':}, {}, {}]
        self.run_steps("../page/index_pate.yaml", "goto_market")

