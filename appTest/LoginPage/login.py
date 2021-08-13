from selenium.webdriver.support.wait import WebDriverWait
from appTest.readData.elementData import getElement
from appTest.Element.elementBase import isElement
from appTest.Element import elementBase
import time


# 游客登陆
def visitor_login(driver):
    value=""
    if isElement(driver,"id",getElement("Login", "agree")):
        elementBase.e_click(driver,getElement("Login", "agree"))

    for i in range(4):
        if isElement(driver, "id", getElement("Login", "allow")):
            elementBase.e_click(driver, getElement("Login", "allow"))

    page = elementBase.isElement(driver, "id", getElement("Login", "page"))

    elementBase.e_click(driver, getElement("Login", "login"))

    element = elementBase.e_wait_element(driver, getElement("Login", "visitor"))
    if element != "":
        element.click()

    if isElement(driver,"id",getElement("Home","close")):
        elementBase.e_click(driver,getElement("Home","close"))
    text = elementBase.e_wait_element(driver, getElement("Home", "home"))
    if text != "":
        value = text.text
    # print(value)
    return page,value


def normal_login(driver, username, password):
    phone_error_text = ""
    password_error_text = ""
    home=""
    if isElement(driver,"id",getElement("Login", "agree")):
        elementBase.e_click(driver,getElement("Login", "agree"))
    for i in range(4):
        elementBase.e_click(driver, getElement("Login", "allow"))

    elementBase.e_click(driver, getElement("Login", "login"))
    elementBase.e_send_key(driver, getElement("Login", "phone"), username)
    elementBase.e_send_key(driver, getElement("Login", "password"), password)
    elementBase.e_click(driver, getElement("Login", "login_button"))
    try:
        if isElement(driver, "id", getElement("Login", "password_error2")):
            password_error_text = elementBase.e_text(driver, getElement("Login", "password_error2"))
            return phone_error_text, password_error_text, home
        if isElement(driver, "id", getElement("Login", "phone_error")):
            phone_error_text = elementBase.e_text(driver, getElement("Login", "phone_error"))
            return phone_error_text, password_error_text, home
        if isElement(driver, "id", getElement("Login", "password_error")):
            password_error_text = elementBase.e_text(driver, getElement("Login", "password_error"))
            return phone_error_text, password_error_text, home
        if isElement(driver, "id", getElement("Home", "close")):
            home=isElement(driver, "id", getElement("Home", "close"))
        else:
            pass
    except:
        print("找不到元素")
    return phone_error_text, password_error_text, home
