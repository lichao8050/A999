# _*_ coding: utf-8 _*_
# @Time     : 2021/10/19 16:41
# @Author   : Mr_Li
# @FileName : discuss_project_page.py
from selenium.webdriver.common.by import By


class DiscussProjectPage:
    """洽谈项目"""

    add_new_button = (By.XPATH, "//span[text()='新增']")  # 新增按钮
    turn_tender_project = (By.XPATH, "//span[text()='转成投标项目']")  # 转成投标项目
    turn_execute_project = (By.XPATH, "//span[text()='转成执行项目']")  # 转成执行项目
    project_termination = (By.XPATH, "//span[text()='项目终止']")  # 项目终止
    save_button = (By.XPATH, "//span[text()='保存']")  # 保存
    clear = (By.XPATH, "//span[text()='清空']")  # 清空
    project_information = (By.XPATH, "//div[text()='项目信息']")  # 项目信息
    meeting_project_name = (By.XPATH, "//input[@placeholder='城市+地产+项目名称+硬装设计/软装采购']")  # 项目名称
    area = (By.XPATH, "//*[contains(text(),'开发商所属区域')]//parent::div//input[@placeholder='请选择']")  # 开发商所属区域
    area_central_choose = (By.XPATH, "//div[@x-placement='bottom-start']//li")  # 选择开发商所属区域
    meeting_customer_source = (By.XPATH, "//*[contains(text(),'客户来源')]//parent::div//input[@placeholder='请选择']")  # 客户来源
    meeting_customer_source_choose = (By.XPATH, "//div[@x-placement='bottom-start']//li")  # 选择客户来源
    partner_information = (By.XPATH, "//input[@placeholder='请输入合作方信息']")  # 合作方信息
    straight_or_tender = (By.XPATH, "//*[contains(text(),'直委or投标')]//parent::div//input[@placeholder='请选择']")  # 直委or投标
    straight_or_tender_choose = (By.XPATH, "//div[@x-placement='bottom-start']//li")  # 选择直委or投标
    start_time = (By.XPATH, "//input[@placeholder='请选择预计开工日期']")  # 预计设计启动时间
    start_time_today = (By.XPATH, "//button[text()='今天']")  # 预计设计启动时间--今天
    start_time_yesterday = (By.XPATH, "//button[text()='昨天']")  # 预计设计启动时间--昨天
    start_time_monday = (By.XPATH, "//button[text()='周一']")  # 预计设计启动时间--周一
    start_time_beginning_month = (By.XPATH, "//button[text()='月初']")  # 预计设计启动时间--月初
    start_time_beginning_year = (By.XPATH, "//button[text()='年初']")  # 预计设计启动时间--年初
    return_time = (By.XPATH, "//input[@placeholder='请选择回标/摆场时间']")  # 回标 / 摆场时间
    return_time_today = (By.XPATH, "//div[@x-placement='bottom-end']//button[text()='今天']")  # 回标 / 摆场时间--今天
    return_time_yesterday = (By.XPATH, "//div[@x-placement='bottom-end']//button[text()='昨天']")  # 回标 / 摆场时间--昨天
    return_time_monday = (By.XPATH, "//div[@x-placement='bottom-end']//button[text()='周一']")  # 回标 / 摆场时间--周一
    return_time_beginning_month = (By.XPATH, "//div[@x-placement='bottom-end']//button[text()='月初']")  # 回标 / 摆场时间--月初
    return_time_beginning_year = (By.XPATH, "//div[@x-placement='bottom-end']//button[text()='年初']")  # 回标 / 摆场时间--年初
    open_time = (By.XPATH, "//input[@placeholder='请选择预计完工日期']")  # 项目开放时间
    open_time_today = (By.XPATH, "//div[@x-placement='bottom-end']//button[text()='今天']")  # 项目开放时间--今天
    open_time_yesterday = (By.XPATH, "//div[@x-placement='bottom-end']//button[text()='昨天']")  # 项目开放时间--昨天
    open_time_monday = (By.XPATH, "//div[@x-placement='bottom-end']//button[text()='周一']")  # 项目开放时间--周一
    open_time_beginning_month = (By.XPATH, "//div[@x-placement='bottom-end']//button[text()='月初']")  # 项目开放时间--月初
    open_time_beginning_year = (By.XPATH, "//div[@x-placement='bottom-end']//button[text()='年初']")  # 项目开放时间--年初
    meeting_CBO_business = (By.XPATH, "//input[@placeholder='选择一个商务总监']")  # 商务总监
    CBO_business_username = (By.XPATH, "//*[contains(text(),'用户名：')]//parent::div//input")  # 商务总监--用户名（输入搜索）
    choose_number_one = (By.XPATH, "//td[@class='el-table_17_column_158  ']//div[text()='1']")  # 选择搜索到的第一条数据
    choose_CBO_name = (By.XPATH, "//td[@class='el-table_17_column_159  ']//span[text()='王勇']")  # 选择搜索到的总监姓名
    CBO_select_button = (By.XPATH, "//*[contains(text(),'商务总监')]//parent::div//span[text()='查询']")  # 查询按钮
    CBO_clear_button = (By.XPATH, "//*[contains(text(),'商务总监')]//parent::div//span[text()='清空']")  # 清空按钮
    CBO_confirm_button = (By.XPATH, "//*[contains(text(),'商务总监')]//parent::div//span[contains(text(),'确定')]")  # 确定按钮
    CBO_cancel_button = (By.XPATH, "//*[contains(text(),'商务总监')]//parent::div//span[contains(text(),'取消')]")  # 取消按钮
    meeting_business_manager = (By.XPATH, "//input[@placeholder='选择一个商务经理']")  # 商务经理
    manager_select_button = (By.XPATH, "//*[contains(text(),'商务经理')]//parent::div//span[text()='查询']")  # 查询按钮
    manager_clear_button = (By.XPATH, "//*[contains(text(),'商务经理')]//parent::div//span[text()='清空']")  # 清空按钮
    manager_confirm_button = (By.XPATH, "//*[contains(text(),'商务经理')]"
                                        "//parent::div//span[contains(text(),'确定')]")  # 确定按钮
    manager_cancel_button = (By.XPATH, "//*[contains(text(),'商务经理')]//parent::div//span[contains(text(),'取消')]")  # 取消按钮
    choose_business_one = (By.XPATH, "//td[@class='el-table_18_column_162  ']//div[text()='1']")  # 选择第一条数据
    business_progress = (By.XPATH, "//*[contains(text(),'商务进度')]//parent::div//input[@placeholder='请选择']")  # 商务进度
    business_progress_quotation = (By.XPATH, "//span[text()='报价中']")  # 商务进度--报价中
    business_progress_tender = (By.XPATH, "//span[text()='投标中']")  # 商务进度--投标中
    business_progress_evaluating = (By.XPATH, "//span[text()='评标中']")  # 商务进度--评标中
    business_progress_calibration = (By.XPATH, "//span[text()='已定标']")  # 商务进度--已定标
    business_progress_outbid = (By.XPATH, "//span[text()='已落标']")  # 商务进度--已落标
    meeting_business_division = (By.XPATH, "//*[contains(text(),'所属事业部')]//parent::div"
                                           "//input[@placeholder='请选择']")  # 所属事业部
    meeting_business_division_soft = (By.XPATH, "//div[@x-placement='bottom-start']"
                                                "//span[text()='软装']")  # 所属事业部--软装（默认）
    meeting_business_division_hard = (By.XPATH, "//div[@x-placement='bottom-start']//span[text()='硬装']")  # 所属事业部--硬装
    first_party_information = (By.XPATH, "//div[text()='甲方信息']")  # 甲方信息
    appoint_first_party = (By.XPATH, "//*[contains(text(),'签约甲方：')]//parent::div//input[@placeholder='请选择']")  # 签约甲方
    customer_id = (By.XPATH, "//div[contains(@style,'2038')]//input[@placeholder='甲方单位选择']")  # 客户编号
    customer_unit = (By.XPATH, "//div[contains(@style,'2038')]//input[@placeholder='请输入客户名称']")  # 客户单位
    first_party_select_button = (By.XPATH, "//span[text()='查询']")  # 查询按钮
    first_party_clear_button = (By.XPATH, "//span[text()='清空']")  # 清空按钮
    first_party_confirm_button = (By.XPATH, "//span[text()='确定']")  # 确定按钮
    first_party_cancel_button = (By.XPATH, "//span[text()='取消']")  # 取消按钮
    choose_customer_one = (By.XPATH, "//div[@class='el-table__fixed-body-wrapper']"
                                     "//input[@value='0']//ancestor::tr//div[text()='1']")  # 选择第一条数据
