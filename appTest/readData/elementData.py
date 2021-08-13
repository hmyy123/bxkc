import configparser
import os

def getElement(sections,host):
    Dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(Dir_path,"Element","config.ini")
    # print(file_path)
    cf = configparser.ConfigParser()
    cf.read(file_path)
    # secs = cf.sections()
    # print(secs)
    # options = cf.options("Login")  # 获取某个section名为Mysql-Database所对应的键
    # print(options)
    # items = cf.items("Login")  # 获取section名为Mysql-Database所对应的全部键值对
    # print(items)
    host = cf.get(sections, host)  # 获取[Mysql-Database]中host对应的值
    return host

# a=getElement("Login","agree")
# print(a)

