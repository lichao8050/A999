# _*_ coding: utf-8 _*_
# @Time     : 2022/1/18 10:23
# @Author   : Mr_Li
# @FileName : contracts_manager_project.py
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from time import sleep
from base.base_util import logger
from pageobject.login_page import LoginPage
import traceback

from pageobject.system_dictionary_list import matrix

logger.info('---商务流程--合同管理---')


class ContractsManager(BasePage):
    """商务流程--合同管理"""

    contract_manager_project_name = (By.XPATH, "//*[text()='项目名称：']//parent::div//input")  # 项目名称
    contract_manager_project_number = (By.XPATH, "//*[text()='项目编码：']//parent::div//input")  # 项目编码
    contract_manager_sap_number = (By.XPATH, "//*[text()='SAP编码：']//parent::div//input")  # SAP编码
    contract_manager_project_status = (By.XPATH, "//*[text()='项目状态：']//parent::div//input")  # 项目状态
    contract_manager_project_status_one = (By.XPATH, "//*[text()='项目状态：']//parent::div//li[1]")  # 项目状态1
    contract_manager_group_name = (By.XPATH, "//*[text()='集团名称：']//parent::div//input")  # 集团名称
    contract_manager_group_name_one = (By.XPATH, "//*[text()='集团名称：']//parent::div//li[1]")  # 集团名称1
    contract_manager_face_name = (By.XPATH, "//*[text()='签约甲方名称：']//parent::div//input")  # 签约甲方名称
    contract_manager_customer_source = (By.XPATH, "//*[text()='客户来源：']//parent::div//input")  # 客户来源
    contract_manager_customer_source_one = (By.XPATH, "//*[text()='客户来源：']//parent::div//li[1]")  # 客户来源1
    contract_manager_date_signing = (By.XPATH, "//*[text()='合同签订日期：']//parent::div//input[1]")  # 合同签订日期
    contract_manager_date_signing_today = (By.XPATH, "//div[@x-placement='bottom-end']"
                                                     "//button[text()='今天']")  # 合同签订日期:今天
    contract_manager_business_division = (By.XPATH, "//*[text()='所属事业部：']//parent::div//input")  # 所属事业部
    contract_manager_business_division_hard = (By.XPATH, "//*[text()='所属事业部：']//parent::div//li[1]")  # 所属事业部：硬装
    contract_manager_design_director = (By.XPATH, "//*[text()='设计总监：']//parent::div//input")  # 设计总监
    contract_manager_design_director_one = (By.XPATH, "//*[text()='设计总监：']//parent::div//li[1]")  # 设计总监1
    contract_manager_designer = (By.XPATH, "//*[text()='设计师：']//parent::div//input")  # 设计师
    contract_manager_audit_status = (By.XPATH, "//*[text()='审核状态：']//parent::div//input")  # 审核状态
    contract_manager_audit_status_one = (By.XPATH, "//*[text()='审核状态：']//parent::div//li[1]")  # 审核状态:待提交
    contract_manager_select_button = (By.XPATH, "//span[text()='查询']")  # 查询按钮
    contract_manager_clear_button = (By.XPATH, "//span[text()='清空']")  # 清空按钮
    contract_manager_editor_button = (By.XPATH, "//div[@style='width: 150px;']"
                                                "//span[contains(text(),'编辑')]")  # 第一条数据编辑按钮
    contract_manager_view_button = (By.XPATH, "//div[@style='width: 150px;']"
                                              "//span[contains(text(),'查看')]")  # 第一条数据查看按钮
    contract_manager_contract_details = (By.XPATH, "//div[(text()='合同详情')]")  # 合同详情
    contract_manager_contract_details_1 = (By.XPATH, "//input")  # 编辑

    def test_contracts_manager(self, username, password, value1):
        login = LoginPage(self.driver)  # 登录
        login.login_erp(username, password)  # 输入用户名、密码

        sleep(1)
        logger.info('点击“商务流程”')
        self.click(matrix.business_process)  # 点击“商务流程”
        logger.info('点击“合同管理”')
        self.click(matrix.contract_management)  # 点击“合同管理”
        sleep(3)
        self.click_index(ContractsManager.contract_manager_contract_details_1, value1)
        # logger.info('输入项目名称')
        # self.send_ks(ContractsManager.contract_manager_project_name, value1)  # 输入项目名称
        # sleep(2)
        # logger.info('点击查询按钮')
        # self.click(ContractsManager.contract_manager_select_button)  # 点击查询按钮
        # logger.info('点击编辑按钮')
        # self.click(ContractsManager.contract_manager_editor_button)  # 点击编辑按钮
