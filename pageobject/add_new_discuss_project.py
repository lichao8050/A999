# _*_ coding: utf-8 _*_
# @Time     : 2021/10/18 12:16
# @Author   : Mr_Li
# @FileName : add_new_discuss_project.py

# 商务洽谈项目新增
from time import sleep
from base.base_page import BasePage
from base.base_util import logger
from pageobject.discuss_project_page import DiscussProjectPage
from pageobject.system_dictionary_list import matrix


class DiscussProject(BasePage):

    def discuss_project(self, username, password, value1, value2, value3):
        logger.info('输入用户名')
        self.send_ks(matrix.use_loc, username)
        logger.info('输入登录密码')
        self.send_ks(matrix.pas_loc, password)
        logger.info('点击登录按钮')
        self.click(matrix.sub_loc)
        sleep(1)
        logger.info('点击商務流程')
        self.click(matrix.business_process)
        logger.info('点击項目立項')
        self.click(matrix.approve_project)
        logger.info('点击商務洽談')
        self.click(matrix.business_negotiations)
        logger.info('点击洽談項目')
        self.click(matrix.discuss_project)
        logger.info('点击"新增按钮"')
        self.click(DiscussProjectPage.add_new_button)
        sleep(1)
        logger.info('点击"所属事业部"')
        self.click(DiscussProjectPage.meeting_business_division)
        list1 = [value2]
        for i in list1:
            if i == 1:
                logger.info('选择"软装"')
                self.click(DiscussProjectPage.meeting_business_division_soft)
            if i == 2:
                logger.info('选择"硬装"')
                self.click(DiscussProjectPage.meeting_business_division_hard)
        logger.info('输入项目名称')
        self.send_ks(DiscussProjectPage.meeting_project_name, value1)
        logger.info('点击"开发商区域"')
        self.click(DiscussProjectPage.area)
        logger.info('选择"开发商区域"')
        self.click(DiscussProjectPage.area_central_china)
        logger.info('点击"客户来源"')
        self.click(DiscussProjectPage.meeting_customer_source)
        logger.info('选择"客户来源"')
        self.click(DiscussProjectPage.meeting_customer_source_online)
        logger.info('点击"直委/投标"')
        self.click(DiscussProjectPage.straight_or_tender)
        list2 = [value3]
        for i in list2:
            if i == 1:
                logger.info('选择"直委"')
                self.click(DiscussProjectPage.straight)
            if i == 2:
                logger.info('选择"投标"')
                self.click(DiscussProjectPage.tender)
        logger.info('点击"甲方信息"')
        self.click(DiscussProjectPage.first_party_information)
        logger.info('点击"签约甲方"')
        self.click(DiscussProjectPage.appoint_first_party)
        sleep(3)
        logger.info('点击选择"第一条数据"')
        self.click(DiscussProjectPage.choose_customer_one)
        logger.info('点击"确定"按钮')
        self.click(DiscussProjectPage.first_party_confirm_button)
        logger.info('点击"保存"按钮')
        self.click(DiscussProjectPage.save_button)

        # self.assertEqual(DiscussProjectPage., afterchange, 'Change failed')


        # logger.info('点击所属事业部')
        # self.click(DiscussProjectPage.business_division)
        # sleep(1)
        # logger.info('点击项目名称')
        # self.click(DiscussProjectPage.project_name)
        # sleep(1)
        # logger.info('点击客户来源')
        # self.click(DiscussProjectPage.customer_source)
        # sleep(1)
        # logger.info('点击项目状态')
        # self.click(DiscussProjectPage.project_status)
        # sleep(1)
        # logger.info('点击合同签订日期')
        # self.click(DiscussProjectPage.date_of_contract)
        # sleep(1)
        # logger.info('点击结束日期')
        # self.click(DiscussProjectPage.date_closed)
        # sleep(1)
        # logger.info('点击商务总监')
        # self.click(DiscussProjectPage.CBO_business)
        # sleep(1)
        # logger.info('点击商务经理')
        # self.click(DiscussProjectPage.business_manager)
        # sleep(1)
        # logger.info('点击设计总监')
        # self.click(DiscussProjectPage.design_director)
        # sleep(1)
        # logger.info('点击设计师')
        # self.click(DiscussProjectPage.stylist)
        # sleep(1)
        # logger.info('点击集团名称')
        # self.click(DiscussProjectPage.group_name)
        # sleep(1)
        # logger.info('点击项目编码')
        # self.click(DiscussProjectPage.item_coding)
        # sleep(1)
        # logger.info('点击查询按钮')
        # self.click(DiscussProjectPage.inquire_button)

        # logger.info('')
        # logger.info('')
        # logger.info('')
        # logger.info('')
        # logger.info('')
        # logger.info('')
        # logger.info('')
        # logger.info('')
        # logger.info('')
        # logger.info('')
        # logger.info('')
#
# scenename = self.driver.find_elements_by_xpath('//android.widget.TextView[@index="0"]')
# afterchange = scenename[6].text
# scenename[6].click()
# time.sleep(10)
# # To verify whether the scene change successfully
# self.assertEqual(self.driver.find_element_by_id('com.lashou.cloud:id/tv_scenes').text,afterchange,'Change failed')