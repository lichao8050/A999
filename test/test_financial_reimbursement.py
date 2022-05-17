# _*_ coding: utf-8 _*_
# @Time : 2021/9/6 12:15
# @Author  : Mr_Li
# @FileName: test_expense_claim.py
from base.base_util import BaseUtil
# 数据驱动ddt导包
from ddt import ddt, data, unpack
# yaml文件导包
from ddt import file_data

from pageobject.financial_reimbursement import ExpenseClaim


@ddt
class TestExpenseClaim(BaseUtil):
    """报销管理--报销申请"""

    @file_data('E:\\A999\\yaml\\expense_claim.yaml')
    def test_expense_claim(self, **kwargs):
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

        hard_coordinate = ExpenseClaim(self.driver)
        hard_coordinate.test_expense_claim(username, password, value1, value2, value3, value4, value5, value6,
                                                     value7, value8, value9, value10, value11, value12, value13,
                                                     value14, value15)
