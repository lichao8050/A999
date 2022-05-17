# @time    : 2021/3/30 12:53
# @author  :Mr_Li
# _*_coding:utf-8_*_
# @FileName: base_until.py
import unittest
from selenium import webdriver
import selenium.webdriver.support.wait
from log import Log

logger = Log().Logger
logger.info(50 * '-')
logger.info('---开始执行测试---')


class BaseUtil(unittest.TestCase):

    def setUp(self):
        logger.info('全局浏览器')
        global driver
        self.driver = webdriver.Chrome()
        driver = self.driver
        self.driver.implicitly_wait(10)
        logger.info('最大化浏览器')
        self.driver.maximize_window()
        logger.info('打开网页')
        # self.driver.get("http://192.168.1.165:8001/")
        self.driver.get("http://kbs.matrixdesign.cn/")
        # self.driver.get("https://erp.matrixdesign.cn/")
        # self.driver.get("http://miao.matrixdesign.cn//")

    def tearDown(self):
        pass
        # logger.info('---执行完毕，关闭浏览器---')
        # self.driver.quit()
        # logger.info(50 * '-')
