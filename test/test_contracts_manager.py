# _*_ coding: utf-8 _*_
# @Time     : 2022/1/18 10:26
# @Author   : Mr_Li
# @FileName : test_contracts_manager.py

from base.base_util import BaseUtil
# 数据驱动ddt导包
from ddt import ddt, data, unpack
# yaml文件导包
from ddt import file_data

from pageobject.contracts_manager_project import ContractsManager


@ddt
class TestContractsManager(BaseUtil):
    """商务流程--合同管理"""

    @file_data("E:\\A999\\yaml\\contracts_manager.yaml")
    def test_action_item(self, **kwargs):
        username = kwargs.get('username')
        password = kwargs.get('password')
        value1 = kwargs.get('value1')

        action_item = ContractsManager(self.driver)
        action_item.test_contracts_manager(username, password, value1)
