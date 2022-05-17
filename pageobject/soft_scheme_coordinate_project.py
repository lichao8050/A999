# _*_ coding: utf-8 _*_
# @Time    : 2021/5/19 0019 22:13
# @Author  : Mr_Li
# @FileName: soft_scheme_coordinate_project.py
from time import sleep

from base.base_page import BasePage
from base.base_util import logger
from pageobject.login_page import LoginPage
from pageobject.soft_decoration_division_page import SoftBusinessDivisionPage
from pageobject.system_dictionary_list import matrix

logger.info('---执行项目--软装方案配合项目新增---')


class SoftSchemeCoordinateProject(BasePage):
    """软装方案配合项目新增"""

    def test_soft_scheme_coordinate_project(self, username, password, value1, value2, value3, value4, value5, value6
                                            , value7, value8, value9, value10, value11, value12, value13, value14,
                                            value15):
        login = LoginPage(self.driver)  # 登录
        login.login_erp(username, password)  # 输入用户名、密码

        sleep(1)
        logger.info('点击“项目流程”')
        self.click(matrix.project_procedures)
        logger.info('点击“软装事业部”')
        self.click(matrix.soft_decoration_division)
        logger.info('点击“方案清单配合项目”')
        self.click(SoftBusinessDivisionPage.list_matching_project)
        logger.info('点击“新增按钮”')
        self.click(SoftBusinessDivisionPage.list_matching_new_add_button)
        sleep(1)
        logger.info('点击方案清单项目')
        self.click(SoftBusinessDivisionPage.list_matching_project_choose)
        logger.info('输入项目名称')
        self.send_ks(SoftBusinessDivisionPage.project_name, value1)
        logger.info('点击“商务总监”')
        self.click(SoftBusinessDivisionPage.CBO_business)
        logger.info('输入总监姓名')
        self.send_ks(SoftBusinessDivisionPage.CBO_business_select, value2)
        sleep(1)
        logger.info('点击查询按钮')
        self.click(SoftBusinessDivisionPage.CBO_business_select_button)
        logger.info('选择查询到的总监')
        self.click(SoftBusinessDivisionPage.CBO_business_choose)
        logger.info('点击“确定”按钮')
        self.click(SoftBusinessDivisionPage.CBO_business_yes_button)
        logger.info('点击‘选择一个商务经理’')
        self.click(SoftBusinessDivisionPage.business_manager)
        logger.info('选择第一个')
        self.click(SoftBusinessDivisionPage.business_manager_choose)
        logger.info('点击“确定”按钮')
        self.click(SoftBusinessDivisionPage.business_manager_yes_button)
        logger.info('点击“是否公司硬装”')
        self.click(SoftBusinessDivisionPage.whether_company_soft)
        logger.info('选择“是否公司硬装”')
        self.click_index(SoftBusinessDivisionPage.whether_company_soft_choose, value3)
        logger.info('点击“硬装设计师”')
        self.click(SoftBusinessDivisionPage.hard_stylist)
        logger.info('选择“硬装设计师”')
        self.click_index(SoftBusinessDivisionPage.hard_stylist_choose, value4)
        logger.info('输入“开始时间”')
        self.send_ks(SoftBusinessDivisionPage.start_time, value5)
        logger.info('键盘确定')
        self.keyboard_enter()
        logger.info('输入“预计完成时间”')
        self.send_ks(SoftBusinessDivisionPage.end_time, value6)
        logger.info('键盘确定')
        self.keyboard_enter()
        logger.info('点击‘项目小组’')
        self.click(SoftBusinessDivisionPage.project_group)
        logger.info('选择第一个')
        self.click(SoftBusinessDivisionPage.business_manager_choose)
        logger.info('点击“确定”按钮')
        self.click(SoftBusinessDivisionPage.project_group_confirm)
        logger.info('点击‘设计总监’')
        self.click(SoftBusinessDivisionPage.design_director)
        logger.info('选择第一个')
        self.click(SoftBusinessDivisionPage.business_manager_choose)
        logger.info('点击“确定”按钮')
        self.click(SoftBusinessDivisionPage.design_director_confirm)
        logger.info('点击‘项目经理’')
        self.click(SoftBusinessDivisionPage.project_manager)
        logger.info('选择第一个')
        self.click(SoftBusinessDivisionPage.business_manager_choose)
        logger.info('点击“确定”按钮')
        self.click(SoftBusinessDivisionPage.project_manager_confirm)
        logger.info('点击‘业态类型’')
        self.send_ks(SoftBusinessDivisionPage.formats_type, value7)
        if value7 == '酒店':
            logger.info('选择‘业态类型’')
            self.click(SoftBusinessDivisionPage.formats_type_choose)
        else:
            logger.info('选择‘业态类型’')
            self.click(SoftBusinessDivisionPage.formats_type_choose1)
        sleep(1)
        if value7 == '酒店':
            logger.info('点击‘二级业态类型’')
            self.click(SoftBusinessDivisionPage.formats_type_first)
            logger.info('选择‘二级业态类型’')
            self.click_index(SoftBusinessDivisionPage.formats_type_first_choose, value8)
        else:
            pass
        logger.info('输入户型明细')
        self.send_ks(SoftBusinessDivisionPage.family_breakdown, value9)
        logger.info('输入面积')
        self.send_ks(SoftBusinessDivisionPage.area, value10)
        logger.info('输入合同金额')
        self.send_ks(SoftBusinessDivisionPage.contract_amount, value11)
        logger.info('点击‘开拓项目系数’')
        self.click(SoftBusinessDivisionPage.expand_coefficient)
        logger.info('选择‘开拓项目系数’')
        self.click_index(SoftBusinessDivisionPage.expand_coefficient_choose, value12)
        if value12 == 0 :
            pass
        else:
            logger.info('上传钉钉审批记录')
            self.send_ks(SoftBusinessDivisionPage.check_record, value13)
        logger.info('输入总监把控比例')
        self.send_ks(SoftBusinessDivisionPage.control_proportion, value14)
        if value14 == 0:
            sleep(1)
            logger.info('选择把控比例')
            self.click(SoftBusinessDivisionPage.control_proportion_choose)
        if value14 == 2 :
            logger.info('点击把控比例')
            self.click(SoftBusinessDivisionPage.control_proportion)
            logger.info('选择把控比例')
            self.click(SoftBusinessDivisionPage.control_proportion_choose1)
            logger.info('点击项目组得分比例')
            self.click(SoftBusinessDivisionPage.score_proportion)
            logger.info('选择项目组得分比例')
            self.click_index(SoftBusinessDivisionPage.score_proportion_choose, value15)
        # logger.info('点击保存')
        # self.click(SoftBusinessDivisionPage.list_matching_project_save)
