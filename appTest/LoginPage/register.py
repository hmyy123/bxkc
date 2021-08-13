from appTest.readData.elementData import getElement
from appTest.Element.elementBase import isElement
from appTest.Element import elementBase
from appTest.Database.db import db
from appTest.Database.phone import phone
import time


class register:
    def __init__(self, driver, phone, code, flag,company,name,position):
        self.driver = driver
        self.phone = phone
        self.code = code
        self.flag = flag
        self.company = company
        self.name = name
        self.position = position

    def user_reg(self):
        phone_error_text = ""
        code_error_text = ""
        toast_text = ""
        home=""
        if isElement(self.driver, "id", getElement("Login", "agree")):
            elementBase.e_click(self.driver, getElement("Login", "agree"))
        for i in range(4):
            if isElement(self.driver, "id", getElement("Login", "allow")):
                elementBase.e_click(self.driver, getElement("Login", "allow"))
        elementBase.e_click(self.driver, getElement("Login", "login"))
        elementBase.e_click(self.driver, getElement("Login", "register"))

        if self.phone == 0:
            self.phone = phone().get_phone()
        elementBase.e_send_key(self.driver, getElement("Register", "phone"), self.phone)
        elementBase.e_click(self.driver, getElement("Register", "getcode"))
        if self.code=="":
            if elementBase.isElement(self.driver, "xpath", getElement("Register", "toast")):
                toast_text = elementBase.e_text_xpath(self.driver, getElement("Register", "toast"))
                return phone_error_text, toast_text, code_error_text, home
        if self.code ==0:
            self.code = db(self.phone).get_code()
        elementBase.e_send_key(self.driver, getElement("Register", "code"), self.code)
        if self.flag == 1:
            elementBase.e_tap(self.driver, 58, 886)
        elementBase.e_click(self.driver, getElement("Register", "register"))
        if self.flag ==0:
            if elementBase.isElement(self.driver, "xpath", getElement("Register", "toast")):
                toast_text = elementBase.e_text_xpath(self.driver, getElement("Register", "toast"))
                return phone_error_text, toast_text, code_error_text, home
        if elementBase.isElement(self.driver,"id",getElement("Register","code_toast")):
            code_error_text = elementBase.e_text(self.driver, getElement("Register", "code_toast"))
            return phone_error_text, toast_text, code_error_text, home
        if elementBase.isElement(self.driver, "id", getElement("Register", "phone_error")):
            phone_error_text = elementBase.e_text(self.driver, getElement("Register", "phone_error"))
            return phone_error_text, toast_text, code_error_text, home
        if elementBase.isElement(self.driver, "id", getElement("Register", "code_error")):
            code_error_text = elementBase.e_text(self.driver, getElement("Register", "code_error"))
            return phone_error_text, toast_text, code_error_text, home
        if elementBase.isElement(self.driver, "id", getElement("Register", "know")):
            elementBase.e_click(self.driver,getElement("Register", "know"))
            elementBase.e_send_key(self.driver, getElement("Register","company"), self.company)
            elementBase.e_tap(self.driver,590,260)
            elementBase.e_tap(self.driver,590,260)
            elementBase.e_tap(self.driver,590,260)
            elementBase.e_send_key(self.driver, getElement("Register","name"), self.name)
            elementBase.e_click(self.driver,getElement("Register", "line"))
            if self.position=="法人":
                elementBase.e_tap(self.driver,140,940)
            if self.position=="负责人":
                elementBase.e_tap(self.driver,140,1050)
            if self.position=="经理":
                elementBase.e_tap(self.driver,140,1150)
            if self.position=="其他":
                elementBase.e_tap(self.driver,140,1250)
            elementBase.e_click(self.driver,getElement("Register", "commit"))
            time.sleep(10)
            if elementBase.isElement(self.driver,"id",getElement("Home","close")):
                home = isElement(self.driver, "id", getElement("Home", "close"))
        else:
            pass
        return phone_error_text,toast_text,code_error_text,home
        # 58 886
