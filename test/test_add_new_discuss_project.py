# _*_ coding: utf-8 _*_
# @Time     : 2021/10/18 12:15
# @Author   : Mr_Li
# @FileName : test_add_new_discuss_project.py
from base.base_util import BaseUtil
# 数据驱动ddt导包
from ddt import ddt, data, unpack
# yaml文件导包
from ddt import file_data

from pageobject.add_new_discuss_project import DiscussProject


@ddt
class TestDiscussProject(BaseUtil):
    """新增洽谈项目"""

    @file_data("E:\\A999\\yaml\\add_new_discuss_project.yaml")
    def test_add_new_discuss_project(self, **kwargs):
        username = kwargs.get('username')
        password = kwargs.get('password')
        value1 = kwargs.get('value1')
        value2 = kwargs.get('value2')
        value3 = kwargs.get('value3')
        login = DiscussProject(self.driver)
        login.discuss_project(username, password, value1, value2, value3)
