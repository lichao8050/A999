# _*_ coding: utf-8 _*_
# @time  : 2021/3/30 13:49
# @author:Mr_Li
# 执行并生成测试报告
import unittest
from time import strftime, localtime, time

from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover("./test", pattern='test_login1')  # 执行指定用例
    # path = os.path.dirname(os.path.abspath("test_add_customer.py"))
    # discover = unittest.defaultTestLoader.discover(path, pattern='test_*.py')
    now = strftime("%Y-%m-%M-%H_%M_%S", localtime(time()))
    filename = "E:\\A999\\report\\" + now + "test.html"
    fp = open(filename, "wb")
    runner = HTMLTestRunner(stream=fp, title="erp自动化测试报告", description="以下是测试详情")
    runner.run(suite)
    fp.close()
