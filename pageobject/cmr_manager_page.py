# _*_ coding: utf-8 _*_
# @Time     : 2022/4/15 18:32
# @Author   : Mr_Li
# @FileName : cmr_manager_page.py


class CmrManagerPage:
    """cmr管理"""

    week_new_ad = (By.XPATH, "")  # 本周新增
    '''我的客户页面'''
    my_customer = (By.XPATH, "//span[text()='我的客戶']")  # 我的客户
    all = (By.XPATH, "//div[text()='全部']")  # 全部
    today_new_add = (By.XPATH, "//div[text()='今日新增']")  # 今日新增
    week_new_add = (By.XPATH, "//div[text()='本周新增']")  # 本周新增
    company_name = (By.XPATH, "//input[@placeholder='请输入集团名称']")  # 集团名称
    customer_unit = (By.XPATH, "placeholder='请输入客户单位'")  # 客户单位
    charater_of_customer = (By.XPATH, "//*[contains(text(),'客户性质：')]"
                                      "//parent::div//input[@placeholder='请选择']")  # 客户性质
    charater_of_customer_choose = (By.XPATH, "//div[@x-placement='bottom-start']//li")  # 客户性质选择
    client_grade = (By.XPATH, "//*[contains(text(),'客户等级：')]//parent::div//input[@placeholder='请选择']")  # 客户等级
    province = (By.XPATH, "")  # 省
    city = (By.XPATH, "")  # 市
    matrix_area = (By.XPATH, "")  # 矩阵区域

    administrative_region = (By.XPATH, "")  # 行政区域
    input_time = (By.XPATH, "")  # 录入时间

    '''全部客户页面'''
    all_customer = (By.XPATH, "//span[text()='全部客戶']")  # 全部客户

    '''访客计划页面'''
    visitors_to_plan = (By.XPATH, "//span[text()='訪客計劃']")  # 访客计划

    '''客户跟进页面'''
    client_follow_up = (By.XPATH, "//span[text()='客戶跟進']")  # 客户跟进

    '''客户公海池页面'''
    customer_open_sea_Pool = (By.XPATH, "//span[text()='客戶公海池']")  # 客户公海池
