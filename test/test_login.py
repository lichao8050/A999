# _*_ coding: utf-8 _*_
# @Time    : 2021/5/12 0012 23:11
# @Author  : Mr_Li
# @FileName: test_login.py
from base.base_util import BaseUtil
from pageobject.login_page import LoginPage
# 数据驱动ddt导包
from ddt import ddt, data, unpack
# yaml文件导包
from ddt import file_data


@ddt
class TestLogin(BaseUtil):

    @file_data("E:\\A999\\yaml\\test_login.yaml")
    def test_login(self, **kwargs):
        username = kwargs.get('username')
        password = kwargs.get('password')

        login = LoginPage(self.driver)
        login.login_erp(username, password)

