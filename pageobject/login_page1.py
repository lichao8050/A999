# _*_ coding: utf-8 _*_
# @Time    : 2021/5/12 0012 23:03
# @Author  : Mr_Li
# @FileName: login_page1.py
"""1页面元素2页面动作"""
from time import sleep
from base.base_page import BasePage
from base.base_util import logger
from pageobject.system_dictionary_list import matrix


class LoginPage1(BasePage):

    def login_erp(self, username, password, b, msg):
        logger.info('输入用户名')
        self.send_ks(matrix.use_loc, username)
        logger.info('输入登录密码')
        self.send_ks(matrix.pas_loc, password)
        logger.info('点击登录按钮')
        self.click(matrix.sub_loc)
        sleep(1)
        self.equal(self.gt_text(matrix.login_success), b, msg)
        self.take_screenshot()
