# _*_ coding: utf-8 _*_
# @Time    : 2021/8/30 10:54
# @Author  : Mr_Li
# @FileName: other_file.py
import unittest, os

# 1.执行需要的用例，并生成HTML的自动化测试报告
# # suite = unittest.defaultTestLoader.discover()
# # suite = os.path.dirname(os.path.dirname(os.path.abspath("test_add_customer.py")))
# # # 2.生成报告HTML文件,报告文件一般在report文件夹下
# # # a，在python根目录下新建report文件夹. b，生成文件：
# # # 获取当前时间
# # now = strftime("%Y-%m-%M-%H_%M_%S", localtime(time()))
# # # 文件名
# # filename = "E:\\999\\report\\"+now+"test.html"
# # # 以二进制的方式打开文件并写入结果
# # fp = open(filename,"wb")
# # # 3.导入HTMLTestRunenr的包,生成一个HTMLTestRunenr运行器对象
# # # （必须下载一个HTMLTestRunenr.py的文件并放在python的lib目录下）
# # runner = HTMLTestRunner(stream=fp,title="erp自动化测试报告",description="以下是测试详情")
# # # 通过运行器运行测试用例
# # runner.run(suite)
# # fp.close()'''

# # 当前文件的绝对路径,包括文件名
# print(__file__)
# # 当前文件的系统绝对路径,往往用于添加到环境变量BASE_DIR
# print(os.path.abspath(__file__))
# # 当前文件所在的目录
# print(os.path.dirname(__file__))
# # 文件所在目录的上一级目录
# print(os.path.dirname(os.path.dirname(__file__)))
# # 当前文件所在的目录
# print(os.path.dirname(os.path.abspath(__file__)))
# path = os.path.dirname(os.path.abspath("test_add_customer.py"))
# print(path)

# get_path = os.path.dirname(os.path.abspath('./log'))
# __path = os.path.join(os.path.dirname(get_path),"log")
print(50 * '-')
