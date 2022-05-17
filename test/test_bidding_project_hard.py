# _*_ coding: utf-8 _*_
# @Time    : 2021/5/19 0019 22:36
# @Author  : Mr_li
# @FileName: test_bidding_project_hard.py

# 数据驱动ddt导包
from ddt import ddt
# yaml文件导包
from ddt import file_data

from base.base_util import BaseUtil
from pageobject.bidding_project_hard import BiddingProjectHard


@ddt
class TestBiddingProjectHard(BaseUtil):
    """投标项目--硬装"""

    @file_data("E:\\A999\\yaml\\bidding_project_hard.yaml")
    def test_bidding_project_hard(self, **kwargs):
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
        value12 = kwargs.get('value12')
        value13 = kwargs.get('value13')
        value14 = kwargs.get('value14')
        value15 = kwargs.get('value15')
        value16 = kwargs.get('value16')
        value17 = kwargs.get('value17')

        action_item = BiddingProjectHard(self.driver)
        action_item.test_bidding_project_hard(username, password, value1, value2, value3, value4, value5, value6,
                                              value7, value8, value9, value10, value11, value12, value13, value14,
                                              value15, value16, value17)
