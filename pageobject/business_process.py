# _*_ coding: utf-8 _*_
# @Time     : 2022/4/6 14:59
# @Author   : Mr_Li
# @FileName : business_process.py
from selenium.webdriver.common.by import By


class BusinessProcess:

    # 项目立项
    approve_project = (By.XPATH, "//span[text()='項目立項']")
    # 商務洽談
    business_negotiations = (By.XPATH, "//span[text()='商務洽談']")
    # 洽談項目
    discuss_project = (By.XPATH, "//span[text()='洽談項目']")
    '''洽谈项目展示页面'''
    # 所属事业部
    business_division = (By.XPATH, "//*[contains(text(),'所属事业部')]//parent::div//input[@placeholder='请选择']")
    # 项目名称
    project_name = (By.XPATH, "//*[contains(text(),'项目名称')]//parent::div//input[@placeholder='请输入']")
    # 客户来源
    customer_source = (By.XPATH, "//*[contains(text(),'客户来源')]//parent::div//input[@placeholder='请选择']")
    # 项目状态
    project_status = (By.XPATH, "//*[contains(text(),'项目状态')]//parent::div//input[@placeholder='请选择']")
    # 合同签订日期
    date_of_contract = (By.XPATH, "//*[contains(text(),'合同签订日期')]//parent::div//input[@placeholder='开始日期']")
    # 结束日期
    date_closed = (By.XPATH, "//*[contains(text(),'合同签订日期')]//parent::div//input[@placeholder='结束日期']")
    # 商务总监
    CBO_business = (By.XPATH, "//*[contains(text(),'商务总监')]//parent::div//input[@placeholder='请选择']")
    # 商务经理
    business_manager = (By.XPATH, "//*[contains(text(),'商务经理')]//parent::div//input[@placeholder='请选择']")
    # 设计总监
    design_director = (By.XPATH, "//*[contains(text(),'设计总监')]//parent::div//input[@placeholder='请选择']")
    # 设计师
    stylist = (By.XPATH, "//*[contains(text(),'设计师')]//parent::div//input[@placeholder='请输入']")
    # 集团名称
    group_name = (By.XPATH, "//*[contains(text(),'集团名称')]//parent::div//input[@placeholder='请选择']")
    # 项目编码
    item_coding = (By.XPATH, "//*[contains(text(),'项目编码')]//parent::div//input[@placeholder='请输入']")
    inquire_button = (By.XPATH, "//span[text()='查询']")  # 查询按钮
    clear_button = (By.XPATH, "//span[text()='清空']")  # 清空按钮
    add_new_button = (By.XPATH, "//button//span[contains(text(),'新增')]")  # 新增按钮
    look_over_button = (By.XPATH, "//span[text()='查看']")  # 查看按钮
    compile_button = (By.XPATH, "//span[text()='编辑']")  # 编辑按钮

    # 商务投标
    commercial_bid = (By.XPATH, "//span[text()='商务投标']")
    # 投標項目(硬裝)
    bidding_project_hard = (By.XPATH, "//span[text()='投標項目(硬裝)']")
    # 投標項目(軟裝)
    bidding_project_soft = (By.XPATH, "//span[text()='投標項目(軟裝)']")
    # 執行項目
    business_process_action_item = (By.XPATH, "//span[text()='執行項目']")
    # 商務DKP
    business_dkp = (By.XPATH, "//span[text()='商務DKP']")
    # 發票管理
    invoice_management = (By.XPATH, "//span[text()='發票管理']")
    # 合同变更
    contract_change = (By.XPATH, "//span[text()='合同变更']")
    # 合同管理
    contract_management = (By.XPATH, "//span[text()='合同管理']")
    # 收付款管理
    Collection_and_payment_management = (By.XPATH, "//span[text()='收付款管理']")
    # 保證金申請
    margin_application = (By.XPATH, "//span[text()='保證金申請']")
    # 商务比对
    business_alignment = (By.XPATH, "//span[text()='商务比对']")

