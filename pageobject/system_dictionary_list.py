# _*_ coding: utf-8 _*_
# @Time     : 2021/10/15 10:47
# @Author   : Mr_Li
# @FileName : system_dictionary_list.py
from selenium.webdriver.common.by import By


class matrix:
    use_loc = (By.XPATH, "//input[@placeholder='請輸入賬號']")  # 請輸入賬號
    pas_loc = (By.XPATH, "//input[@placeholder='請輸入密碼']")  # 請輸入密碼

    tips = (By.XPATH, "//span[text()='提示']")  # 提示
    use_loc1 = (By.XPATH, "//input[@placeholder='请输入用户名']")  # 請輸入賬號
    pas_loc1 = (By.XPATH, "//input[@placeholder='请输入密码']")  # 請輸入密碼
    sub_loc = (By.XPATH, "//button[@type='button']")  # 点击登录按钮
    login_success = (By.XPATH, "//span[text()='小铃铛有您待处理的事项，是否立即去处理？']")  # 登录成功
    home_page = (By.XPATH, "//span[text()='首頁']")  # 首頁
    personal_homepage = (By.XPATH, "//span[text()='個人首頁']")  # 個人首頁
    matrix_mall = (By.XPATH, "//span[text()='矩陣商城']")  # 矩陣商城
    crm_management = (By.XPATH, "//span[text()='CRM管理']")  # CRM管理
    my_customer = (By.XPATH, "//span[text()='我的客戶']")  # 我的客戶
    all_customer = (By.XPATH, "//span[text()='全部客戶']")  # 全部客戶
    visitors_plan = (By.XPATH, "//span[text()='訪客計劃']")  # 訪客計劃
    customer_follow_up = (By.XPATH, "//span[text()='客戶跟進']")  # 客戶跟進
    customer_sea_pool = (By.XPATH, "//span[text()='客戶公海池']")  # 客戶公海池
    business_process = (By.XPATH, "//span[text()='商務流程']")  # 商務流程
    approve_project = (By.XPATH, "//span[text()='項目立項']")  # 項目立項
    business_negotiations = (By.XPATH, "//span[text()='商務洽談']")  # 商務洽談
    discuss_project = (By.XPATH, "//span[text()='洽談項目']")  # 洽談項目
    commercial_bid = (By.XPATH, "//span[text()='商务投标']")  # 商务投标
    bidding_project_hard = (By.XPATH, "//span[text()='投標項目(硬裝)']")  # 投標項目(硬裝)
    bidding_project_soft = (By.XPATH, "//span[text()='投標項目(軟裝)']")  # 投標項目(軟裝)
    project_procedures = (By.XPATH, "//span[text()='項目流程']")  # 项目流程
    project_implementation = (By.XPATH, "//span[text()='執行項目']")  # 執行項目
    business_dkp = (By.XPATH, "//span[text()='商務DKP']")  # 商務DKP
    invoice_management = (By.XPATH, "//span[text()='發票管理']")  # 發票管理
    change_contract = (By.XPATH, "//span[text()='合同变更']")  # 合同变更
    contract_management = (By.XPATH, "//span[text()='合同管理']")  # 合同管理
    using_management = (By.XPATH, "//span[text()='用印管理']")  # 用印管理
    factoring_business = (By.XPATH, "//span[text()='用印审批']")  # 用印审批
    collection_payment_management = (By.XPATH, "//span[text()='收付款管理']")  # 收付款管理
    margin_application = (By.XPATH, "//span[text()='保證金申請']")  # 保證金申請
    soft_decoration_division = (By.XPATH, "//span[text()='軟裝事業部']")  # 軟裝事業部
    real_estate_division = (By.XPATH, "//span[text()='地產事業部']")  # 地產事業部
    Easy_expense = (By.XPATH, "//span[text()='报销管理']")  # 报销管理
    expense_claim = (By.XPATH, "//span[text()='报销管理']")  # 报销申请
    home_page_messages_close = (By.XPATH, "//div[@aria-label='提示']//span[text()='取消']")  # 小铃铛提示“关闭”
    home_page_messages_no = (By.XPATH, "//div[@aria-label='提示']//span[text()='取消']")  # 小铃铛提示“取消”
    home_page_messages_yes = (By.XPATH, "//div[@aria-label='提示']//span[text()='确定']")  # 小铃铛提示“确定”
    # 酒店事業部
    # 辦公事業部
    # 合縱事業部
    # idm事業部
    # 精裝事業部
    # 公共環境部
    '''# DKP管理
    DKP management
        # 團隊DKP申請
    Team DKP application
        # 制作DKP申请
    Make DKP application
    # 合同管理
    contract management
        # 用印管理
    Using the management
        # 用印审批
    Using the approval
        # 主合同管理
        # 子合同管理
        # 合同注销终止
        # 合同文件上传
    # 印章管理
    # 財務管理
        # 開票
    make out an invoice
        # 收款
    gathering
        # 付款
    payment
        # 应收管理
    Accounts receivable management
        # 确认函导出
    Confirmation letter export
    # 报销管理

    # 報表管理
        # DKP統計
        # 小組DKP統計
        # 小組項目統計
        # 項目DKP統計
        # 部门DKP排名
        # 总监合同额报表
    # 團隊DKP
        # 團隊DKP報表
    # 流程管理
        # 我的申请
        # 我的待办
        # 我的已办
        # 我的抄送
        # 全部申請
    # 矩阵学院
        # 學院首頁
        # 考試中心
        # 學院中心
    # 系統設置
        # 菜單導航
        # 崗位權限
        # 登錄賬號
        # 數據字典
        # 系統日誌
        # 附件類別
        # 導出模板
        # api文檔
        # 數據庫字典
        # 定時任務
        # 流程模型
        # 功能權限
        # 區域負責人
        # 時間表配置
        # 項目階段配置
        # 報表組織架構
        # 目標DKP配置
        # 製作DKP配置
    # 操作指南'''
