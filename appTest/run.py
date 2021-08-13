from BeautifulReport import BeautifulReport
import unittest, os, time

# 用例存放位置
test_case_path = os.path.dirname(__file__)

# 测试报告存放位置
log_path = os.path.join(test_case_path, "Report")
# print(log_path)
ti = time.strftime("%Y-%m-%d %H_%M_%S")
# 测试报告名称
filename = ti + "Report.html"
# 用例名称
description = '标讯登录'
# 需要执行哪些用例，如果目录下的全部，可以改为"*.py"，如果是部分带test后缀的，可以改为"*test.py"
pattern = "test_subscribe.py"

if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover(test_case_path, pattern=pattern)
    result = BeautifulReport(test_suite)
    result.report(filename=filename, description=description, log_path=log_path,report_dir=log_path)
