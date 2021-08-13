import pymysql
import time

class db:
    def __init__(self, phone):
        self.phone = phone

    def get_code(self):
        time.sleep(8)
        # 打开数据库连接
        db = pymysql.connect(host="192.168.2.170", port=3306, user="root", password="pwdformysql0922", db="bxkc")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # sql = "desc b2c_user_login_info"
        sql = "select code from bxkc_identifycode where phone = %s " % self.phone
        # 使用 execute()  方法执行 SQL 查询
        cursor.execute(sql)
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchall()

        return data[-1][0]

# b=db("16551000556")
# c=b.get_code()
# print(c)

