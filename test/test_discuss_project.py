# _*_ coding: utf-8 _*_
# @Time    : 2021/5/19 0019 22:36
# @Author  : Mr_li
# @FileName: test_discuss_project.py

from base.base_util import BaseUtil
# 数据驱动ddt导包
from ddt import ddt, data, unpack
# yaml文件导包
from ddt import file_data
from pageobject.discuss_project import DiscussProject


@ddt
class TestDiscussProject(BaseUtil):
    """洽谈项目--软装"""

    @file_data("E:\\A999\\yaml\\discuss_project.yaml")
    def test_action_item(self, **kwargs):
        username = kwargs.get('username')
        password = kwargs.get('password')
        value1 = kwargs.get('value1')
        value2 = kwargs.get('value2')
        value3 = kwargs.get('value3')
        value4 = kwargs.get('value4')
        value5 = kwargs.get('value5')

        action_item = DiscussProject(self.driver)
        action_item.test_discuss_project(username, password, value1, value2, value3, value4, value5)
