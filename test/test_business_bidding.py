# _*_ coding: utf-8 _*_
# @Time : 2021/9/6 12:15
# @Author  : Mr_Li
# @FileName: test_business_bidding.py
from base.base_util import BaseUtil
# 数据驱动ddt导包
from ddt import ddt
# yaml文件导包
from ddt import file_data
from pageobject.stamp.stamp_service_business_bidding import BusinessBidding


@ddt
class TestBusinessBidding(BaseUtil):
    """用印审批--商务招投标"""

    @file_data('E:\\A999\\yaml\\business_bidding.yaml')
    def test_stamp_service_purchasing_class(self, **kwargs):
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

        action_item = BusinessBidding(self.driver)
        action_item.test_business_bidding(username, password, value1, value2, value3,
                                          value4, value5, value6, value7, value8)
