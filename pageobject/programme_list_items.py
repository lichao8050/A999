# _*_ coding: utf-8 _*_
# @Time    : 2021/5/19 0019 22:13
# @Author  : Mr_Li
# @FileName: programme_list_items.py
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from time import sleep
from base.base_util import logger
from pageobject.login_page import LoginPage

logger.info('---执行项目--方案清单项目---')


class ProgrammeListItems(BasePage):
    """执行项目--方案清单项目"""

    project_process = (By.XPATH, "//span[text()='項目流程']")   # 项目流程
    project_process_soft = (By.XPATH, "//span[text()='軟裝事業部']")  # 軟裝事業部
    project_programme_list_items = (By.XPATH, "//div[@span='8']//button[contains(@class,'el')][3]")  # 方案清单项目

    project_search = (By.XPATH, "//span[text()='硬装']")  # 查询
    project_new_add = (By.XPATH, "//span[text()='硬装']")  # 新增
    project_clear = (By.XPATH, "//span[text()='硬装']")  # 清空
    Project_team = (By.XPATH, "//span[text()='硬装']")  # 所属项目组
    project_name = (By.XPATH, "//span[text()='硬装']")  # 项目名称
    project_content = (By.XPATH, "//span[text()='硬装']")  # 项目内容
    project_process_syb1 = (By.XPATH, "//span[text()='硬装']")  # 商务总监
    project_process_syb1 = (By.XPATH, "//span[text()='硬装']")  # 设计总监
    project_process_syb1 = (By.XPATH, "//span[text()='硬装']")  # 商务经理
    project_process_syb1 = (By.XPATH, "//span[text()='硬装']")  # 项目启动时间
    project_process_syb1 = (By.XPATH, "//span[text()='硬装']")  # 项目参与人员
    project_process_syb1 = (By.XPATH, "//span[text()='硬装']")  # 所属事业部：硬装


    # 点击新增按钮
    project_process_sy = (By.XPATH, "//div[@span='8']//button[contains(@class,'el')][5]")
    # 输入新增项目名称
    project_process_dw = (By.XPATH, "//input[@placeholder='城市+地产+项目名称+硬装设计/软装采购']")
    # 所属事业部：默认软装
    project_process_syb = (By.XPATH, "//div[3]/div/div/div/div/div/input[@placeholder='请选择']")
    # 所属事业部：硬装
    project_process_syb1 = (By.XPATH, "//span[text()='硬装']")  # 所属事业部：硬装
    # 项目地址省市选择
    project_process_dw1 = (
    By.XPATH, "//div[2]/div/div[1]/div[2]/div[1]//div[1]/div/div/div/div/div[1]/input[@placeholder='请选择']")
    # 项目地址选河北省
    project_process_dw2 = (By.XPATH, "//div[@x-placement='bottom-start']//span[text()='河北省']")
    # 项目地址市区选择
    project_process_dw3 = (By.XPATH, "//form/div[1]//div[2]//div[2]/div[1]//div[2]//div[1]/input")
    # 项目地址选择张家口市
    project_process_dw4 = (By.XPATH, "//div[@x-placement='bottom-start']//span[text()='张家口市']")
    project_process_dw5 = (By.XPATH, "//input[@placeholder='请输入详细地址信息']")
    # 输入合同金额
    project_process_dw6 = (By.XPATH, "//input[@placeholder='请输入合同金额']")
    # 选择客户来源
    project_process_dw7 = (By.XPATH, "//form/div[1]//div[2]/div/div[1]/div[3]/div[1]//input")
    # 客户来源：网上了解（微博、微信公众号）
    project_process_dw8 = (By.XPATH, "//div[@x-placement='bottom-start']//span[text()='网上了解（微博、微信公众号）']")
    # 客户来源：考察过相关项目慕名而来
    project_process_dw81 = (By.XPATH, "//div[@x-placement='bottom-start']//span[text()='考察过相关项目慕名而来']")
    # 是否公司软装
    project_process_dw9 = (By.XPATH, "//div[@placeholder='请选择' and @class='el-form-item is-required"
                                      "el-form-item--medium']/div[@class='el-form-item__content']//input["
                                      "@placeholder='请选择']")
    # 是否公司软装：是
    project_process_dw10 = (By.XPATH, "//div[@x-placement='bottom-start']//span[text()='是']")
    # 请输入整体设计风格
    project_process_dw11 = (By.XPATH, "//input[@placeholder='请输入整体设计风格']")
    # 法人主体选择框
    project_process_dw19 = (By.XPATH, "//form//div[5]/div[2]//input")
    # 法人主体：'矩阵纵横设计股份有限公司'
    project_process_dw191 = (By.XPATH, "//li[contains(text(),'矩阵纵横设计股份有限公司')][1]")
    # 法人主体：'矩阵纵横设计股份有限公司'
    project_process_dw192 = (By.XPATH, "//li[contains(text(),'深圳市释相艺术文化传播有限公司')][1]")
    # 矩阵纵横设计股份有限公司成都分公司
    project_process_dw193 = (By.XPATH, "//li[contains(text(),'矩阵纵横设计股份有限公司成都分公司')][1]")
    # 矩阵纵横（上海）设计咨询有限公司
    project_process_dw194 = (By.XPATH, "//li[contains(text(),'矩阵纵横（上海）设计咨询有限公司')][1]")
    # 请选择合同签订时间
    project_process_dw20 = (By.XPATH, "//input[@placeholder='请选择合同签订时间']")
    # 请选择合同签订时间：今天
    project_process_dw201 = (By.XPATH, "//button[text()='今天']")
    # 请选择项目开始时间
    project_process_dw21 = (By.XPATH, "//input[@placeholder='请选择项目开始时间']")
    # 请选择项目开始时间：昨天
    project_process_dw211 = (By.XPATH, "//div[@x-placement='bottom-end']//button[text()='昨天']")
    # 请选择预计完成时间
    project_process_dw22 = (By.XPATH, "//input[@placeholder='请选择预计完成时间']")
    # 请选择预计完成时间：今天
    project_process_dw221 = (By.XPATH, "//div[@x-placement='bottom-end']//button[text()='今天']")
    # 请选择施工图时间
    project_process_dw23 = (By.XPATH, "//input[@placeholder='请选择施工图时间']")
    # 请选择施工图时间：今天
    project_process_dw231 = (By.XPATH, "//div[@x-placement='bottom-end']//button[text()='今天']")
    # 请输入SAP编码
    project_process_dw24 = (By.XPATH, "//input[@placeholder='请输入SAP编码']")
    # 输入合作记录
    project_process_dw33 = (By.XPATH, "//textarea[@placeholder='请填写合作记录']")
    # 选择一个商务总监
    project_process_dw25 = (By.XPATH, "//input[@placeholder='选择一个商务总监']")
    # 点击搜索框输入搜索人名：王勇
    project_process_dw251 = (By.XPATH, "//form/div/div[1]/div/div/div/div/input")
    # 点击查询按钮
    project_process_dw252 = (By.XPATH, "//span[text()='查询']")
    # 点击王勇
    project_process_dw253 = (By.XPATH, "//div[@class='el-table__fixed']//span[text()='王勇']")
    # 点击确定按钮
    project_process_dw254 = (By.XPATH, "//div/div[3]/div/button[1]/span")
    # 选择一个商务经理
    project_process_dw26 = (By.XPATH, "//input[@placeholder='选择一个商务经理']")
    # 商务经理钮双双
    project_process_dw261 = (By.XPATH, "//div[@class='el-table__fixed']//span[text()='钮双双']")
    # 点击确定按钮
    project_process_dw262 = (By.XPATH, "//form//div[3]//div[2]/div/div[3]//span[contains(text(),'确定')]")
    # 选择一个合约负责人
    project_process_dw27 = (By.XPATH, "//input[@placeholder='选择一个合约负责人']")
    # 合约负责人：王紫凡
    project_process_dw271 = (By.XPATH, "//div[@class='el-table__fixed']//span[text()='王紫凡']")
    # 点击确定按钮
    project_process_dw272 = (By.XPATH, "//form//div[3]/div[1]/div/div/div/div[2]//span[contains(text(),'确定')]")
    # 选择商务进度
    project_process_dw28 = (By.XPATH, "//form//div[2]/div/div[3]/div[2]//input")
    # 商务进度：已收定金款
    project_process_dw281 = (By.XPATH, "//span[text()='已收定金款']")
    # 是否补充协议
    project_process_dw29 = (By.XPATH, "//form/div[1]//div[2]/div/div[4]//input")
    # 是补充协议
    project_process_dw291 = (By.XPATH, "//li[contains(@class,'hover')]//span[text()='是']")
    # 不是补充协议
    project_process_dw292 = (By.XPATH, "//div[@x-placement='top-start']//span[text()='否']")
    # 点击甲方信息
    project_process_dw30 = (By.XPATH, "//div[contains(text(),'甲方信息')]")
    # 点击签约甲方
    project_process_dw301 = (By.XPATH, "//div[@placeholder='请输入甲方公司名称']//input[@placeholder='请选择']")
    # 请输入客户编号
    project_process_dw302 = (By.XPATH, "//input[@placeholder='甲方单位选择']")
    # 请输入客户名称
    project_process_dw303 = (By.XPATH, "//input[@placeholder='请输入客户名称']")
    # 点击查询按钮
    project_process_dw304 = (By.XPATH, "//div[@span='8']//span[text()='查询']")
    # 选择CXD10254客户编号
    project_process_dw305 = (By.XPATH, "//div[@class='el-table__fixed']//span[text()='CXD10254']")
    # 点击'东升室内装修设计有限公司'
    # project_process_dw305 = (By.XPATH, "//div[@class='el-table__fixed']//span[text()='东升室内装修设计有限公司']")
    # 点击确定按钮
    project_process_dw306 = (By.XPATH, "//*[text()='确定']")
    # 点击保存
    project_process_dw31 = (By.XPATH, "//*[text()='保存']")
    # 预计签订时间
    project_process_dw32 = (By.XPATH, "//input[@placeholder='请选择预计签订时间']")
    # 选择预计签订时间
    project_process_dw321 = (By.XPATH, "//div[@x-placement='top-end']//button[text()='今天']")
    # 地产/非地产项目
    project_process_real_estate = (By.XPATH, "//form/div[1]/div/div/div/div[2]/div/div[1]/div[3]/div[9]"
                                              "/div/div/div/div[1]/input[@placeholder='请选择']")
    # 选择：地产项目
    project_process_yes_real_estate = (By.XPATH, "//li[1][contains(text(),'地产')]")
    # 选择：非地产项目
    project_process_no_real_estate = (By.XPATH, "//li[contains(text(),'非地产')]")

    def test_programme_list_items(self, username, password, value1, value2, value3, value4, value5, value6,
                         value7):
        login = LoginPage(self.driver)  # 登录
        login.login_erp(username, password)  # 输入用户名、密码

        sleep(1)
        logger.info('点击“商务流程”')
        self.click(ActionItemHard.project_process)  # 点击“商务流程”
        logger.info('点击“执行项目”')
        self.click(ActionItemHard.project_process_action_item)  # 点击“执行项目”
        sleep(1)
        logger.info('点击“新增”')
        self.click(ActionItemHard.project_process_sy)  # 点击“新增”
        logger.info('输入项目名称')
        self.send_ks(ActionItemHard.project_process_dw, value1)  # 输入项目名称
        logger.info('点击所属事业部')
        self.click(ActionItemHard.project_process_syb)  # 点击所属事业部
        self.click(ActionItemHard.project_process_syb1)  # 选择硬装
        self.click(ActionItemHard.project_process_dw1)  # 点击省/市
        sleep(1)
        self.click(ActionItemHard.project_process_dw2)  # 选择省/市
        self.click(ActionItemHard.project_process_dw3)  # 点击区域
        sleep(1)
        self.click(ActionItemHard.project_process_dw4)  # 选择区域
        self.send_ks(ActionItemHard.project_process_dw5, value2)  # 输入详细地址
        # self.clear_sz(ActionItemHard.project_process_dw6)   # 清空金额
        # self.send_ks(ActionItemHard.project_process_dw6, value3)   # 输入金额
        self.click(ActionItemHard.project_process_dw7)  # 点击客户来源
        sleep(1)
        self.click(ActionItemHard.project_process_dw81)  # 选择客户来源
        self.click(ActionItemHard.project_process_dw9)  # 点击公司软装
        sleep(1)
        self.click(ActionItemHard.project_process_dw10)  # 选择是否公司软装
        self.send_ks(ActionItemHard.project_process_dw11, value3)  # 输入设计风格
        self.click(ActionItemHard.project_process_dw20)  # 合同签订时间
        self.click(ActionItemHard.project_process_dw201)
        self.click(ActionItemHard.project_process_dw21)  # 项目开始时间
        sleep(1)
        self.click(ActionItemHard.project_process_dw211)
        self.click(ActionItemHard.project_process_dw22)  # 预计完成时间
        sleep(1)
        self.click(ActionItemHard.project_process_dw221)
        self.click(ActionItemHard.project_process_dw23)  # 施工图时间
        sleep(1)
        self.click(ActionItemHard.project_process_dw231)
        self.send_ks(ActionItemHard.project_process_dw24, value4)  # SAP编码
        self.click(ActionItemHard.project_process_real_estate)  # 点击地产/非地产
        sleep(1)
        self.click(ActionItemHard.project_process_yes_real_estate)  # 选择地产/非地产
        self.click(ActionItemHard.project_process_dw32)  # 预计签订时间
        sleep(1)
        self.click(ActionItemHard.project_process_dw321)
        self.click(ActionItemHard.project_process_dw19)  # 法人主体
        self.click(ActionItemHard.project_process_dw192)

        self.send_ks(ActionItemHard.project_process_dw33, value5)  # 合作记录
        self.click(ActionItemHard.project_process_dw25)
        self.send_ks(ActionItemHard.project_process_dw251, value6)  # 总监姓名
        sleep(1)
        self.click(ActionItemHard.project_process_dw252)  # 点击查询按钮
        self.click(ActionItemHard.project_process_dw253)
        self.click(ActionItemHard.project_process_dw254)  # 点击确定按钮
        self.click(ActionItemHard.project_process_dw26)  # 选择一个商务经理
        sleep(1)
        self.click(ActionItemHard.project_process_dw261)
        self.click(ActionItemHard.project_process_dw262)  # 点击确定按钮
        self.click(ActionItemHard.project_process_dw27)  # 选择一个合约负责人
        sleep(1)
        self.click(ActionItemHard.project_process_dw271)
        self.click(ActionItemHard.project_process_dw272)
        self.click(ActionItemHard.project_process_dw28)  # 选择商务进度
        self.click(ActionItemHard.project_process_dw281)
        self.click(ActionItemHard.project_process_dw29)  # 是否补充协议
        sleep(1)
        self.click(ActionItemHard.project_process_dw292)
        self.click(ActionItemHard.project_process_dw30)  # 点击甲方信息
        self.click(ActionItemHard.project_process_dw301)  # 点击签约甲方
        self.send_ks(ActionItemHard.project_process_dw303, value7)  # 客户名称
        sleep(1)
        self.click(ActionItemHard.project_process_dw304)  # 点击查询按钮
        self.click(ActionItemHard.project_process_dw305)  # 选择CXD10254客户编号
        self.click(ActionItemHard.project_process_dw306)  # 点击确定按钮
        self.click(ActionItemHard.project_process_dw31)  # 点击保存
