# _*_ coding: utf-8 _*_
# @Time    : 2021/5/19 0019 22:13
# @Author  : Mr_Li
# @FileName: bidding_project_hard.py
from time import sleep

from base.base_page import BasePage
from base.base_util import logger
from pageobject.bidding_project_hard_page import BiddingProjectHardPage
from pageobject.business_process import BusinessProcess
from pageobject.discuss_project_page import DiscussProjectPage
from pageobject.login_page import LoginPage
from pageobject.system_dictionary_list import matrix

logger.info('---投标项目新增--硬装---')


class BiddingProjectHard(BasePage):
    """投标项目新增--硬装"""

    def test_bidding_project_hard(self, username, password, value1, value2, value3, value4, value5, value6, value7,
                                  value8, value9, value10, value11, value12, value13, value14, value15, value16,
                                  value17):
        login = LoginPage(self.driver)  # 登录
        login.login_erp(username, password)  # 输入用户名、密码

        # 如果元素存在
        flag = self.get_presence_element(matrix.home_page_messages_close)
        try:
            assert flag == True
            logger.info('关闭小铃铛提醒')
            self.click(matrix.home_page_messages_close)
        except:
            logger.info('点击“商务流程”')
            self.click(matrix.business_process)
            logger.info('点击“项目立项”')
            self.click(BusinessProcess.approve_project)
            logger.info('点击“商務投标”')
            self.click(BusinessProcess.commercial_bid)
            logger.info('点击“投標項目(硬裝)”')
            self.click(BusinessProcess.bidding_project_hard)
            logger.info('点击“新增按钮”')
            self.click(BusinessProcess.add_new_button)
            logger.info('输入项目名称')
            self.send_ks(DiscussProjectPage.meeting_project_name, value1)
            logger.info('点击省/市')
            self.click(BiddingProjectHardPage.project_area_province)  # 点击省/市
            logger.info('选择省/市')
            self.click_index(BiddingProjectHardPage.project_area_province_choose, value2)  # 选择省/市
            logger.info('点击区域')
            self.click(BiddingProjectHardPage.project_area_city)  # 点击区域
            sleep(1)
            logger.info('选择区域')
            self.click_index(BiddingProjectHardPage.project_area_city_choose, value3)  # 选择区域
            logger.info('输入详细地址')
            self.send_ks(BiddingProjectHardPage.project_area_write_remark, value4)  # 输入详细地址
            logger.info('点击“客户来源”')
            self.click(BiddingProjectHardPage.meeting_customer_source)
            sleep(0.5)
            logger.info('选择客户来源')
            self.click_index(BiddingProjectHardPage.meeting_customer_source_choose, value5)
            logger.info('输入设计风格')
            self.send_ks(BiddingProjectHardPage.design_style, value6)  # 输入设计风格
            logger.info('输入预计完成时间')
            self.send_ks(BiddingProjectHardPage.predict_end_time, value7)
            logger.info('回车确定')
            self.keyboard_enter()
            logger.info('输入施工图时间')
            self.send_ks(BiddingProjectHardPage.production_drawing_time, value8)
            logger.info('回车确定')
            self.keyboard_enter()
            logger.info('点击“法人主体”')
            self.click(BiddingProjectHardPage.legal_person)
            logger.info('选择“法人主体”')
            self.click_index(BiddingProjectHardPage.legal_person_choose, value9)
            logger.info('输入商务标占比')
            self.send_ks(BiddingProjectHardPage.the_business_of, value10)
            logger.info('输入技术标占比')
            self.send_ks(BiddingProjectHardPage.technology_of, value11)
            logger.info('输入投标启动时间')
            self.send_ks(BiddingProjectHardPage.bid_start_time, value12)
            logger.info('回车确定')
            self.keyboard_enter()
            logger.info('输入回标时间')
            self.send_ks(BiddingProjectHardPage.return_time, value13)
            logger.info('回车确定')
            self.keyboard_enter()
            logger.info('点击“是否合作过”')
            self.click(BiddingProjectHardPage.whether_cooperation)
            logger.info('选择“是否合作过”')
            self.click_index(BiddingProjectHardPage.whether_cooperation_choose, value14)
            logger.info('点击“商务总监”')
            self.click(BiddingProjectHardPage.meeting_CBO_business)
            logger.info('输入总监姓名')
            self.send_ks(BiddingProjectHardPage.CBO_business_username, value15)
            sleep(1)
            logger.info('点击查询按钮')
            self.click(BiddingProjectHardPage.CBO_select_button)
            logger.info('选择查询到的总监')
            self.click(BiddingProjectHardPage.choose_number_one)
            logger.info('点击“确定”按钮')
            self.click(BiddingProjectHardPage.CBO_confirm_button)
            logger.info('点击‘选择一个商务经理’')
            self.click(BiddingProjectHardPage.meeting_business_manager)
            logger.info('选择第一个')
            self.click_index(BiddingProjectHardPage.choose_business_one1, value16)
            logger.info('点击“确定”按钮')
            self.click(BiddingProjectHardPage.manager_confirm_button)
            logger.info('点击‘商务进度’')
            self.click(BiddingProjectHardPage.business_progress)
            logger.info('选择商务进度')
            self.click_index(BiddingProjectHardPage.business_progress_quotation1, value17)
            logger.info('点击‘是否补充协议’')
            self.click(BiddingProjectHardPage.replenish_yes_or_no)
            logger.info('选择‘是否补充协议’')
            self.click(BiddingProjectHardPage.replenish_no)
            logger.info('点击‘甲方信息’')
            self.click(BiddingProjectHardPage.first_party_information)
            logger.info('点击‘签约甲方’')
            self.click(BiddingProjectHardPage.appoint_first_party)
            logger.info('选择第一个')
            self.click_index(BiddingProjectHardPage.choose_business_one1, value18)
            logger.info('点击“确定”按钮')
            self.click(BiddingProjectHardPage.manager_confirm_button)