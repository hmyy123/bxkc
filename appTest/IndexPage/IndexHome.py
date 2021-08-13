import time
from appTest.readData.elementData import getElement
from appTest.Element.elementBase import isElement
from appTest.Element import elementBase


class homePage:
    def __init__(self, driver):
        self.driver = driver

    def get_index_home(self):
        value = ""
        if isElement(self.driver, "id", getElement("Login", "agree")):
            elementBase.e_click(self.driver, getElement("Login", "agree"))
        for i in range(4):
            elementBase.e_click(self.driver, getElement("Login", "allow"))
        if isElement(self.driver, "id", getElement("Login", "login")):
            elementBase.e_click(self.driver, getElement("Login", "login"))
        elementBase.e_send_key(self.driver, getElement("Login", "phone"), getElement("User", "supreme_user"))
        elementBase.e_send_key(self.driver, getElement("Login", "password"), getElement("User", "password"))
        elementBase.e_click(self.driver, getElement("Login", "login_button"))
        time.sleep(10)
        if isElement(self.driver, "id", getElement("Home", "close")):
            elementBase.e_click(self.driver, getElement("Home", "close"))
        if isElement(self.driver, "id", getElement("Home", "first_search")):
            elementBase.e_click(self.driver, getElement("Home", "first_search"))
        if isElement(self.driver, "id2", getElement("Home", "edit_search")):
            element = elementBase.e_wait_element2(self.driver, getElement("Home", "edit_search"))
            # print(element)
            if element != "":
                try:
                    element[0].send_keys("电梯")
                    element[1].send_keys("电梯")
                except:
                    pass
            elementBase.e_click(self.driver, getElement("Home", "txt_search"))
        if isElement(self.driver, "id", getElement("Home", "txt_type")):
            elementBase.e_click(self.driver, getElement("Home", "txt_type"))
        if isElement(self.driver, "id", getElement("Home", "close")):
            elementBase.e_click(self.driver, getElement("Home", "close"))
        if isElement(self.driver, "id", getElement("Home", "confirm")):
            elementBase.e_click(self.driver, getElement("Home", "confirm"))
        if isElement(self.driver, "id", getElement("Home", "back")):
            elementBase.e_click(self.driver, getElement("Home", "back"))
        if isElement(self.driver, "id", getElement("Home", "home")):
            text = elementBase.e_wait_element(self.driver, getElement("Home", "home"))
            if text != "":
                value = text.text
        return value
        # print(a)

    def get_index_page(self):
        title = "1"
        detail_title = ""
        if isElement(self.driver, "id2", getElement("Home", "title")):
            element = elementBase.e_wait_element2(self.driver, getElement("Home", "title"))
            if element != "":
                title = element[0].text
                element[0].click()
                time.sleep(8)
        if isElement(self.driver, "id", getElement("Home", "detail_title")):
            detail_title = elementBase.e_text(self.driver, getElement("Home", "detail_title"))
        if isElement(self.driver, "id", getElement("Home", "back")):
            elementBase.e_click(self.driver, getElement("Home", "back"))
        return title, detail_title

    def search_project(self):
        title = ""
        if isElement(self.driver, "id2", getElement("Home", "cqy")):
            element = elementBase.e_wait_element2(self.driver, getElement("Home", "cqy"))
            if element != "":
                element[0].click()
        if isElement(self.driver, "id", getElement("Home", "index_search")):
            elementBase.e_click(self.driver, getElement("Home", "index_search"))
        if isElement(self.driver, "id", getElement("Home", "edit_search")):
            # element = elementBase.e_wait_element2(self.driver,getElement("Home", "edit_search"))
            # element[1].send_keys("电梯")
            elementBase.e_send_key(self.driver, getElement("Home", "edit_search"), "电梯")
            if isElement(self.driver, "id", getElement("Home", "close")):
                elementBase.e_click(self.driver, getElement("Home", "close"))
            elementBase.e_click(self.driver, getElement("Home", "txt_search"))
            time.sleep(5)
        if isElement(self.driver, "id", getElement("Home", "close")):
            elementBase.e_click(self.driver, getElement("Home", "close"))
        if isElement(self.driver, "id2", getElement("Home", "title")):
            element = elementBase.e_wait_element2(self.driver, getElement("Home", "title"))
            if element != "":
                title = element[0].text
        if isElement(self.driver, "id", getElement("Home", "back")):
            elementBase.e_click(self.driver, getElement("Home", "back"))
        return title

    def default(self, name, title_name, detail_title_name):
        title, detail_title = "1", ""
        if isElement(self.driver, "id", getElement("Home", "close")):
            elementBase.e_click(self.driver, getElement("Home", "close"))
        if isElement(self.driver, "id", getElement("Home", name)):
            elementBase.e_click(self.driver, getElement("Home", name))
            time.sleep(5)
        if isElement(self.driver, "id2", getElement("Home", title_name)):
            element = elementBase.e_wait_element2(self.driver, getElement("Home", title_name))
            if element != "":
                title = element[0].text
                element[0].click()
                time.sleep(8)
        if isElement(self.driver, "id", getElement("Home", "close")):
            elementBase.e_click(self.driver, getElement("Home", "close"))
        if isElement(self.driver, "id", getElement("Home", detail_title_name)):
            detail_title = elementBase.e_text(self.driver, getElement("Home", detail_title_name))
        if isElement(self.driver, "id", getElement("Home", "back")):
            elementBase.e_click(self.driver, getElement("Home", "back"))
        if isElement(self.driver, "id", getElement("Home", "back")):
            elementBase.e_click(self.driver, getElement("Home", "back"))
        return title, detail_title

    def ctb(self):
        # 查招标
        title, detail_title = self.default("ctb", "title", "detail_title")
        return title, detail_title

    def czb(self):
        # 查中标
        title, detail_title = self.default("czb", "title", "detail_title")
        return title, detail_title

    def cnzj(self):
        # 查拟在建
        title, detail_title = self.default("cnzj", "name", "name")
        return title, detail_title

    def sjdc(self):
        # 数据导出
        text = ""
        if isElement(self.driver, "id", getElement("Home", "close")):
            elementBase.e_click(self.driver, getElement("Home", "close"))
        if isElement(self.driver, "id", getElement("Home", "sjdc")):
            elementBase.e_click(self.driver, getElement("Home", "sjdc"))
        if isElement(self.driver, "id", getElement("Home", "sure")):
            elementBase.e_click(self.driver, getElement("Home", "sure"))
            time.sleep(2)
        if isElement(self.driver, "id", getElement("Home", "preview")):
            text = elementBase.e_text(self.driver, getElement("Home", "preview"))
        if isElement(self.driver, "id", getElement("Home", "back")):
            elementBase.e_click(self.driver, getElement("Home", "back"))
        if isElement(self.driver, "id", getElement("Home", "back")):
            elementBase.e_click(self.driver, getElement("Home", "back"))
        return text

    def bsdx(self):
        # 标书代写
        text = ""
        if isElement(self.driver, "id", getElement("Home", "close")):
            elementBase.e_click(self.driver, getElement("Home", "close"))
        if isElement(self.driver, "id", getElement("Home", "bsdx")):
            elementBase.e_click(self.driver, getElement("Home", "bsdx"))
        if isElement(self.driver, "id", getElement("Home", "txt_title")):
            text = elementBase.e_text(self.driver, getElement("Home", "txt_title"))
        if isElement(self.driver, "id", getElement("Home", "back")):
            elementBase.e_click(self.driver, getElement("Home", "back"))
        return text

    def qybg(self):
        # 企业报告
        text = ""
        text2 = ""
        if isElement(self.driver, "id", getElement("Home", "close")):
            elementBase.e_click(self.driver, getElement("Home", "close"))
        if isElement(self.driver, "id", getElement("Home", "qybg")):
            elementBase.e_click(self.driver, getElement("Home", "qybg"))
        if isElement(self.driver, "id2", getElement("Home", "tab")):
            name = elementBase.e_wait_element2(self.driver, getElement("Home", "tab"))
            element = elementBase.e_wait_element2(self.driver, getElement("Home", "download_report"))
            if element != "":
                text = element[0].text
                name[1].click()
            element2 = elementBase.e_wait_element2(self.driver, getElement("Home", "download_report"))
            if element2 != "":
                text2 = element2[0].text
        if isElement(self.driver, "id", getElement("Home", "back")):
            elementBase.e_click(self.driver, getElement("Home", "back"))
        return text, text2

    def hybg(self):
        # 行业报告
        text = ""
        if isElement(self.driver, "id", getElement("Home", "close")):
            elementBase.e_click(self.driver, getElement("Home", "close"))
        if isElement(self.driver, "id", getElement("Home", "hybg")):
            elementBase.e_click(self.driver, getElement("Home", "hybg"))
        if isElement(self.driver, "id2", getElement("Home", "download_report")):
            element = elementBase.e_wait_element2(self.driver, getElement("Home", "download_report"))
            if element != "":
                text = element[0].text
        if isElement(self.driver, "id", getElement("Home", "back")):
            elementBase.e_click(self.driver, getElement("Home", "back"))
        return text

    def gnjs(self):
        # 功能介绍
        text = ""
        if isElement(self.driver, "id", getElement("Home", "close")):
            elementBase.e_click(self.driver, getElement("Home", "close"))
        if isElement(self.driver, "id", getElement("Home", "gnjs")):
            elementBase.e_click(self.driver, getElement("Home", "gnjs"))
        if isElement(self.driver, "id2", getElement("Home", "content")):
            element = elementBase.e_wait_element2(self.driver, getElement("Home", "content"))
            if element != "":
                text = element[0].text
        if isElement(self.driver, "id", getElement("Home", "back")):
            elementBase.e_click(self.driver, getElement("Home", "back"))
        return text

    def gdgn(self):
        # 更多功能
        text = ""
        if isElement(self.driver, "id", getElement("Home", "close")):
            elementBase.e_click(self.driver, getElement("Home", "close"))
        if isElement(self.driver, "id", getElement("Home", "more")):
            elementBase.e_click(self.driver, getElement("Home", "more"))
        if isElement(self.driver, "id2", getElement("Home", "name")):
            element = elementBase.e_wait_element2(self.driver, getElement("Home", "name"))
            if element != "":
                text = element[0].text
        if isElement(self.driver, "id", getElement("Home", "back")):
            elementBase.e_click(self.driver, getElement("Home", "back"))
        return text

    def qyxxk(self):
        # 企业信息库
        text = ""
        if isElement(self.driver, "id", getElement("Home", "close")):
            elementBase.e_click(self.driver, getElement("Home", "close"))
        if isElement(self.driver, "id", getElement("Home", "qyxxk")):
            elementBase.e_click(self.driver, getElement("Home", "qyxxk"))
        if isElement(self.driver, "id2", getElement("Home", "company_phone")):
            element = elementBase.e_wait_element2(self.driver, getElement("Home", "company_phone"))
            if element != "":
                text = element[0].text
        if isElement(self.driver, "id", getElement("Home", "back")):
            elementBase.e_click(self.driver, getElement("Home", "back"))
        return text

    def cqy(self):
        # 查企业
        title = ""
        if isElement(self.driver, "id", getElement("Home", "close")):
            elementBase.e_click(self.driver, getElement("Home", "close"))
        if isElement(self.driver, "id2", getElement("Home", "cqy")):
            element = elementBase.e_wait_element2(self.driver, getElement("Home", "cqy"))
            if element != "":
                element[1].click()
        if isElement(self.driver, "id", getElement("Home", "index_search")):
            elementBase.e_click(self.driver, getElement("Home", "index_search"))
        if isElement(self.driver, "id", getElement("Home", "edit_search")):
            # element = elementBase.e_wait_element2(self.driver,getElement("Home", "edit_search"))
            # element[1].send_keys("电梯")
            elementBase.e_send_key(self.driver, getElement("Home", "edit_search"), "中国能源")
            if isElement(self.driver, "id", getElement("Home", "close")):
                elementBase.e_click(self.driver, getElement("Home", "close"))
            elementBase.e_click(self.driver, getElement("Home", "txt_search"))
            time.sleep(5)
        if isElement(self.driver, "id", getElement("Home", "btn_kown")):
            elementBase.e_click(self.driver, getElement("Home", "btn_kown"))
        if isElement(self.driver, "id", getElement("Home", "close")):
            elementBase.e_click(self.driver, getElement("Home", "close"))
        if isElement(self.driver, "id2", getElement("Home", "name")):
            element = elementBase.e_wait_element2(self.driver, getElement("Home", "name"))
            if element != "":
                title = element[0].text
        if isElement(self.driver, "id", getElement("Home", "cancel")):
            elementBase.e_click(self.driver, getElement("Home", "cancel"))
        if isElement(self.driver, "id", getElement("Home", "back")):
            elementBase.e_click(self.driver, getElement("Home", "back"))
        return title

    def cqybg(self):
        # 查企业报告
        title = ""
        title2 = ""
        if isElement(self.driver, "id", getElement("Home", "close")):
            elementBase.e_click(self.driver, getElement("Home", "close"))
        if isElement(self.driver, "id2", getElement("Home", "cqy")):
            element = elementBase.e_wait_element2(self.driver, getElement("Home", "cqy"))
            if element != "":
                element[2].click()
        if isElement(self.driver, "id", getElement("Home", "index_search")):
            elementBase.e_click(self.driver, getElement("Home", "index_search"))
        if isElement(self.driver, "id", getElement("Home", "edit_search")):
            elementBase.e_send_key(self.driver, getElement("Home", "edit_search"), "中国能源")
            if isElement(self.driver, "id", getElement("Home", "close")):
                elementBase.e_click(self.driver, getElement("Home", "close"))
            elementBase.e_click(self.driver, getElement("Home", "txt_search"))
            time.sleep(5)
        if isElement(self.driver, "id2", getElement("Home", "tab")):
            name = elementBase.e_wait_element2(self.driver, getElement("Home", "tab"))
            element = elementBase.e_wait_element2(self.driver, getElement("Home", "qy_title"))
            if name != "" and element != "":
                title = element[0].text
                name[1].click()
                element2 = elementBase.e_wait_element2(self.driver, getElement("Home", "qy_title"))
                if element2 != "":
                    title2 = element2[0].text
        if isElement(self.driver, "id", getElement("Home", "back")):
            elementBase.e_click(self.driver, getElement("Home", "back"))
        if isElement(self.driver, "id", getElement("Home", "close")):
            elementBase.e_click(self.driver, getElement("Home", "close"))
        if isElement(self.driver, "id", getElement("Home", "back")):
            elementBase.e_click(self.driver, getElement("Home", "back"))
        return title, title2

    def chybg(self):
        # 查行业报告
        title = ""
        if isElement(self.driver, "id", getElement("Home", "close")):
            elementBase.e_click(self.driver, getElement("Home", "close"))
        if isElement(self.driver, "id2", getElement("Home", "cqy")):
            element = elementBase.e_wait_element2(self.driver, getElement("Home", "cqy"))
            if element != "":
                element[3].click()
        if isElement(self.driver, "id", getElement("Home", "index_search")):
            elementBase.e_click(self.driver, getElement("Home", "index_search"))
        if isElement(self.driver, "id", getElement("Home", "edit_search")):
            elementBase.e_send_key(self.driver, getElement("Home", "edit_search"), "服务")
            if isElement(self.driver, "id", getElement("Home", "close")):
                elementBase.e_click(self.driver, getElement("Home", "close"))
            elementBase.e_click(self.driver, getElement("Home", "txt_search"))
            time.sleep(5)
        if isElement(self.driver, "id2", getElement("Home", "qy_title")):
            element = elementBase.e_wait_element2(self.driver, getElement("Home", "qy_title"))
            if element != "":
                title = element[0].text
        if isElement(self.driver, "id", getElement("Home", "back")):
            elementBase.e_click(self.driver, getElement("Home", "back"))
        if isElement(self.driver, "id", getElement("Home", "close")):
            elementBase.e_click(self.driver, getElement("Home", "close"))
        if isElement(self.driver, "id", getElement("Home", "back")):
            elementBase.e_click(self.driver, getElement("Home", "back"))
        return title
