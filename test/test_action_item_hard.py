# _*_ coding: utf-8 _*_
# @Time    : 2021/5/19 0019 22:36
# @Author  : Mr_Li
# @FileName: test_action_item_hard.py
# 数据驱动ddt导包
from ddt import ddt
# yaml文件导包
from ddt import file_data

from base.base_util import BaseUtil
from pageobject.action_item_hard import ActionItemHard


@ddt
class TestActionItemHard(BaseUtil):
    """执行项目--硬装"""

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
        value11 = kwargs.get('value11')

        action_item = ActionItemHard(self.driver)
        action_item.test_action_hard(username, password, value1, value2, value3,
                                     value4, value5, value6, value7, value11)
