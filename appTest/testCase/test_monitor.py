from appTest.base2 import base2
from appTest.IndexPage.monitor import monitor
from appTest.readData.readExcel import ExcelUtil
from ddt import data, ddt

e = ExcelUtil("monitor")
eData = e.dict_data()


@ddt
class test_monitor(base2):

    def test_admin(self):
        '''
        是否需要登陆
        '''
        text, status = monitor.index(self.driver)
        if text == "":
            self.assertTrue(status, "没有登陆")
        else:
            self.assertEqual("首页", text, "登陆失败")

    @data(*eData)
    def test_add_proxy(self, value):
        '''
        添加代理监测
        '''
        key_text, title, detail_title = monitor(self.driver, value["company"], value["keyword"], value["scope"],
                                                value["model"], value["exclude"], value["email"], value["flag"],
                                                value["type"]).add_proxy()
