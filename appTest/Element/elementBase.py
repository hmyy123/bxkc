from selenium.webdriver.support.wait import WebDriverWait
import time


def e_wait_element(driver, c):
    try:
        element = WebDriverWait(driver, 3, 1).until(lambda x: x.find_element_by_id(c))
        return element
    except:
        return ""

def e_wait_element2(driver, c):
    try:
        element = WebDriverWait(driver, 3, 1).until(lambda x: x.find_elements_by_id(c))
        return element
    except:
        return ""



def e_wait_element_xpath(driver, c):
    try:
        element = WebDriverWait(driver, 3, 1).until(lambda x: x.find_element_by_xpath(c))
        return element
    except:
        return ""

def e_text(driver, c):
    try:
        text = driver.find_element_by_id(c).text
        return text
    except:
        return ""

def e_text_xpath(driver, c):
    try:
        text = driver.find_element_by_xpath(c).text
        return text
    except:
        return ""


def e_send_key(driver, c, value):
    try:
        driver.find_element_by_id(c).clear()
        time.sleep(1)
        driver.find_element_by_id(c).send_keys(value)
        time.sleep(1)
    except:
        return ""


def e_click(driver, c):
    try:
        driver.find_element_by_id(c).click()
        time.sleep(1)
    except:
        return ""


def e_tap(driver, x, y):
    driver.tap([(x, y)])
    time.sleep(1)


def isElement(driver, identifyBy, c):
    flag = None
    try:
        if identifyBy == "id":
            WebDriverWait(driver, 2, 0.5).until(lambda x: x.find_element_by_id(c))
        elif identifyBy == "id2":
            WebDriverWait(driver, 2, 0.5).until(lambda x: x.find_elements_by_id(c))
        elif identifyBy == "xpath":
            WebDriverWait(driver, 2, 0.5).until(lambda x: x.find_element_by_xpath(c))
        elif identifyBy == "class":
            driver.find_element_by_class_name(c)
        elif identifyBy == "link text":
            driver.find_element_by_link_text(c)
        # elif identifyBy == "partial link text":
        #     self.driver.find_element_by_partial_link_text(c)
        elif identifyBy == "name":
            driver.find_element_by_name(c)
        elif identifyBy == "tag name":
            driver.find_element_by_tag_name(c)
        elif identifyBy == "css selector":
            driver.find_element_by_css_selector(c)
        flag = True
    except:
        flag = False
    finally:
        return flag
