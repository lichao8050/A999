# _*_ coding: utf-8 _*_
# @Time    : 2021/5/19 0019 22:13
# @Author  : Mr_Li
# @FileName: soft_business_division_page.py
from selenium.webdriver.common.by import By


class SoftBusinessDivisionPage:
    """软装执行项目页面"""

    # 软装事业部
    soft_decoration_Division = (By.XPATH, "//span[text()='软装事業部']")
    # 概念配合项目
    concept_matching_project = (By.XPATH, "//div[text()='概念配合项目']")
    # 方案+清单配合项目
    list_matching_project = (By.XPATH, "//div[text()='方案+清单配合项目']")
    # 执行项目
    action_project = (By.XPATH, "//div[text()='执行项目']")
    # 归档项目
    pigeonhole_project = (By.XPATH, "//div[text()='归档项目']")
    # 概念配合项目查询按钮
    concept_matching_select_button = (By.XPATH, "//div[@id='pane-first']//span[text()='查询']")
    # 概念配合项目新增按钮
    concept_matching_new_add_button = (By.XPATH, "//div[@id='pane-first']//button//span[contains(text(),'新增')]")
    # 概念配合项目清空按钮
    concept_matching_clear_button = (By.XPATH, "//div[@id='pane-first']//button//span[contains(text(),'清空')]")
    # 方案+清单配合项目查询按钮
    list_matching_select_button = (By.XPATH, "//div[@id='pane-second']//span[text()='查询']")
    # 方案+清单配合项目新增按钮
    list_matching_new_add_button = (By.XPATH, "//div[@id='pane-second']//button//span[contains(text(),'新增')]")
    # 方案+清单配合项目清空按钮
    list_matching_clear_button = (By.XPATH, "//div[@id='pane-second']//button//span[contains(text(),'清空')]")
    # 方案+清单配合项目显示合同额按钮
    list_matching_show_money_button = (By.XPATH, "//div[@id='pane-second']//i[@title='显示合同额']")
    # 方案+清单配合项目隐藏合同额按钮
    list_matching_close_money_button = (By.XPATH, "//div[@id='pane-second']//i[@title='隐藏合同额']")
    # 执行项目查询按钮
    action_select_button = (By.XPATH, "//div[@id='pane-third']//span[text()='查询']")
    # 执行项目新增按钮
    action_new_add_button = (By.XPATH, "//div[@id='pane-third']//button//span[contains(text(),'新增')]")
    # 执行项目清空按钮
    action_clear_button = (By.XPATH, "//div[@id='pane-third']//button//span[contains(text(),'清空')]")
    # 方案+清单配合项目显示合同额按钮
    action__show_money_button = (By.XPATH, "//div[@id='pane-third']//i[@title='显示合同额']")
    # 方案+清单配合项目隐藏合同额按钮
    action_close_money_button = (By.XPATH, "//div[@id='pane-third']//i[@title='隐藏合同额']")
    # 归档项目查询按钮
    pigeonhole_select_button = (By.XPATH, "//div[@id='pane-four']//span[text()='查询']")
    # 归档项目新增按钮
    pigeonhole_new_add_button = (By.XPATH, "//div[@id='pane-four']//button//span[contains(text(),'新增')]")
    # 归档项目清空按钮
    pigeonhole_clear_button = (By.XPATH, "//div[@id='pane-four']//button//span[contains(text(),'清空')]")
    # 方案+清单配合项目显示合同额按钮
    pigeonhole_show_money_button = (By.XPATH, "//div[@id='pane-four']//i[@title='显示合同额']")
    # 方案+清单配合项目隐藏合同额按钮
    pigeonhole_close_money_button = (By.XPATH, "//div[@id='pane-four']//i[@title='隐藏合同额']")
    # 一键收起按钮
    pack_up = (By.XPATH, "//div[@id='pane-third']//span[text()='一键收起']")
    # 导出文件
    export_file = (By.XPATH, "//div[@id='pane-third']//span[text()='导出']")
    # 更多查询按钮
    more_select_button = (By.XPATH, "//div[@id='pane-third']//span[text()='更多查询']")

    '''方案清单项目新增页面'''
    # 保存按钮
    list_matching_project_save = (By.XPATH, "//span[text()='保存']")
    # 清空按钮
    list_matching_project_cleat = (By.XPATH, "//div[contains(@style,'-5px;')]//span[text()='清空']")
    # 方案清单项目
    list_matching_project_choose = (By.XPATH, "//div[text()='方案清单项目新增']")
    # 保存按钮
    save_button = (By.XPATH, "//span[text()='保存']")
    # 清空按钮
    clear_button = (By.XPATH, "//span[text()='清空']")
    # 项目名称
    project_name = (By.XPATH, "//*[contains(text(),'项目名称')]//parent::div//input")
    # 商务总监
    CBO_business = (By.XPATH, "//*[@placeholder='选择一个商务总监']")
    # 商务总监输入查找
    CBO_business_select = (By.XPATH, "//*[contains(text(),'用户名')]//parent::div//input")
    # 商务总监查询按钮
    CBO_business_select_button = (By.XPATH, "//span[text()='查询']")
    # 商务总监清空按钮
    CBO_business_clear_button = (By.XPATH, "//span[text()='查询']//following::button//span[text()='清空']")
    # 选择第一个查询结果
    CBO_business_choose = (By.XPATH, "//div[contains(@style,'54px')]//div[text()='1']")
    #  商务总监确定按钮
    CBO_business_yes_button = (
        By.XPATH, "//*[contains(text(),'商务总监')]//parent::div//span[contains(text(),'确定')]")
    #  商务总监取消按钮
    CBO_business_no_button = (
        By.XPATH, "//*[contains(text(),'商务总监')]//parent::div//span[contains(text(),'取消')]")
    # 商务经理
    business_manager = (By.XPATH, "//*[@placeholder='选择一个商务经理']")
    # 商务经理输入查找
    business_manager_select = (
        By.XPATH, "//div[contains(text(),'商务经理')]//ancestor::div[contains(@style,'15vh')]"
                  "//*[contains(text(),'用户名')]//parent::div//input")
    # 商务经理查询按钮
    business_manager_select_button = (
        By.XPATH, "//div[contains(text(),'商务经理')]//ancestor::div[@role='dialog']//parent::div//span[text()='查询']")
    # 选择第一个查询结果
    business_manager_choose = (By.XPATH, "//div[contains(@style,'54px')]//div[text()='1']")
    #  商务经理确定按钮
    business_manager_yes_button = (
        By.XPATH, "//*[contains(text(),'商务经理')]//parent::div//span[contains(text(),'确定')]")
    #  商务经理取消按钮
    business_manager_no_button = (
        By.XPATH, "//*[contains(text(),'商务经理')]//parent::div//span[contains(text(),'取消')]")
    # 是否公司硬装：
    whether_company_soft = (By.XPATH, "//*[contains(text(),'是否公司硬装：')]//parent::div//input")
    # 选择是否公司软装
    whether_company_soft_choose = (By.XPATH, "//div[@x-placement='bottom-start']//li")
    # 硬装设计师
    hard_stylist = (By.XPATH, "//*[contains(text(),'硬装设计师')]//parent::div//input")
    # 选择硬装设计师
    hard_stylist_choose = (By.XPATH, "//div[@x-placement='bottom-start']//li")
    # 开始时间：
    start_time = (By.XPATH, "//*[contains(text(),'开始时间：')]//parent::div//input")
    # 预计完成时间：
    end_time = (By.XPATH, "//*[contains(text(),'预计完成时间：')]//parent::div//input")

    # 项目小组
    project_group = (By.XPATH, "//*[text()='项目小组']//parent::div"
                               "//div[@class='input-box']//input[@placeholder='请选择']")
    # 项目小组确定按钮
    project_group_confirm = (By.XPATH, "//*[contains(text(),'项目小组')]//parent::div//*[contains(text(),'确定')]")
    # 项目小组取消按钮
    project_group_cancel = (By.XPATH, "//*[contains(text(),'项目小组')]//parent::div//*[contains(text(),'取消')]")
    # 项目小组查询按钮
    project_group_select = (By.XPATH, "//*[contains(text(),'项目小组')]//parent::div//*[contains(text(),'查询')]")
    # 项目小组清空按钮
    project_group_clear = (By.XPATH, "//*[contains(text(),'项目小组')]//parent::div//*[contains(text(),'清空')]")
    # 设计总监
    design_director = (By.XPATH, "//*[contains(text(),'设计总监')]//parent::div//input")
    # 设计总监确定按钮
    design_director_confirm = (By.XPATH, "//*[contains(text(),'设计总监')]//parent::div//*[contains(text(),'确定')]")
    # 设计总监取消按钮
    design_director_cancel = (By.XPATH, "//*[contains(text(),'设计总监')]//parent::div//*[contains(text(),'取消')]")
    # 项目经理
    project_manager = (By.XPATH, "//*[contains(text(),'项目经理')]//parent::div//input")
    # 项目经理确定按钮
    project_manager_confirm = (By.XPATH, "//*[contains(text(),'项目经理')]//parent::div//*[contains(text(),'确定')]")
    # 项目经理取消按钮
    project_manager_cancel = (By.XPATH, "//*[contains(text(),'项目经理')]//parent::div//*[contains(text(),'取消')]")
    # 项目经理查询按钮
    project_manager_select = (By.XPATH, "//*[contains(text(),'项目经理')]//parent::div//*[contains(text(),'查询')]")
    # 项目经理清空按钮
    project_manager_clear = (By.XPATH, "//*[contains(text(),'项目经理')]//parent::div//*[contains(text(),'清空')]")
    # 业态类型
    formats_type = (By.XPATH, "//*[contains(text(),'业态类型')]//parent::div//input")
    # 选择业态类型
    formats_type_choose = (By.XPATH, "//span[text()='酒店']")
    # 选择业态类型
    formats_type_choose1 = (By.XPATH, "//span[text()='高端私宅']")
    # 二级类型
    formats_type_first = (By.XPATH, "//*[contains(text(),'二级类型')]//parent::div//input")
    # 选择二级类型
    formats_type_first_choose = (By.XPATH, "//div[@x-placement='bottom-start']//li")
    # 户型明细
    family_breakdown = (By.XPATH, "//*[contains(text(),'户型明细')]//parent::div//input")
    # 面积
    area = (By.XPATH, "//*[contains(text(),'面积')]//parent::div//input")
    # 合同金额
    contract_amount = (By.XPATH, "//*[contains(text(),'合同金额')]//parent::div//input")
    # 开拓项目系数
    expand_coefficient = (By.XPATH, "//*[contains(text(),'开拓项目系数')]//parent::div//input")
    # 开拓项目系数选择
    expand_coefficient_choose = (By.XPATH, "//div[@x-placement='top-start']//li")
    # 上传钉钉审批记录
    check_record = (By.XPATH, "//*[contains(text(),'上传钉钉审批记录')]//parent::div//input")
    # 其他修正系数
    amendment_other = (By.XPATH, "//*[contains(text(),'其他修正系数')]//parent::div//input[@placeholder='其他修正系数']")
    # 其他修正系数说明
    amendment_other_explain = (By.XPATH, "//*[contains(text(),'合同金额')]//parent::div//input")
    # 把控比例
    control_proportion = (By.XPATH, "//*[contains(text(),'把控比例')]//parent::div//input")
    # 选择把控比例:0
    control_proportion_choose = (By.XPATH, "//div[@x-placement='bottom-start']//span[text()='0']")
    # 选择把控比例:0.2
    control_proportion_choose1 = (By.XPATH, "//div[@x-placement='bottom-start']//span[text()='0.2']")
    # 项目组得分比例
    score_proportion = (By.XPATH, "//*[contains(text(),'项目组得分比例')]//parent::div//input")
    # 选择项目组得分比例
    score_proportion_choose = (By.XPATH, "//div[@x-placement='top-start']//li")
    # 添加项目成员
    add_project_member = (By.XPATH, "//span[text()='+点击选择']")

    # 选择项目成员
    soft_soft_project_add_member_add_one = (By.XPATH, "//div[contains(@style,'53px')]"
                                                      "//tr[2]/td[2]//span[contains(text(),'选择')]")
    soft_soft_project_add_member_add_tow = (By.XPATH, "//div[contains(@style,'53px')]"
                                                      "//tr[3]/td[2]//span[contains(text(),'选择')]")
    soft_soft_project_add_member_add_three = (By.XPATH, "//div[contains(@style,'53px')]"
                                                        "//tr[4]/td[2]//span[contains(text(),'选择')]")
    # 项目成员确定
    soft_soft_project_add_member_yes_button = (By.XPATH, "//span[text()='确定']")
    # 项目保存成功
    list_matching_project_save_success = (By.XPATH, "//*[text()='保存成功']")
