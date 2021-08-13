from appTest.readData.elementData import getElement
from appTest.Element.elementBase import isElement
from appTest.Element import elementBase
from appTest.Database.db import db


class forget:
    def __init__(self, driver, phone, code, password):
        self.driver = driver
        self.phone = phone
        self.code = code
        self.password = password

    def modify_pwd(self):
        phone_error_text=""
        password_error_text=""
        code_error=""
        text=""
        if isElement(self.driver, "id", getElement("Login", "agree")):
            elementBase.e_click(self.driver, getElement("Login", "agree"))

        for i in range(4):
            if isElement(self.driver, "id", getElement("Login", "allow")):
                elementBase.e_click(self.driver, getElement("Login", "allow"))
        elementBase.e_click(self.driver, getElement("Login", "login"))
        elementBase.e_click(self.driver, getElement("Login", "forget"))
        elementBase.e_send_key(self.driver, getElement("Forget", "phone"), self.phone)
        elementBase.e_click(self.driver,getElement("Forget", "getcode"))
        if self.code ==1111 and self.phone is not None:
            self.code = db(self.phone).get_code()
        elementBase.e_send_key(self.driver, getElement("Forget", "code"), self.code)
        elementBase.e_send_key(self.driver, getElement("Forget", "password"), self.password)
        elementBase.e_click(self.driver, getElement("Forget", "commit"))
        try:
            if isElement(self.driver, "id", getElement("Forget", "password_error")):
                password_error_text = elementBase.e_text(self.driver, getElement("Forget", "password_error"))
                return phone_error_text, password_error_text, code_error, text
            if isElement(self.driver, "id", getElement("Forget", "phone_error")):
                phone_error_text = elementBase.e_text(self.driver, getElement("Forget", "phone_error"))
                return phone_error_text, password_error_text, code_error, text
            if isElement(self.driver, "id", getElement("Forget", "code_error")):
                code_error = elementBase.e_text(self.driver, getElement("Forget", "code_error"))
                return phone_error_text, password_error_text, code_error, text
            if isElement(self.driver, "id", getElement("Login", "login_button")):
                text = elementBase.e_text(self.driver, getElement("Login", "login_button"))
            else:
                pass
        except:
            print("找不到元素")
        return phone_error_text, password_error_text, code_error, text
