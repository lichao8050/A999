# _*_ coding: utf-8 _*_
# @Time : 2021/9/6 12:15
# @Author  : Mr_Li
# @FileName: test_soft_scheme_coordinate_project.py
from base.base_util import BaseUtil
# 数据驱动ddt导包
from ddt import ddt
# yaml文件导包
from ddt import file_data

from pageobject.soft_scheme_coordinate_project import SoftSchemeCoordinateProject


@ddt
class TestSoftSchemeCoordinateProject(BaseUtil):
    """软装方案配合项目新增"""

    @file_data('E:\\A999\\yaml\\soft_scheme_coordinate_project.yaml')
    def test_soft_scheme_coordinate_project(self, **kwargs):
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

        action_item = SoftSchemeCoordinateProject(self.driver)
        action_item.test_soft_scheme_coordinate_project(username, password, value1, value2, value3, value4, value5,
                                                        value6, value7 , value8, value9, value10, value11, value12,
                                                        value13, value14, value15)
