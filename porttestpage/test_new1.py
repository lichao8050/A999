# _*_ coding: utf-8 _*_
# @Time     : 2022/4/25 20:24
# @Author   : Mr_Li
# @FileName : test_new1.py
import unittest
from porttestpage.httpport import request
from porttestpage.port_page import PortElement
from jsonpath import jsonpath


class TestRequests(unittest.TestCase):

    # 登录用例
    def test_login_api(self):
        response = request('post', url=PortElement.login_url, headers=PortElement.loggin_headers,
                           json=PortElement.login_test_value)
        print(response.status_code)
        print(response.headers['set-cookie'])
        li = response.json()
        s = jsonpath(li, '$..id')
        print(s)
        response1 = request('post', url=PortElement.action_select_url, headers=PortElement.loggin_headers,
                            json=PortElement.action_projedt_select_value)
        print(response1.json())

    # 新增硬装投标项目
    def test_add_new_hardbid_project(self):
        response = request('post', url=PortElement.login_url, headers=PortElement.loggin_headers,
                           json=PortElement.login_test_value)
        print(response.status_code)
        print(response.headers['set-cookie'])
        response1 = request('post', url=PortElement.hardbid_project_save_port, headers=PortElement.loggin_headers,
                            json=PortElement.add_hardbid_project)
        print(response1.text)

    # 新增软装投标项目
    def test_add_new_softbid_project(self):
        response = request('post', url=PortElement.login_url, headers=PortElement.loggin_headers,
                           json=PortElement.login_test_value)
        print(response.status_code)
        print(response.headers['set-cookie'])
        response1 = request('post', url=PortElement.softbid_project_save_port, headers=PortElement.loggin_headers,
                            json=PortElement.add_softbid_project)
        print(response1.text)

    # 新增执行项目
    def test_action_new_add(self):
        response = request('post', url=PortElement.login_url, headers=PortElement.loggin_headers,
                           json=PortElement.login_test_value)
        print(response.status_code)
        print(response.headers['set-cookie'])
        response1 = request('post', url=PortElement.action_project_save_port, headers=None,
                            json=PortElement.action_add_project)
        print(response1.json())

    # 执行项目查看
    def test_action_view(self):
        response = request('post', url=PortElement.login_url, headers=PortElement.loggin_headers,
                           json=PortElement.login_test_value)
        print(response.status_code)
        print(response.headers['set-cookie'])
        response1 = request('post', url=PortElement.action_project_examine_port, headers=None,
                            data=PortElement.action_examine)
        print(response1.text)

    def test_gw_p(self):
        response = request('post', url=PortElement.gw_port, headers=None,
                           json=None)
        print(response.text)
