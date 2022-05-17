# _*_ coding: utf-8 _*_
# @Time    : 2021/5/19 0019 22:36
# @Author  : LiChao
# @FileName: test_action_item.py
from base.base_util import BaseUtil
from pageobject.action_item import ActionItem


class TestActionItem(BaseUtil):

    def test_action_item(self):
        '''商务合同-用印审批'''

        action_item = ActionItem(self.driver)
        action_item.test_action_item(username='heqiangming', password='abc123456',
                                     value1='厦门亿联软件综合楼一期#30511', value2='这是测试地址1', value3=155000,
                                     value4='1测试设计风格@',
                                     value5='@简约、现代', value6='暂时没有其它需求', value7="2021-08-10",
                                     value8='2021-08-10',
                                     value9='2021-08-11', value10='2021-08-12', value11='Y2021081012',
                                     value12='东升室内装修设计', value13='')
