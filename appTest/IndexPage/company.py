from appTest.IndexPage.IndexHome import homePage
from appTest.readData.elementData import getElement
from appTest.Element.elementBase import isElement
from appTest.Element import elementBase
import time


class company:
    def __init__(self, driver, flag=True):
        self.driver = driver
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

    def index_page(self):
        if isElement(self.driver, "id", getElement("Company", "company")):
            elementBase.e_click(self.driver, getElement("Company", "company"))
        if isElement(self.driver, "id", getElement("Company", "recommend")):
            elementBase.e_click(self.driver, getElement("Company", "recommend"))
        company_element = elementBase.e_wait_element2(self.driver, getElement("Company", "company_name"))
        if company_element != "":
            company_name = company_element[0].text
            company_element[0].click()
            time.sleep(5)
            company_detail = elementBase.e_text(self.driver, getElement("Company", "company_detail"))
        else:
            company_name, company_detail = "", "1"

        return company_name, company_detail

    def search(self):
        if isElement(self.driver, "id", getElement("Company", "company")):
            elementBase.e_click(self.driver, getElement("Company", "company"))
        if isElement(self.driver, "id", getElement("Company", "search")):
            elementBase.e_click(self.driver, getElement("Company", "search"))
        if isElement(self.driver, "id", getElement("Company", "search_edit")):
            elementBase.e_send_key(self.driver, getElement("Company", "search_edit"), "电梯")
        company_element = elementBase.e_wait_element2(self.driver, getElement("Company", "company_name"))
        if company_element != "":
            company_name = company_element[0].text
            company_element[0].click()
            time.sleep(5)
            company_detail = elementBase.e_text(self.driver, getElement("Company", "company_detail"))
        else:
            company_name, company_detail = "", "1"

        return company_name, company_detail

    def history(self):
        company_name, company_name_history = "", "1"
        if isElement(self.driver, "id", getElement("Company", "company")):
            elementBase.e_click(self.driver, getElement("Company", "company"))
        if isElement(self.driver, "id", getElement("Company", "history")):
            elementBase.e_click(self.driver, getElement("Company", "history"))
        if isElement(self.driver, "id", getElement("Company", "delete")):
            elementBase.e_click(self.driver, getElement("Company", "delete"))
            if isElement(self.driver, "id", getElement("Company", "btn_delete")):
                elementBase.e_click(self.driver, getElement("Company", "btn_delete"))
        if isElement(self.driver, "id", getElement("Company", "recommend")):
            elementBase.e_click(self.driver, getElement("Company", "recommend"))
        company_element = elementBase.e_wait_element2(self.driver, getElement("Company", "company_name"))
        if company_element != "":
            company_name = company_element[0].text
            company_element[0].click()
            time.sleep(5)
        if isElement(self.driver, "id", getElement("Company", "back")):
            elementBase.e_click(self.driver, getElement("Company", "back"))
        if isElement(self.driver, "id", getElement("Company", "history")):
            elementBase.e_click(self.driver, getElement("Company", "history"))
        company_element_history = elementBase.e_wait_element2(self.driver, getElement("Company", "company_name"))
        if company_element_history != "":
            company_name_history = company_element_history[0].text

        return company_name, company_name_history

    def collection(self):
        company_name, company_name_history = "", "1"
        if isElement(self.driver, "id", getElement("Company", "company")):
            elementBase.e_click(self.driver, getElement("Company", "company"))
        if isElement(self.driver, "id", getElement("Company", "collection")):
            elementBase.e_click(self.driver, getElement("Company", "collection"))
        if isElement(self.driver, "id", getElement("Company", "delete")):
            elementBase.e_click(self.driver, getElement("Company", "delete"))
            if isElement(self.driver, "id", getElement("Company", "btn_delete")):
                elementBase.e_click(self.driver, getElement("Company", "btn_delete"))
        if isElement(self.driver, "id", getElement("Company", "recommend")):
            elementBase.e_click(self.driver, getElement("Company", "recommend"))
        company_element = elementBase.e_wait_element2(self.driver, getElement("Company", "company_name"))
        if company_element != "":
            company_name = company_element[0].text
            company_element[0].click()
            time.sleep(5)
            if isElement(self.driver, "id", getElement("Company", "detail_collect")):
                elementBase.e_click(self.driver, getElement("Company", "detail_collect"))
                time.sleep(5)
        if isElement(self.driver, "id", getElement("Company", "back")):
            elementBase.e_click(self.driver, getElement("Company", "back"))
        if isElement(self.driver, "id", getElement("Company", "collection")):
            elementBase.e_click(self.driver, getElement("Company", "collection"))
        company_element_history = elementBase.e_wait_element2(self.driver, getElement("Company", "company_name"))
        if company_element_history != "":
            company_name_history = company_element_history[0].text

        return company_name, company_name_history
