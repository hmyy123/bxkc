import unittest
from appium import webdriver
import time
from appTest.LoginPage.register import register
from appTest.base import base
from appTest.readData.readExcel import ExcelUtil
from ddt import data, ddt

e = ExcelUtil("regsiter")
eData = e.dict_data()


@ddt
class test_user_register(base):
    @data(*eData)
    def test_register(self, value):
        '''
        用户注册测试
        '''
        phone = e.value_re(value["phone"])
        code = e.value_re(value["code"])
        is_True= e.value_re(value["isTrue"])
        phone_error_text, toast_error_text, code_error_text, home = register(self.driver, phone, code,
                                                                             is_True, value["company"],
                                                                             value["name"],
                                                                             value["position"]).user_reg()
        if phone_error_text=="" and toast_error_text=="" and code_error_text=="":
            self.assertTrue(home,"注册失败")
        if phone_error_text is not None:
            self.assertEqual(phone_error_text,value["phone_error_text"],"手机号输入有误")
        if toast_error_text is not None:
            self.assertEqual(toast_error_text,value["toast_error_text"],"toast提示有误")
        if code_error_text is not None:
            self.assertEqual(code_error_text,value["code_error_text"],"验证码提示有误")
