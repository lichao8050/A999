# _*_ coding: utf-8 _*_
# @Time     : 2021/10/19 16:41
# @Author   : Mr_Li
# @FileName : bidding_project_hard_page.py
from selenium.webdriver.common.by import By


class BiddingProjectHardPage:
    """硬装投标项目"""

    turn_execute_project = (By.XPATH, "//span[text()='转成执行项目']")  # 转成执行项目
    save_button = (By.XPATH, "//span[text()='保存']")  # 保存
    clear = (By.XPATH, "//span[text()='清空']")  # 清空
    project_information = (By.XPATH, "//div[text()='项目信息']")  # 项目信息
    meeting_project_name = (By.XPATH, "//input[@placeholder='城市+地产+项目名称+硬装设计/软装采购']")  # 项目名称
    # 点击项目地址省市
    project_area_province = (
        By.XPATH, "//*[contains(text(),'项目地址：')]//parent::div//div[@class='region-picker']/div[1]//input")
    # 选择项目地址省/市
    project_area_province_choose = (By.XPATH, "//*[@x-placement='bottom-start']//li")
    # 点击项目地址市区
    project_area_city = (By.XPATH, "//*[contains(text(),'项目地址：')]//parent::div"
                                   "//div[@class='region-picker']/div[2]//input")
    # 选择项目地址市区
    project_area_city_choose = (By.XPATH, "//*[@x-placement='bottom-start']//li")
    # 输入详细地址信息
    project_area_write_remark = (By.XPATH, "//input[@placeholder='请输入详细地址信息']")
    meeting_customer_source = (By.XPATH, "//*[contains(text(),'客户来源')]//parent::div//input[@placeholder='请选择']")  # 客户来源
    meeting_customer_source_choose = (By.XPATH, "//div[@x-placement='bottom-start']//li")  # 选择客户来源
    # 是否公司软装
    whether_company_soft = (By.XPATH, "//*[contains(text(),'是否公司软装：')]//parent::div//input")
    # 选择是否公司软装
    whether_company_soft_choose = (By.XPATH, "//div[@x-placement='bottom-start']//li")
    # 请输入整体设计风格
    design_style = (By.XPATH, "//input[@placeholder='请输入整体设计风格']")
    predict_end_time = (By.XPATH, "//*[contains(text(),'预计完成时间：')]//parent::div//input")  # 预计完成时间
    predict_end_time_choose = (By.XPATH, "//button[text()='今天']")  # 选择预计完成时间
    production_drawing_time = (By.XPATH, "//*[contains(text(),'施工图时间：')]//parent::div//input")  # 施工图时间
    production_drawing_time_choose = (By.XPATH, "//button[text()='周一']")  # 选择施工图时间
    straight_commission_or_bid = (By.XPATH, "//*[contains(text(),'直委or投标：')]//parent::div//input")  # 直委or投标
    # 法人主体选择框
    legal_person = (By.XPATH, "//*[contains(text(),'法人主体：')]//parent::div//input[@type='text']")
    # 选择法人主体
    legal_person_choose = (By.XPATH, "//div[@x-placement='bottom-start']//li")
    # 商务标 / 技术标
    the_tender_way = (By.XPATH, "//*[contains(text(),'商务标/技术标：')]//parent::div//input")
    # 选择商务/技术标
    the_tender_way_choose = (By.XPATH, "//div[@x-placement='bottom-start']//li")
    # 商务标占比
    the_business_of = (By.XPATH, "//*[contains(text(),'商务标占比：')]//parent::div//input")
    # 技术标占比
    technology_of = (By.XPATH, "//*[contains(text(),'技术标占比：')]//parent::div//input")
    bid_start_time = (By.XPATH, "//*[contains(text(),'投标启动时间：')]//parent::div//input")  # 投标启动时间
    bid_start_time_choose = (By.XPATH, "//button[text()='年初']")  # 选择投标启动时间
    return_time = (By.XPATH, "//*[contains(text(),'回标时间：')]//parent::div//input")  # 回标时间
    return_time_today = (By.XPATH, "//div[@x-placement='bottom-end']//button[text()='今天']")  # 回标时间--今天
    # 是否合作过
    whether_cooperation = (By.XPATH, "//*[contains(text(),'是否合作过：')]//parent::div//input")
    # 选择是否合作过
    whether_cooperation_choose = (By.XPATH, "//div[@x-placement='top-start']//li")
    meeting_CBO_business = (By.XPATH, "//input[@placeholder='选择一个商务总监']")  # 商务总监
    CBO_business_username = (By.XPATH, "//*[contains(text(),'用户名：')]//parent::div//input")  # 商务总监--用户名（输入搜索）
    choose_number_one = (By.XPATH, "//div[@class='el-table__fixed-body-wrapper']"
                                   "//input[@value='0']//ancestor::tr//div[text()='1']")  # 选择搜索到的第一条数据
    choose_CBO_name = (By.XPATH, "//td[@class='el-table_17_column_159  ']//span[text()='王勇']")  # 选择搜索到的总监姓名
    CBO_select_button = (By.XPATH, "//*[contains(text(),'商务总监')]//parent::div//span[text()='查询']")  # 查询按钮
    CBO_clear_button = (By.XPATH, "//*[contains(text(),'商务总监')]//parent::div//span[text()='清空']")  # 清空按钮
    CBO_confirm_button = (By.XPATH, "//*[contains(text(),'商务总监')]//parent::div//span[contains(text(),'确定')]")  # 确定按钮
    CBO_cancel_button = (By.XPATH, "//*[contains(text(),'商务总监')]//parent::div//span[contains(text(),'取消')]")  # 取消按钮
    meeting_business_manager = (By.XPATH, "//input[@placeholder='选择一个商务经理']")  # 商务经理
    choose_business_first_one = (By.XPATH, "//div[@class='el-table__fixed-body-wrapper']"
                                           "//span[@class='el-radio__input']//input")  # 选择第一个数据
    manager_select_button = (By.XPATH, "//*[contains(text(),'商务经理')]//parent::div//span[text()='查询']")  # 查询按钮
    manager_clear_button = (By.XPATH, "//*[contains(text(),'商务经理')]//parent::div//span[text()='清空']")  # 清空按钮
    manager_confirm_button = (By.XPATH, "//*[contains(text(),'商务经理')]"
                                        "//parent::div//span[contains(text(),'确定')]")  # 确定按钮
    manager_cancel_button = (By.XPATH, "//*[contains(text(),'商务经理')]//parent::div//span[contains(text(),'取消')]")  # 取消按钮
    choose_business_one = (By.XPATH, "//div[@class='el-table__fixed-body-wrapper']"
                                     "//input[@value='0']//ancestor::tr//div[text()='1']")  # 选择第一条数据
    choose_business_one1 = (By.XPATH, "//div[@class='el-table__fixed' and @style='width: 655px;']//"
                                      "tr[@class='el-table__row expanded']")  # 选择第一条数据
    business_progress = (By.XPATH, "//*[contains(text(),'商务进度')]//parent::div//input[@placeholder='请选择']")  # 商务进度
    business_progress_quotation1 = (By.XPATH, "//div[@x-placement='top-start']//li")  # 商务进度选择
    business_progress_quotation = (By.XPATH, "//span[text()='报价中']")  # 商务进度--报价中
    business_progress_tender = (By.XPATH, "//span[text()='投标中']")  # 商务进度--投标中
    business_progress_evaluating = (By.XPATH, "//span[text()='评标中']")  # 商务进度--评标中
    business_progress_calibration = (By.XPATH, "//span[text()='已定标']")  # 商务进度--已定标
    business_progress_outbid = (By.XPATH, "//span[text()='已落标']")  # 商务进度--已落标
    replenish_yes_or_no = (By.XPATH, "//*[contains(text(),'是否补充协议：')]//parent::div//input")  # 是否补充协议
    replenish_choose = (By.XPATH, "//div[@x-placement='top-start']//li")  # 选择是否补充协议
    replenish_yes = (By.XPATH, "//div[@x-placement='top-start']//span[text()='是']")  # 是否补充协议
    replenish_no = (By.XPATH, "//div[@x-placement='top-start']//span[text()='否']")  # 不是否补充协议
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

    # choose_customer_one = (By.XPATH, "//div[text()='1']")  # 选择第一条数据
    first_party_add = (By.XPATH, "//button//span[contains(text(),'新增')]")  # 新增甲方按钮
    record_communication = (By.XPATH, "//div[text()='沟通记录']")  # 沟通记录
    recorded_information = (By.XPATH, "//td[@class='el-table_3_column_14  ']//textarea[@placeholder='请填写记录信息']")  # 记录信息
    communication_upload_file = (By.XPATH, "//td[@class='el-table_3_column_15 is-center ']"
                                           "//input[@name='file']")  # 上传文件
    quotation_record = (By.XPATH, "//div[text()='报价记录']")  # 报价记录
    contract_particulars = (By.XPATH, "//div[text()='合同详情']")  # 合同详情
    invoice_information = (By.XPATH, "//div[text()='发票信息']")  # 发票信息
