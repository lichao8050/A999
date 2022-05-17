# _*_ coding: utf-8 _*_
# @Time     : 2022/4/20 9:37
# @Author   : Mr_Li
# @FileName : py_test.py

import unittest
from porttestpage.httpport import request
from porttestpage.port_page import PortElement
from jsonpath import jsonpath


class TestRequests(unittest.TestCase):

    # 测试执行项目修改审核状态
    def test_action_new_add1(self):
        response = request('post', url=PortElement.login_url, headers=PortElement.loggin_headers,
                           json=PortElement.login_test_value)
        print(response.status_code)
        print(response.headers['set-cookie'])
        response1 = request('post', url=PortElement.action_project_save_port1, headers=None,
                            json=PortElement.action_add_project1)
        print(response1.json(1))
