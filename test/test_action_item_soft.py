# _*_ coding: utf-8 _*_
# @Time    : 2021/5/19 0019 22:36
# @Author  : Mr_Li
# @FileName: test_action_item_hard.py
from base.base_util import BaseUtil
from pageobject.action_item_soft import ActionItemSoft
# 数据驱动ddt导包
from ddt import ddt, data, unpack
# yaml文件导包
from ddt import file_data


@ddt
class TestActionItemSoft(BaseUtil):
    """执行项目--软装"""

    @file_data("E:\\A999\\yaml\\action_item_soft.yaml")
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
        value8 = kwargs.get('value8')
        value9 = kwargs.get('value9')
        value10 = kwargs.get('value10')
        value11 = kwargs.get('value11')

        action_item = ActionItemSoft(self.driver)
        action_item.test_action_soft(username, password, value1, value2, value3, value4, value5, value6,
                                     value7, value8, value9, value10, value11)
