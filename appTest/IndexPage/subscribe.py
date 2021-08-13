from appTest.IndexPage.IndexHome import homePage
from appTest.readData.elementData import getElement
from appTest.Element.elementBase import isElement
from appTest.Element import elementBase
import time


class subscribe:
    def __init__(self, driver, keyword, scope, model, email, flag=True):
        self.driver = driver
        self.keyword = keyword
        self.scope = scope
        self.model = model
        self.email = email
        self.flag = flag

    @classmethod
    def index(cls, driver):
        if isElement(driver, "id", getElement("Subscribe", "close")):
            elementBase.e_click(driver, getElement("Subscribe", "close"))
        if not isElement(driver, "id2", getElement("Home", "title")):
            text = homePage(driver).get_index_home()
            status = False
            return text, status
        else:
            text = ""
            status = True
            return text, status

    def add_sub(self):
        key_text = ""
        title = ""
        detail_title = "1"
        if isElement(self.driver, "id", getElement("Subscribe", "close")):
            elementBase.e_click(self.driver, getElement("Subscribe", "close"))
        if isElement(self.driver, "id", getElement("Subscribe", "custom")):
            elementBase.e_click(self.driver, getElement("Subscribe", "custom"))
            time.sleep(2)
        if isElement(self.driver, "id", getElement("Subscribe", "close")):
            elementBase.e_click(self.driver, getElement("Subscribe", "close"))
        if isElement(self.driver, "id", getElement("Subscribe", "add")):
            elementBase.e_click(self.driver, getElement("Subscribe", "add"))
        if isElement(self.driver, "id", getElement("Subscribe", "text")):
            elementBase.e_click(self.driver, getElement("Subscribe", "close"))
            subscribe.delete_sub(self.driver)
        if isElement(self.driver, "id", getElement("Subscribe", "add")):
            elementBase.e_click(self.driver, getElement("Subscribe", "add"))
        if isElement(self.driver, "id", getElement("Subscribe", "next")):
            for i in range(2):
                elementBase.e_click(self.driver, getElement("Subscribe", "next"))
        if isElement(self.driver, "id", getElement("Subscribe", "add_keyword")):
            elementBase.e_click(self.driver, getElement("Subscribe", "add_keyword"))
        values = self.keyword.split(",")
        for i in values:
            elementBase.e_send_key(self.driver, getElement("Subscribe", "input_keyword"), i)
            elementBase.e_click(self.driver, getElement("Subscribe", "increase"))
        time.sleep(5)
        if self.scope == "全文搜索":
            elementBase.e_click(self.driver, getElement("Subscribe", "full_text_search"))
        if self.scope == "标题搜索":
            elementBase.e_click(self.driver, getElement("Subscribe", "title_text_search"))
        element = elementBase.e_wait_element2(self.driver, getElement("Subscribe", "model"))
        if self.model == "模糊搜索" and element != "":
            element[1].click()
            time.sleep(1)
        if self.model == "精准搜索" and element != "":
            element[0].click()
            time.sleep(1)
        if self.model == "智能搜索" and element != "":
            element[-1].click()
            time.sleep(1)
        elementBase.e_click(self.driver, getElement("Subscribe", "keyword_save"))
        if self.flag == 0:
            elementBase.e_click(self.driver, getElement("Subscribe", "custom_status"))
        if isElement(self.driver, "id", getElement("Subscribe", "email")):
            elementBase.e_send_key(self.driver, getElement("Subscribe", "email"), self.email)
        elementBase.e_click(self.driver, getElement("Subscribe", "add_save"))
        elementBase.e_click(self.driver, getElement("Subscribe", "close"))
        time.sleep(5)
        key_element = elementBase.e_wait_element2(self.driver, getElement("Subscribe", "key"))
        if key_element != "":
            key_text = key_element[0].text
        if isElement(self.driver, "id2", getElement("Subscribe", "all")):
            all_element = elementBase.e_wait_element2(self.driver, getElement("Subscribe", "all"))
            all_element[0].click()
            time.sleep(5)
        if isElement(self.driver, "id2", getElement("Subscribe", "title")):
            title_element = elementBase.e_wait_element2(self.driver, getElement("Subscribe", "title"))
            title = title_element[0].text
            title_element[0].click()
            time.sleep(5)
        if isElement(self.driver, "id", getElement("Home", "detail_title")):
            detail_title = elementBase.e_text(self.driver, getElement("Home", "detail_title"))

        return key_text, title, detail_title

    @classmethod
    def delete_sub(cls, driver):
        delete_number = ""
        now_number = ""
        if isElement(driver, "id", getElement("Subscribe", "close")):
            elementBase.e_click(driver, getElement("Subscribe", "close"))
        if isElement(driver, "id", getElement("Subscribe", "custom")):
            elementBase.e_click(driver, getElement("Subscribe", "custom"))
        if isElement(driver, "id", getElement("Subscribe", "close")):
            elementBase.e_click(driver, getElement("Subscribe", "close"))
        if isElement(driver, "id2", getElement("Subscribe", "number")):
            number = elementBase.e_wait_element2(driver, getElement("Subscribe", "number"))
            if number != "":
                delete_number = number[0].text
        else:
            delete_number = "1"
        if isElement(driver, "id2", getElement("Subscribe", "delete")):
            delete_element = elementBase.e_wait_element2(driver, getElement("Subscribe", "delete"))
            delete_element[0].click()
        if isElement(driver, "id2", getElement("Subscribe", "btn_delete")):
            elementBase.e_click(driver, getElement("Subscribe", "btn_delete"))
            time.sleep(3)
        if isElement(driver, "id2", getElement("Subscribe", "number")):
            number = elementBase.e_wait_element2(driver, getElement("Subscribe", "number"))
            if number != "":
                now_number = number[0].text
        if delete_number != now_number:
            return True
        else:
            return False

    def add_sub_nzj(self, exclude):
        key_text = ""
        title = ""
        detail_title = "1"
        if isElement(self.driver, "id", getElement("Subscribe", "close")):
            elementBase.e_click(self.driver, getElement("Subscribe", "close"))
        if isElement(self.driver, "id", getElement("Subscribe", "custom")):
            elementBase.e_click(self.driver, getElement("Subscribe", "custom"))
            time.sleep(2)
        if isElement(self.driver, "id", getElement("Subscribe", "close")):
            elementBase.e_click(self.driver, getElement("Subscribe", "close"))
        if isElement(self.driver, "id", getElement("Subscribe", "nzj")):
            elementBase.e_click(self.driver, getElement("Subscribe", "nzj"))
        if isElement(self.driver, "id", getElement("Subscribe", "add")):
            elementBase.e_click(self.driver, getElement("Subscribe", "add"))
        if isElement(self.driver, "id", getElement("Subscribe", "text")):
            elementBase.e_click(self.driver, getElement("Subscribe", "close"))
            subscribe.delete_sub(self.driver)
        if isElement(self.driver, "id", getElement("Subscribe", "add")):
            elementBase.e_click(self.driver, getElement("Subscribe", "add"))
        if isElement(self.driver, "id", getElement("Subscribe", "next")):
            for i in range(2):
                elementBase.e_click(self.driver, getElement("Subscribe", "next"))
        if isElement(self.driver, "id", getElement("Subscribe", "add_keyword")):
            elementBase.e_click(self.driver, getElement("Subscribe", "add_keyword"))
        values = self.keyword.split(",")
        for i in values:
            elementBase.e_send_key(self.driver, getElement("Subscribe", "input_keyword"), i)
            elementBase.e_click(self.driver, getElement("Subscribe", "increase"))
        time.sleep(5)
        if self.scope == "全文搜索":
            elementBase.e_click(self.driver, getElement("Subscribe", "full_text_search"))
        if self.scope == "标题搜索":
            elementBase.e_click(self.driver, getElement("Subscribe", "title_text_search"))
        element = elementBase.e_wait_element2(self.driver, getElement("Subscribe", "model"))
        if self.model == "模糊搜索" and element != "":
            element[1].click()
            time.sleep(1)
        if self.model == "精准搜索" and element != "":
            element[0].click()
            time.sleep(1)
        if self.model == "智能搜索" and element != "":
            element[-1].click()
            time.sleep(1)
        elementBase.e_click(self.driver, getElement("Subscribe", "keyword_save"))
        if exclude != "":
            elementBase.e_click(self.driver, getElement("Subscribe", "exclude"))
            values = exclude.split(",")
            for i in values:
                elementBase.e_send_key(self.driver, getElement("Subscribe", "input_keyword"), i)
                elementBase.e_click(self.driver, getElement("Subscribe", "increase"))
            elementBase.e_click(self.driver, getElement("Subscribe", "keyword_save"))
        elementBase.e_click(self.driver, getElement("Subscribe", "custom_status"))
        elementBase.e_click(self.driver, getElement("Subscribe", "custom_status"))
        if self.flag == 0:
            elementBase.e_click(self.driver, getElement("Subscribe", "custom_status"))
        if isElement(self.driver, "id", getElement("Subscribe", "email")):
            elementBase.e_send_key(self.driver, getElement("Subscribe", "email"), self.email)
        elementBase.e_click(self.driver, getElement("Subscribe", "add_save"))
        elementBase.e_click(self.driver, getElement("Subscribe", "close"))
        time.sleep(5)
        # key_element = elementBase.e_wait_element2(self.driver, getElement("Subscribe", "key"))
        # if key_element != "":
        #     key_text = key_element[0].text
        if isElement(self.driver, "id2", getElement("Subscribe", "all")):
            all_element = elementBase.e_wait_element2(self.driver, getElement("Subscribe", "all"))
            all_element[0].click()
            time.sleep(5)
        if isElement(self.driver, "id2", getElement("Subscribe", "title_name")):
            title_element = elementBase.e_wait_element2(self.driver, getElement("Subscribe", "title_name"))
            title = title_element[0].text
            title_element[0].click()
            time.sleep(5)
        if isElement(self.driver, "id", getElement("Subscribe", "title_name")):
            detail_title = elementBase.e_text(self.driver, getElement("Subscribe", "title_name"))

        return title, detail_title
