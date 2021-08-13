import unittest
from appium import webdriver
import time
from appTest.LoginPage.forget import forget
from appTest.base import base
from appTest.readData.readExcel import ExcelUtil
from ddt import data, ddt

e = ExcelUtil("forget")
eData = e.dict_data()


@ddt
class test_pwd_forget(base):
    @data(*eData)
    def test_forget(self, value):
        '''
        用户忘记密码测试
        '''
        phone = e.value_re(value["phone"])
        code = e.value_re(value["code"])
        password = e.value_re(value["password"])
        phone_error_text, password_error_text, code_error_text, text = forget(self.driver, phone, code,
                                                                              password).modify_pwd()
        # print(username,password)
        # print(phone_error_text, password_error_text)
        if phone_error_text =="" and password_error_text=="" and code_error_text =="":
            self.assertEqual(text, "登录", "修改密码不成功")
        elif phone_error_text != "":
            self.assertEqual(value["phone_error_text"], phone_error_text, "手机号不正确 ")
        elif password_error_text != "":
            self.assertEqual(value["password_error_text"], password_error_text, "密码不正确 ")
        elif code_error_text != "":
            self.assertEqual(value["code_error_text"], code_error_text, "验证码不正确")

