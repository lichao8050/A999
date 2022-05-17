# _*_ coding: utf-8 _*_
# @Time    : 2021/5/19 0019 22:13
# @Author  : Mr_Li
# @FileName: hard_coordinate_project.py
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from time import sleep
from base.base_util import logger
from pageobject.login_page import LoginPage
from pageobject.system_dictionary_list import matrix

logger.info('---执行项目新增--硬装配合项目---')


class HardCoordinateProject(BasePage):
    """执行项目新增--硬装配合项目"""

    Real_Estate_Division = (By.XPATH, "//span[text()='地產事業部']")
    hard_coordinate_project = (By.XPATH, "//*[text()='硬装配合项目']")
    # 点击清空按钮
    hard_project_action_item3 = (By.XPATH, "//div[@span='8']//button[contains(@class,'el')][3]")
    # 点击新增按钮
    hard_project_add_button = (By.XPATH, "//i[@title='显示合同额']//parent::div//*[contains(text(),'新增')]")
    # 输入新增项目名称
    hard_project_name = (By.XPATH, "//*[contains(text(),'项目名称')]//parent::div//*[@placeholder='请输入']")
    # 项目地址省市选择
    hard_project_province = (
        By.XPATH, "//*[contains(text(),'项目地址')]//parent::div//*[contains(@style,'2px')]//*[@placeholder='请选择']")
    # 项目地址选河北省
    hard_project_province_choose = (By.XPATH, "//div[@x-placement='bottom-start']//span[text()='河北省']")

    # 项目地址市区选择
    hard_project_city = (
        By.XPATH, "//*[contains(text(),'项目地址')]//parent::div//*[contains(@style,'right: 0px')]//*[@placeholder='请选择']")
    # 项目地址选择张家口市
    hard_project_city_choose = (By.XPATH, "//div[@x-placement='bottom-start']//span[text()='张家口市']")
    # 输入项目详细地址
    hard_project_site = (By.XPATH, "//*[contains(text(),'项目地址')]//parent::div//*[@class='input-box']//*[@type='text']")
    # 项目联系人
    hard_project_contact = (By.XPATH, "//*[contains(text(),'项目联系人')]//parent::div//*[@placeholder='请输入']")
    # 电话号码
    hard_project_phone_number = (By.XPATH, "//*[contains(text(),'电话号码')]//parent::div//*[@placeholder='请输入']")
    # 商务总监
    hard_project_CBO_business = (By.XPATH, "//*[@placeholder='选择一个商务总监']")
    # 商务总监输入查找
    hard_project_CBO_business_select = (By.XPATH, "//*[contains(text(),'用户名')]//parent::div//input")
    # 商务总监查询按钮
    hard_project_CBO_business_select_button = (By.XPATH, "//span[text()='查询']")
    # 选择第一个查询结果
    hard_project_CBO_business_choose = (By.XPATH, "//div[contains(@style,'54px')]//div[text()='1']")
    #  商务总监确定按钮
    hard_project_CBO_business_yes_button = (
        By.XPATH, "//*[contains(text(),'商务总监')]//parent::div//span[contains(text(),'确定')]")
    # 商务经理
    hard_project_business_manager = (By.XPATH, "//*[@placeholder='选择一个商务经理']")
    # 商务经理输入查找
    hard_project_business_manager_select = (
        By.XPATH, "//div[contains(text(),'商务经理')]//ancestor::div[contains(@style,'15vh')]"
                  "//*[contains(text(),'用户名')]//parent::div//input")
    # 商务经理查询按钮
    hard_project_business_manager_select_button = (
        By.XPATH, "//div[contains(text(),'商务经理')]//ancestor::div[@role='dialog']//parent::div//span[text()='查询']")
    # 选择第一个查询结果
    hard_project_business_manager_choose = (By.XPATH, "//div[contains(@style,'54px')]//div[text()='1']")
    #  商务经理确定按钮
    hard_project_business_manager_yes_button = (
        By.XPATH, "//*[contains(text(),'商务经理')]//parent::div//span[contains(text(),'确定')]")
    # 预计开工日期
    hard_project_start_time = (By.XPATH, "//*[contains(text(),'预计开工日期')]//parent::div//input")
    # 今天
    choose_today_start = (By.XPATH, "//*[@x-placement='bottom-end']//button[text()='今天']")
    # 预计完工日期
    hard_project_end_time = (By.XPATH, "//*[contains(text(),'预计完工日期')]//parent::div//input")
    # 今天
    choose_today_end = (By.XPATH, "//*[@x-placement='bottom-end']//button[text()='今天']")
    # 合同金额
    hard_project_money = (By.XPATH, "//*[contains(text(),'合同金额')]//parent::div//input")
    # 所属公司
    hard_project_company = (By.XPATH, "//*[contains(text(),'所属公司')]//parent::div//input")
    # 深圳
    area_sz = (By.XPATH, "//span[text()='深圳']")
    # 项目小组
    hard_project_group = (By.XPATH, "//*[contains(text(),'项目小组')]//parent::div//input")
    # 项目小组输入查找
    hard_project_group_select = (
        By.XPATH, "//div[contains(text(),'硬装项目小组')]//ancestor::"
                  "div[contains(@style,'15vh')]//div[@class='input-box']//input")
    # 项目小组查询按钮
    hard_project_group_select_button = (
        By.XPATH, "//div[contains(text(),'硬装项目小组')]//ancestor::div[contains(@style,'15vh')]//span[text()='查询']")
    # 选择第一个查询结果
    hard_project_group_choose = (By.XPATH, "//div[contains(@style,'54px')]//div[text()='1']")
    #  项目小组确定按钮
    hard_project_group_yes_button = (
        By.XPATH, "//*[contains(text(),'项目小组')]//parent::div//span[contains(text(),'确定')]")
    # 设计总监
    hard_project_design_director = (By.XPATH, "//*[contains(text(),'设计总监')]//parent::div//input")
    # 设计总监输入查找
    hard_project_design_director_select = (
        By.XPATH, "//div[contains(text(),'设计总监')]//ancestor::"
                  "div[contains(@style,'15vh')]//div[@class='input-box']//input")
    # 设计总监查询按钮
    hard_project_design_director_select_button = (
        By.XPATH, "//div[contains(text(),'设计总监')]//ancestor::div[contains(@style,'15vh')]//span[text()='查询']")
    # 选择第一个查询结果
    hard_project_design_director_choose = (By.XPATH, "//div[contains(@style,'54px')]//div[text()='1']")
    #  设计总监确定按钮
    hard_project_design_director_yes_button = (
        By.XPATH, "//*[contains(text(),'设计总监')]//parent::div//span[contains(text(),'确定')]")
    # 项目经理
    hard_project_manager = (By.XPATH, "//*[contains(text(),'项目经理')]//parent::div//input")
    # 选第一个
    choose_number_manager = (By.XPATH, "//div[contains(@style,'54px')]//div[text()='1']")
    #  项目经理确定按钮
    hard_project_manager_yes_button = (
        By.XPATH, "//*[contains(text(),'项目经理')]//parent::div//span[contains(text(),'确定')]")
    # 业态类型
    hard_project_type = (By.XPATH, "//*[contains(text(),'业态类型')]//parent::div//input")
    # 一级类型：地产
    hard_project_type_real_estate = (By.XPATH, "//div[@x-placement='bottom-start']//span[text()='地产']")
    # 二级类型
    hard_project_next_type = (By.XPATH, "//*[contains(text(),'二级类型')]//parent::div//input")
    # 二级类型
    hard_project_next_type_five = (By.XPATH, "//div[@x-placement='bottom-start']//span[text()='批量精装(5套以上)']")

    # 户型明细
    hard_project_detail = (By.XPATH, "//*[contains(text(),'户型明细')]//parent::div//input")
    # 数量
    hard_project_quantity = (By.XPATH, "//*[contains(text(),'数量')]//parent::div//input")
    # 面积
    hard_project_area = (By.XPATH, "//*[contains(text(),'面积')]//parent::div//input")
    # 其他特殊要求
    hard_project_other_requirements = (By.XPATH, "//textarea[@placeholder='请输入内容']")
    # 投标项目系数
    hard_project_bid_point = (By.XPATH, "//*[contains(text(),'投标项目系数')]//parent::div//input")
    # 投标项目系数:0
    hard_project_bid_point_one = (By.XPATH, "//div[@x-placement='bottom-start']//span[text()='0']")
    # 投标项目系数:0.2
    hard_project_bid_point_tow = (By.XPATH, "//div[@x-placement='bottom-start']//li/span[text()='0.2']")
    # 优秀项目系数
    hard_project_excellent_point = (By.XPATH, "//*[contains(text(),'优秀项目系数')]//parent::div//input")
    # 优秀项目系数:0.56
    hard_project_excellent_point_one = (By.XPATH, "//div[@x-placement='bottom-start']//span[text()='0.56']")
    # 商务回访系数
    hard_project_callback_point = (By.XPATH, "//*[contains(text(),'商务回访系数')]//parent::div//input")
    # 商务回访系数:-0.3
    hard_project_callback_point_one = (By.XPATH, "//div[@x-placement='bottom-start']//span[text()='-0.3']")
    # 开拓项目系数
    hard_project_open_up_point = (By.XPATH, "//*[contains(text(),'开拓项目系数')]//parent::div//input")
    # 开拓项目系数:1
    hard_project_open_up_point_one = (By.XPATH, "//div[@x-placement='bottom-start']//span[text()='1']")
    # 项目类型系数
    hard_project_type_point = (By.XPATH, "//*[contains(text(),'项目类型系数')]//parent::div//input")
    # 项目类型系数:地产(1.0)
    hard_project_type_point_one = (By.XPATH, "//div[@x-placement='bottom-start']//span[text()='地产(1.0)']")
    # 其他修正系数
    hard_project_amendment_point = (By.XPATH, "//*[contains(text(),'其他修正系数')]//parent::div//input[@type='number']")

    # 其他修正系数说明
    hard_project_amendment_point_explain = (
        By.XPATH, "//*[contains(text(),'其他修正系数说明')]//parent::div//input[@type='text']")
    # 把控比例
    hard_project_control_proportion = (By.XPATH, "//*[contains(text(),'把控比例')]//parent::div//input")
    # 选择把控比例
    hard_project_control_proportion_one = (By.XPATH, "//div[@x-placement='bottom-start']//span[text()='0.4']")
    # 项目组得分比例
    hard_project_score_proportion = (By.XPATH, "//*[contains(text(),'项目组得分比例')]//parent::div//input")
    # 选择项目组得分比例
    hard_project_score_proportion_one = (By.XPATH, "//div[@x-placement='bottom-start']//span[text()='0.8']")
    # 项目成员添加
    hard_hard_project_add_member = (By.XPATH, "//span[text()='+点击选择']")
    # 选择项目成员
    hard_hard_project_add_member_add_one = (
        By.XPATH, "//div[contains(@style,'53px')]//tr[2]/td[2]//span[contains(text(),'选择')]")
    hard_hard_project_add_member_add_tow = (
        By.XPATH, "//div[contains(@style,'53px')]//tr[3]/td[2]//span[contains(text(),'选择')]")
    hard_hard_project_add_member_add_three = (
        By.XPATH, "//div[contains(@style,'53px')]//tr[4]/td[2]//span[contains(text(),'选择')]")
    # 项目成员确定
    hard_hard_project_add_member_yes_button = (By.XPATH, "//span[text()='确定']")
    # 保存
    hard_hard_project_save = (By.XPATH, "//span[text()='保存']")

    def test_hard_coordinate_project(self, username, password, value1, value2, value3, value4, value5, value6, value7,
                                     value8, value9, value10, value11, value12, value13, value14, value15):
        login = LoginPage(self.driver)  # 登录
        login.login_erp(username, password)  # 输入用户名、密码

        sleep(1)
        logger.info('点击“项目流程”')
        self.click(matrix.project_procedures)  # 点击“项目流程”
        logger.info('点击“地产事业部”')
        self.click(HardCoordinateProject.Real_Estate_Division)  # 点击“地产事业部”
        logger.info('点击“硬装配合项目”')
        self.click(HardCoordinateProject.hard_coordinate_project)  # 点击“硬装配合项目”
        logger.info('点击“新增”按钮')
        self.click(HardCoordinateProject.hard_project_add_button)  # 点击“新增”按钮
        sleep(2)
        logger.info('输入项目名称')
        self.send_ks(HardCoordinateProject.hard_project_name, value1)  # 输入项目名称
        logger.info('点击“省级”区域')
        self.click(HardCoordinateProject.hard_project_province)  # 点击“省级”区域
        sleep(1)
        logger.info('选择省')
        self.click(HardCoordinateProject.hard_project_province_choose)  # 选择省
        logger.info('点击“市级”区域')
        self.click(HardCoordinateProject.hard_project_city)  # 点击“市级”区域
        sleep(1)
        logger.info('选择市')
        self.click(HardCoordinateProject.hard_project_city_choose)  # 选择市
        logger.info('输入详细地址')
        self.send_ks(HardCoordinateProject.hard_project_site, value2)  # 输入详细地址

        logger.info('填写项目联系人')
        self.send_ks(HardCoordinateProject.hard_project_contact, value3)  # 填写项目联系人
        logger.info('填写联系人电话号码')
        self.send_ks(HardCoordinateProject.hard_project_phone_number, value4)  # 填写联系人电话号码
        logger.info('点击选择商务总监')
        self.click(HardCoordinateProject.hard_project_CBO_business)  # 点击选择商务总监
        logger.info('输入想要查找的总监名字')
        self.send_ks(HardCoordinateProject.hard_project_CBO_business_select, value5)  # 输入想要查找的总监名字
        logger.info('点击“查询”按钮')
        self.click(HardCoordinateProject.hard_project_CBO_business_select_button)  # 点击“查询”按钮
        logger.info('选择第一条结果')
        self.click(HardCoordinateProject.hard_project_CBO_business_choose)  # 选择第一条结果
        logger.info('点击“确定”按钮')
        self.click(HardCoordinateProject.hard_project_CBO_business_yes_button)  # 点击“确定”按钮

        logger.info('点击选择商务经理')
        self.click(HardCoordinateProject.hard_project_business_manager)  # 点击选择商务经理
        logger.info('输入想要查找的经理名字')
        self.send_ks(HardCoordinateProject.hard_project_business_manager_select, value6)  # 输入想要查找的经理名字
        sleep(1)
        logger.info('点击“查询”按钮')
        self.click(HardCoordinateProject.hard_project_business_manager_select_button)  # 点击“查询”按钮
        sleep(1)
        logger.info('选择第一条结果')
        self.click(HardCoordinateProject.hard_project_business_manager_choose)  # 选择第一条结果
        logger.info('点击“确定”按钮')
        self.click(HardCoordinateProject.hard_project_business_manager_yes_button)  # 点击“确定”按钮

        logger.info('点击预计开工日期')
        self.click(HardCoordinateProject.hard_project_start_time)  # 点击预计开工日期
        logger.info('选择开工时间')
        self.click(HardCoordinateProject.choose_today_start)  # 选择开工时间
        logger.info('点击预计完工日期')
        self.click(HardCoordinateProject.hard_project_end_time)  # 点击预计完工日期
        sleep(1)
        logger.info('选择完工时间')
        self.click(HardCoordinateProject.choose_today_end)  # 选择完工时间
        logger.info('输入合同金额')
        self.send_ks(HardCoordinateProject.hard_project_money, value7)  # 输入合同金额

        logger.info('点击所属公司')
        self.click(HardCoordinateProject.hard_project_company)  # 点击所属公司
        sleep(1)
        logger.info('选择所属公司')
        self.click(HardCoordinateProject.area_sz)  # 选择所属公司

        logger.info('点击项目小组')
        self.click(HardCoordinateProject.hard_project_group)  # 点击项目小组
        logger.info('输入想要查找的小组负责人名字')
        self.send_ks(HardCoordinateProject.hard_project_group_select, value8)  # 输入想要查找的小组负责人名字
        sleep(1)
        logger.info('点击“查询”按钮')
        self.click(HardCoordinateProject.hard_project_group_select_button)  # 点击“查询”按钮
        sleep(1)
        logger.info('选择第一条结果')
        self.click(HardCoordinateProject.hard_project_group_choose)  # 选择第一条结果
        logger.info('点击“确定”按钮')
        self.click(HardCoordinateProject.hard_project_group_yes_button)  # 点击“确定”按钮

        logger.info('点击设计总监')
        self.click(HardCoordinateProject.hard_project_design_director)  # 点击设计总监
        logger.info('输入想要查找的设计总监名字')
        self.send_ks(HardCoordinateProject.hard_project_design_director_select, value9)  # 输入想要查找的设计总监名字
        sleep(1)
        logger.info('点击“查询”按钮')
        self.click(HardCoordinateProject.hard_project_design_director_select_button)  # 点击“查询”按钮
        sleep(1)
        logger.info('选择第一条结果')
        self.click(HardCoordinateProject.hard_project_design_director_choose)  # 选择第一条结果
        logger.info('点击“确定”按钮')
        self.click(HardCoordinateProject.hard_project_design_director_yes_button)  # 点击“确定”按钮

        logger.info('点击项目经理')
        self.click(HardCoordinateProject.hard_project_manager)  # 点击项目经理
        sleep(1)
        logger.info('选择第一条结果')
        self.click(HardCoordinateProject.choose_number_manager)  # 选择第一条结果
        logger.info('点击“确定”按钮')
        self.click(HardCoordinateProject.hard_project_manager_yes_button)  # 点击“确定”按钮
        logger.info('点击业态类型')
        self.click(HardCoordinateProject.hard_project_type)  # 点击业态类型
        logger.info('选择业态类型')
        self.click(HardCoordinateProject.hard_project_type_real_estate)  # 选择业态类型
        logger.info('输入户型明细')
        self.send_ks(HardCoordinateProject.hard_project_detail, value10)  # 输入户型明细
        logger.info('输入数量')
        self.send_ks(HardCoordinateProject.hard_project_quantity, value11)  # 输入数量
        logger.info('输入面积')
        self.send_ks(HardCoordinateProject.hard_project_area, value12)  # 输入面积
        logger.info('输入其它要求')
        self.send_ks(HardCoordinateProject.hard_project_other_requirements, value13)  # 输入其它要求
        sleep(2)
        logger.info('鼠标向下滚动')
        self.mouse_wheel1_down()
        sleep(1)
        logger.info('点击投标系数')
        self.click(HardCoordinateProject.hard_project_bid_point)  # 点击投标系数
        logger.info('选择投标系数')
        self.click(HardCoordinateProject.hard_project_bid_point_tow)  # 选择投标系数
        logger.info('点击优秀系数')
        self.click(HardCoordinateProject.hard_project_excellent_point)  # 点击优秀系数
        sleep(1)
        logger.info('选择优秀系数')
        self.click(HardCoordinateProject.hard_project_excellent_point_one)  # 选择优秀系数
        logger.info('点击商务回访系数')
        self.click(HardCoordinateProject.hard_project_callback_point)  # 点击商务回访系数
        sleep(1)
        logger.info('选择商务回访系数')
        self.click(HardCoordinateProject.hard_project_callback_point_one)  # 选择商务回访系数
        logger.info('点击开拓项目系数')
        self.click(HardCoordinateProject.hard_project_open_up_point)  # 点击开拓项目系数
        sleep(1)
        logger.info('选择开拓项目系数')
        self.click(HardCoordinateProject.hard_project_open_up_point_one)  # 选择开拓项目系数
        logger.info('点击项目类型系数')
        self.click(HardCoordinateProject.hard_project_type_point)  # 点击项目类型系数
        sleep(1)
        logger.info('选择项目类型系数')
        self.click(HardCoordinateProject.hard_project_type_point_one)  # 选择项目类型系数
        logger.info('清空其它修正系数')
        self.clear_sz(HardCoordinateProject.hard_project_amendment_point)  # 清空其它修正系数
        logger.info('输入其它修正系数')
        self.send_ks(HardCoordinateProject.hard_project_amendment_point, value14)  # 输入其它修正系数
        logger.info('点击把控比例')
        self.click(HardCoordinateProject.hard_project_control_proportion)  # 点击把控比例
        sleep(1)
        logger.info('选择把控比例')
        self.click(HardCoordinateProject.hard_project_control_proportion_one)  # 选择把控比例
        logger.info('点击项目组得分比例')
        self.click(HardCoordinateProject.hard_project_score_proportion)  # 点击项目组得分比例
        sleep(1)
        logger.info('选择项目组得分比例')
        self.click(HardCoordinateProject.hard_project_score_proportion_one)  # 选择项目组得分比例
        logger.info('点击选择项目成员')
        self.click(HardCoordinateProject.hard_hard_project_add_member)  # 点击选择项目成员
        sleep(1)
        logger.info('点击选择项目成员1')
        self.click(HardCoordinateProject.hard_hard_project_add_member_add_one)  # 点击选择项目成员1
        logger.info('点击选择项目成员2')
        self.click(HardCoordinateProject.hard_hard_project_add_member_add_tow)  # 点击选择项目成员2
        logger.info('点击选择项目成员3')
        self.click(HardCoordinateProject.hard_hard_project_add_member_add_three)  # 点击选择项目成员3
        logger.info('点击确定')
        self.click(HardCoordinateProject.hard_hard_project_add_member_yes_button)  # 点击确定
        logger.info('点击保存')
        self.click(HardCoordinateProject.hard_hard_project_save)  # 点击保存

