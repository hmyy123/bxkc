import unittest
from appium import webdriver
import time
from appTest.LoginPage import login
from appTest.base import base



class test_visitor_login(base):
    def test_visitor(self):
        '''
        游客登陆测试
        '''
        page,text = login.visitor_login(self.driver)
        # self.driver.find_element_by_id()
        self.assertEqual(text, "首页", "游客登陆失败")
        self.assertTrue(page,"第一次进入没有引导页")


if __name__ == "__main__":
    unittest.main()
