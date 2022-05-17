# _*_ coding: utf-8 _*_
# @Time    : 2021/5/19 0019 22:36
# @Author  : Mr_Li
# @FileName: test_programme_list_items.py
from base.base_util import BaseUtil

# 数据驱动ddt导包
from ddt import ddt, data, unpack
# yaml文件导包
from ddt import file_data

from pageobject.programme_list_items import ProgrammeListItems


@ddt
class TestProgrammeListItems(BaseUtil):
    """项目流程--方案清单项目"""

    @file_data("E:\\A999\\yaml\\action_item_hard.yaml")
    def test_action_item(self, **kwargs):
        username = kwargs.get('username')
        password = kwargs.get('password')
        value1 = kwargs.get('value1')
        value2 = kwargs.get('value2')
        value3 = kwargs.get('value3')
        value4 = kwargs.get('value4')
        value5 = kwargs.get('value5')
        value6 = kwargs.get('value6')
        value7 = kwargs.get('value7')

        action_item = ProgrammeListItems(self.driver)
        action_item.test_programme_list_items(username, password, value1, value2, value3, value4, value5, value6,
                                              value7)
