# _*_ coding: utf-8 _*_
# @Time    : 2021/5/13 0013 23:15
# @Author  : Mr_Li
# @FileName: test_add_customer.py
from ddt import ddt
from ddt import file_data
from base.base_util import BaseUtil
from pageobject.add_customer import AddCustomer


@ddt
class TestAddCustomer(BaseUtil):
    """新增客户"""

    @file_data('E:\\A999\\yaml\\add_customer.yaml')
    def test_add_customer(self, **kwargs):
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

        xz_kh1 = AddCustomer(self.driver)
        xz_kh1.test_add_customer(username, password, value1, value2, value3, value4, value5, value6,
                                 value7, value8, value9, value10, value11, value12, value13)
