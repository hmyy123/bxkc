from appTest.base2 import base2
from appTest.IndexPage.subscribe import subscribe
from appTest.readData.readExcel import ExcelUtil
from ddt import data, ddt

e = ExcelUtil("subscribe")
eData = e.dict_data()


@ddt
class test_subscribe(base2):
    #
    def test_admin(self):
        '''
        是否需要登陆
        '''
        text, status = subscribe.index(self.driver)
        if text == "":
            self.assertTrue(status, "没有登陆")
        else:
            self.assertEqual("首页", text, "登陆失败")

    @data(*eData)
    def test_subAdd(self, value):
        '''
        增加订阅信息
        '''
        key_text, title, detail_title = subscribe(self.driver, value["keyword"], value["scope"], value["model"],
                                                  value["email"], value["flag"]).add_sub()
        title = "".join(title.split())
        detail_title = "".join(detail_title.split())
        self.assertIn(value["keyword"].split(",")[0], key_text, "订阅关键词错误")
        self.assertEqual(title, detail_title, "详情打开错误")

    @data(*eData)
    def test_subAdd_nzj(self, value):
        title, detail_title = subscribe(self.driver, value["keyword"], value["scope"], value["model"],
                                        value["email"], value["flag"]).add_sub_nzj(value["exclude"])
        title = "".join(title.split())
        detail_title = "".join(detail_title.split())
        self.assertEqual(title, detail_title, "订阅拟在建详情打开错误")

    def test_delete(self):
        '''
        删除订阅信息
        '''
        status = subscribe.delete_sub(self.driver)
        self.assertTrue(status, "删除订阅出错")
