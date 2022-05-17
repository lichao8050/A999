# _*_ coding: utf-8 _*_
# @Time     : 2022/5/17 11:29
# @Author   : Mr_Li
# @FileName : test_case1.py
import unittest
from base.base_start import pyselenium
from pageobject.system_dictionary_list import matrix
from base.base_util import BaseUtil


class TestLogin(BaseUtil):

    def test_loggion(self):
        self.driver = pyselenium(brower="Chrome")
        self.driver.make_maxwindow()
        self.driver.open("http://kbs.matrixdesign.cn/")
        self.driver.send_ke(fangfa == "xpath", matrix.use_loc, "heqiangming")
        self.driver.send_ke(fangfa == "xpath", matrix.pas_loc, "abc123456")
        self.click(fangfa == "xpath", matrix.sub_loc)
