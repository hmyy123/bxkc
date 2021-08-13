import unittest
from appium import webdriver
import time
from appTest.LoginPage import login
from appTest.base import base
from appTest.readData.readExcel import ExcelUtil
from ddt import data, ddt

e = ExcelUtil("login")
eData = e.dict_data()


@ddt
class test_normal_login(base):
    @data(*eData)
    def test_normal(self, value):
        '''
        正常用户登陆测试
        '''
        username = e.value_re(value["username"])
        password = e.value_re(value["password"])
        phone_error_text, password_error_text, home = login.normal_login(self.driver, username, password)
        # print(username,password)
        # print(phone_error_text, password_error_text)
        if phone_error_text == "" and password_error_text == "":
            self.assertTrue(home, "登陆失败")
        elif phone_error_text != "":
            self.assertEqual(value["phoneText"], phone_error_text, "手机号不正确 ")
        elif password_error_text != "":
            self.assertEqual(value["pwdText"], password_error_text, "密码不正确 ")


            # self.driver.find_element_by_id()
