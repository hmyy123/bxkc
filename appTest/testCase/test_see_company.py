from appTest.base2 import base2
from appTest.IndexPage.company import company


class test_see_company(base2):

    def test_admin(self):
        '''
        是否需要登陆
        '''
        text, status = company.index(self.driver)
        if text == "":
            self.assertTrue(status, "没有登陆")
        else:
            self.assertEqual("首页", text, "登陆失败")

    def test_index(self):
        '''
        查企业首页
        '''
        title, detail_title = company(self.driver).index_page()
        title = "".join(title.split())
        detail_title = "".join(detail_title.split())
        self.assertIn(title, detail_title, "查企业首页有误")

    def test_search(self):
        '''
        查企业搜索
        '''
        title, detail_title = company(self.driver).search()
        title = "".join(title.split())
        detail_title = "".join(detail_title.split())
        self.assertIn("电梯", title, "查企业搜索有误")
        self.assertIn(title, detail_title, "查企业搜索有误")

    def test_history(self):
        '''
        查企业-历史
        '''
        title, detail_title = company(self.driver).history()
        title = "".join(title.split())
        detail_title = "".join(detail_title.split())
        self.assertEqual(title, detail_title, "查企业历史记录有误")

    def test_collection(self):
        '''
        查企业-收藏
        '''
        title, detail_title = company(self.driver).collection()
        title = "".join(title.split())
        detail_title = "".join(detail_title.split())
        self.assertEqual(title, detail_title, "查企业历史记录有误")
