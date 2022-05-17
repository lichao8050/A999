# _*_ coding: utf-8 _*_
# @Time : 2021/9/6 12:15
# @Author  : Mr_Li
# @FileName: test_labor_relations.py
from base.base_util import BaseUtil
# 数据驱动ddt导包
from ddt import ddt
# yaml文件导包
from ddt import file_data
from pageobject.stamp.stamp_service_labor_relations import LaborRelations


@ddt
class TestLaborRelations(BaseUtil):
    """劳动关系证明文件--用印审批"""

    @file_data('E:\\A999\\yaml\\labor_relations.yaml')
    def test_stamp_service_purchasing_class(self, **kwargs):
        username = kwargs.get('username')
        password = kwargs.get('password')
        value1 = kwargs.get('value1')
        value2 = kwargs.get('value2')
        value3 = kwargs.get('value3')
        value4 = kwargs.get('value4')
        value5 = kwargs.get('value5')

        action_item = LaborRelations(self.driver)
        action_item.test_labor_relations(username, password, value1, value2, value3, value4, value5)
