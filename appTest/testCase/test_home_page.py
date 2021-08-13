from appTest.IndexPage.IndexHome import homePage
import unittest
from appium import webdriver
from BeautifulReport import BeautifulReport


class test_home_page(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.d = {}
        self.d["platformName"] = "Android"
        self.d["platformNameVersion"] = "9.0"
        # self.d["deviceName"] = "RMSNW18C28004552"
        self.d["deviceName"] = "H6D6DUJ7MV95U4DI"
        self.d["appPackage"] = "com.bxkc.android"
        self.d["appActivity"] = "com.bxkc.android.activity.WelcomeActivity"
        self.d["noReset"] = False
        # self.d["skipServerInstallation"] = True
        # self.d["skipDeviceInitialization"] = True
        self.driver = webdriver.Remote(r"http://127.0.0.1:4723/wd/hub", self.d)
        self.driver.implicitly_wait(10)

    def test_aindex(self):
        '''
        用户登陆首页测试
        '''
        text = homePage(self.driver).get_index_home()
        # self.driver.find_element_by_id()
        self.assertEqual(text, "首页", "登陆失败")

    def test_index_page(self):
        '''
        首页详情测试
        '''
        title, detail_title = homePage(self.driver).get_index_page()
        title="".join(title.split())
        detail_title="".join(detail_title.split())
        self.assertEqual(title, detail_title, "详情页有误")

    def test_search_project(self):
        '''
        查项目测试
        '''
        title = homePage(self.driver).search_project()
        title = "".join(title.split())
        self.assertIn("电梯",title,"项目搜索有误")


    def test_ctb(self):
        '''
        查招标
        '''
        title, detail_title = homePage(self.driver).ctb()
        title = "".join(title.split())
        detail_title = "".join(detail_title.split())
        self.assertEqual(title, detail_title, "查招标有误")

    def test_czb(self):
        '''
        查中标
        '''
        title, detail_title = homePage(self.driver).czb()
        title = "".join(title.split())
        detail_title = "".join(detail_title.split())
        self.assertEqual(title, detail_title, "查中标有误")

    def test_cnzj(self):
        '''
        查拟在建
        '''
        title, detail_title = homePage(self.driver).cnzj()
        title = "".join(title.split())
        detail_title = "".join(detail_title.split())
        self.assertEqual(title, detail_title, "查拟在建有误")

    def test_sjdc(self):
        '''
        数据导出
        '''
        text = homePage(self.driver).sjdc()
        self.assertEqual(text, "预览数据", "数据导出有误")

    def test_bsdx(self):
        '''
        标书代写
        '''
        text = homePage(self.driver).bsdx()
        self.assertEqual(text, "标书代写", "标书代写有误")

    def test_qybg(self):
        '''
        企业报告
        '''
        text1,text2 = homePage(self.driver).qybg()
        self.assertEqual(text1, "下载报告", "企业报告有误")
        self.assertEqual(text2, "下载报告", "企业报告有误")

    def test_hybg(self):
        '''
        行业报告
        '''
        text = homePage(self.driver).hybg()
        self.assertEqual(text, "下载报告", "行业报告有误")

    def test_gnjs(self):
        '''
        功能介绍
        '''
        text = homePage(self.driver).gnjs()
        self.assertEqual(text, "1、如何查招标信息", "功能介绍有误")

    def test_gdgn(self):
        '''
        更多功能
        '''
        text = homePage(self.driver).gdgn()
        self.assertEqual(text, "招标预告", "更多功能有误")

    def test_qyxxk(self):
        '''
        企业信息库
        '''
        text = homePage(self.driver).qyxxk()
        self.assertEqual(text, "查看联系电话", "企业信息库有误")

    def test_cqy(self):
        '''
        查企业
        '''
        text = homePage(self.driver).cqy()
        self.assertIn("中国能源", text, "查企业有误")

    def test_cqybg(self):
        '''
        查企业报告
        '''
        text1, text2 = homePage(self.driver).cqybg()
        self.assertIn("中国能源", text1, "查企业报告有误")
        self.assertIn("中国能源", text2, "查企业报告有误")

    def test_chybg(self):
        '''
        查行业报告
        '''
        text = homePage(self.driver).chybg()
        self.assertIn("服务", text, "查行业报告有误")


    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
