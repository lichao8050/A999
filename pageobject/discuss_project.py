# _*_ coding: utf-8 _*_
# @Time    : 2021/5/19 0019 22:13
# @Author  : Mr_Li
# @FileName: discuss_project.py
from time import sleep

from base.base_page import BasePage
from base.base_util import logger
from pageobject.business_process import BusinessProcess
from pageobject.discuss_project_page import DiscussProjectPage
from pageobject.login_page import LoginPage
from pageobject.system_dictionary_list import matrix

logger.info('---洽谈项目新增--软装---')


class DiscussProject(BasePage):
    """洽谈项目新增--软装"""

    def test_discuss_project(self, username, password, value1, value2, value3, value4, value5):
        login = LoginPage(self.driver)  # 登录
        login.login_erp(username, password)  # 输入用户名、密码

        sleep(1)
        logger.info('点击“商务流程”')
        self.click(matrix.business_process)
        logger.info('点击“项目立项”')
        self.click(BusinessProcess.approve_project)
        logger.info('点击“商務洽談”')
        self.click(BusinessProcess.business_negotiations)
        logger.info('点击“洽談項目”')
        self.click(BusinessProcess.discuss_project)
        logger.info('点击“新增按钮”')
        self.click(BusinessProcess.add_new_button)
        logger.info('输入项目名称')
        self.send_ks(DiscussProjectPage.meeting_project_name, value1)
        logger.info('点击“开发商所属区域”')
        self.click(DiscussProjectPage.area)
        logger.info('选择开发商所属区域')
        self.click_index(DiscussProjectPage.area_central_choose, value2)
        logger.info('点击“客户来源”')
        self.click(DiscussProjectPage.meeting_customer_source)
        sleep(0.5)
        logger.info('选择客户来源')
        self.click_index(DiscussProjectPage.meeting_customer_source_choose, value3)
        logger.info('输入合作方信息')
        self.send_ks(DiscussProjectPage.partner_information, value4)
        logger.info('点击“直委/投标”')
        self.click(DiscussProjectPage.straight_or_tender)
        logger.info('选择‘直委/投标’')
        self.click_index(DiscussProjectPage.straight_or_tender_choose, value5)
        logger.info('点击“预计设计启动时间”')
        self.click(DiscussProjectPage.start_up_time)
        logger.info('选择“预计设计启动时间”')
        self.click(DiscussProjectPage.eighteen_number)
        logger.info('点击“回标/摆场时间”')
        self.click(DiscussProjectPage.business_dw23)
        sleep(1)
        logger.info('选择“回标/摆场时间”')
        self.click(DiscussProjectPage.business_dw231)
        logger.info('点击“项目开放时间”')
        self.click(DiscussProjectPage.opening_hours)
        sleep(1)
        logger.info('选择“项目开放时间”')
        self.click(DiscussProjectPage.today)
        logger.info('点击“商务总监”')
        self.click(DiscussProjectPage.business_dw25)
        logger.info('输入总监姓名')
        self.send_ks(DiscussProjectPage.business_dw251, value3)
        sleep(1)
        logger.info('点击查询按钮')
        self.click(DiscussProjectPage.business_dw252)
        logger.info('选择查询到的总监')
        self.click(DiscussProjectPage.business_dw253)
        logger.info('点击“确定”按钮')
        self.click(DiscussProjectPage.business_dw254)
        logger.info('选择一个商务经理')
        self.click(DiscussProjectPage.business_dw26)
        sleep(1)
        logger.info('点击查询按钮')
        self.click(DiscussProjectPage.business_dw261)
        logger.info('点击“确定”按钮')
        self.click(DiscussProjectPage.business_dw262)
        logger.info('点击“甲方信息”按钮')
        self.click(DiscussProjectPage.business_dw30)
        logger.info('点击“签约甲方”按钮')
        self.click(DiscussProjectPage.business_dw301)
        logger.info('输入“客户名称”按钮')
        self.send_ks(DiscussProjectPage.business_client_name, value4)
        sleep(1)
        logger.info('点击“查询”按钮')
        self.click(DiscussProjectPage.business_search_button)
        logger.info('点击“选择对应客户编号”按钮')
        self.click(DiscussProjectPage.business_client_number)
        logger.info('点击“确定”按钮')
        self.click(DiscussProjectPage.business_confirm_button)
        logger.info('点击“保存”按钮')
        self.click(DiscussProjectPage.business_save)
