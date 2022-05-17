# _*_ coding: utf-8 _*_
# @Time    : 2021/5/19 0019 22:36
# @Author  : Mr_Li
# @FileName: test_shangwuhetongshenpi.py
from base.base_util import BaseUtil
from pageobject.stamp.yyshenpi_swht_page import YyShenPiSwHtPage


class TestShangWuHtShenPi(BaseUtil):
    """商务合同-用印审批"""

    def test_shangwuhetongshenpi(self):
        swht_yysp = YyShenPiSwHtPage(self.driver)
        swht_yysp.test_swht_yysp(
            username='wutingting', password='abc123456',
            value1='商务合同用印审批，关联测试4',
            value2=10000, value3=11, value4=15,
            value5='2021-04-21这是用于测试的一段文字！2@',
            value6=r'D:/测试用图片/测试图片1.jpg',
            value7=r'D:/测试用图片/钢铁是怎样炼成的.pdf',
            value8=r'D:/测试用图片/2021-04-16这是一条关于商务合同用印审批申请的测试消息题目.png'
            , value9='Keys.ENTER')
