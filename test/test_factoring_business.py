# _*_ coding: utf-8 _*_
# @Time : 2021/9/6 12:15
# @Author  : Mr_Li
# @FileName: test_factoring_business.py
from base.base_util import BaseUtil
# 数据驱动ddt导包
from ddt import ddt
# yaml文件导包
from ddt import file_data

from pageobject.stamp.stamp_service_factoring_business import FactoringBusiness


@ddt
class TestFactoringBusiness(BaseUtil):
    """保理相关文件--用印审批"""

    @file_data('E:\\A999\\yaml\\other_business_documents.yaml')
    def test_factoring_business(self, **kwargs):
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

        action_item = FactoringBusiness(self.driver)
        action_item.test_factoring_business(username, password, value1, value2, value3, value4, value5,
                                            value6, value7, value8, value9, value10)
