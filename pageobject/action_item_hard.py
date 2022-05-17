# _*_ coding: utf-8 _*_
# @Time    : 2021/5/19 0019 22:13
# @Author  : Mr_Li
# @FileName: action_item_soft.py
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from time import sleep
from base.base_util import logger
from pageobject.login_page import LoginPage

logger.info('---执行项目新增--硬装---')


class ActionItemHard(BasePage):
    """执行项目新增--硬装"""

    business_process = (By.XPATH, "//span[text()='商務流程']")
    business_process_action_item = (By.XPATH, "//span[text()='執行項目']")
    # 点击清空按钮
    business_process_action_item3 = (By.XPATH, "//div[@span='8']//button[3]")
    # 点击新增按钮
    business_process_sy = (By.XPATH, "//div[@span='8']//button[5]")
    # 输入新增项目名称
    business_process_dw = (By.XPATH, "//input[@placeholder='城市+地产+项目名称+硬装设计/软装采购']")
    # 所属事业部：默认软装
    business_process_syb = (By.XPATH, "//*[contains(text(),'所属事业部：')]//parent::div//input[@type='text']")
    # 所属事业部：硬装
    business_process_syb1 = (By.XPATH, "//span[text()='硬装']")
    # 项目地址省市选择
    business_process_dw1 = (
        By.XPATH, "//*[contains(text(),'项目地址：')]//parent::div//div[@class='region-picker']/div[1]//input")
    # 项目地址选河北省
    business_process_dw2 = (By.XPATH, "//*[@x-placement='bottom-start']//li")
    # 项目地址市区选择
    business_process_dw3 = (By.XPATH, "//*[contains(text(),'项目地址：')]//parent::div"
                                      "//div[@class='region-picker']/div[2]//input")
    # 项目地址选择张家口市
    business_process_dw4 = (By.XPATH, "//*[@x-placement='bottom-start']//li")
    # 输入详细地址信息
    business_process_dw5 = (By.XPATH, "//input[@placeholder='请输入详细地址信息']")
    # 选择客户来源
    business_process_dw7 = (By.XPATH, "//*[contains(text(),'客户来源：')]//parent::div//input")
    # 客户来源
    business_process_dw8 = (By.XPATH, "//div[@x-placement='bottom-start']//li")
    # 是否公司软装
    business_process_dw9 = (By.XPATH, "//*[contains(text(),'是否公司软装：')]//parent::div//input[@type='text']")
    # 是否公司软装：是
    business_process_dw10 = (By.XPATH, "//div[@x-placement='bottom-start']//li")
    # 请输入整体设计风格
    business_process_dw11 = (By.XPATH, "//input[@placeholder='请输入整体设计风格']")

    # 请选择合同收到时间
    business_process_dw200 = (By.XPATH, "//input[@placeholder='请选择合同收到时间']")
    # 请选择合同收到时间：今天
    business_process_dw2001 = (By.XPATH, "//button[text()='今天']")
    # 请选择预计完成时间
    business_process_dw21 = (By.XPATH, "//input[@placeholder='请选择预计完成时间']")
    # 请选择预计完成时间：昨天
    business_process_dw211 = (By.XPATH, "//div[@x-placement='bottom-end']//button[text()='昨天']")
    # 请选择施工图时间
    business_process_dw23 = (By.XPATH, "//input[@placeholder='请选择施工图时间']")
    # 请选择施工图时间：今天
    business_process_dw231 = (By.XPATH, "//div[@x-placement='bottom-end']//button[text()='今天']")
    # 地产/非地产项目
    business_process_real_estate = (By.XPATH, "//*[contains(text(),'地产/非地产项目：')]"
                                              "//parent::div//input[@type='text']")
    # 选择是否地产项目
    business_process_choose_estate = (By.XPATH, "//div[@x-placement='bottom-start']//li")
    # 请输入SAP编码
    business_process_dw24 = (By.XPATH, "//input[@placeholder='请输入SAP编码']")
    # 请选择合同文本时间
    business_process_dw20 = (By.XPATH, "//input[@placeholder='请选择合同文本时间']")
    # 请选择合同文本时间：今天
    business_process_dw201 = (By.XPATH, "//div[@x-placement='bottom-end']//button[text()='今天']")
    # 请选择预签订成时间
    business_process_dw22 = (By.XPATH, "//input[@placeholder='请选择预计签订时间']")
    # 请选择预计签订时间：今天
    business_process_dw221 = (By.XPATH, "//div[@x-placement='top-end']//button[text()='今天']")
    # 法人主体选择框
    business_process_dw19 = (By.XPATH, "//*[contains(text(),'法人主体：')]//parent::div//input[@type='text']")
    # 选择法人主体
    business_process_dw191 = (By.XPATH, "//div[@x-placement='bottom-start']//li")
    # 输入合作记录
    business_process_dw33 = (By.XPATH, "//textarea[@placeholder='请填写合作记录']")
    # 选择一个商务总监
    business_process_dw25 = (By.XPATH, "//input[@placeholder='选择一个商务总监']")
    # 点击搜索框输入搜索总监
    business_process_dw251 = (By.XPATH, "//*[contains(text(),'用户名：')]//parent::div//input")
    # 点击查询按钮
    business_process_dw252 = (By.XPATH, "//span[text()='查询']")
    # 点击第一个搜索到的选项
    business_process_dw253 = (By.XPATH, "//div[@class='el-table__fixed-body-wrapper']"
                                        "//input[@value='0']//ancestor::tr//div[text()='1']")
    # 点击确定按钮
    business_process_dw254 = (By.XPATH, "//*[contains(text(),'商务总监')]//parent::div//span[contains(text(),'确定')]")
    # 选择一个商务经理
    business_process_dw26 = (By.XPATH, "//input[@placeholder='选择一个商务经理']")
    # 选择列表中第一个人员
    business_process_dw261 = (By.XPATH, "//*[contains(text(),'商务经理：')]"
                                        "//parent::div//div[@class='el-table__fixed-body-wrapper']//input[@value='0']"
                                        "//ancestor::tr//div[text()='1']")
    # 点击确定按钮
    business_process_dw262 = (By.XPATH, "//*[contains(text(),'商务经理')]//parent::div//span[contains(text(),'确定')]")
    # 选择一个结算人员
    business_process_dw27 = (By.XPATH, "//input[@placeholder='选择一个结算人员']")
    # 选择列表中第一个人员
    business_process_dw271 = (By.XPATH, "//*[contains(text(),'结算人员：')]//parent::div"
                                        "//div[@class='el-table__fixed-body-wrapper']//input[@value='0']"
                                        "//ancestor::tr//div[text()='1']")
    # 点击确定按钮
    business_process_dw272 = (By.XPATH, "//*[contains(text(),'结算人员：')]//parent::div//span[contains(text(),'确定')]")
    # 点击商务进度
    business_process_dw28 = (By.XPATH, "//*[contains(text(),'商务进度：')]//parent::div//input")
    # 选择商务进度
    business_process_dw281 = (By.XPATH, "//div[@x-placement='top-start']//li")
    # 是否补充协议
    business_process_dw29 = (By.XPATH, "//*[contains(text(),'是否补充协议：')]//parent::div//input")
    # 选择是否补充协议
    business_process_dw291 = (By.XPATH, "//*[@x-placement='top-start']//li")
    # 点击甲方信息
    business_process_dw30 = (By.XPATH, "//div[contains(text(),'甲方信息')]")
    # 点击签约甲方
    business_process_dw301 = (By.XPATH, "//*[contains(text(),'签约甲方：')]//parent::div//input")
    # 请输入客户编号
    business_process_dw302 = (By.XPATH, "//input[@placeholder='请输入客户编号']")
    # 请输入客户名称
    business_process_dw303 = (By.XPATH, "//input[@placeholder='请输入客户名称']")
    # 点击查询按钮
    business_process_dw304 = (By.XPATH, "//*[contains(text(),'客户编号')]//ancestor::form//span[text()='查询']")
    # 选择列表中第一条数据
    business_process_dw305 = (By.XPATH, "//div[text()='行号']//ancestor::div[@style='width: 921px;']//div[text()='1']")
    # 点击确定按钮
    business_process_dw306 = (By.XPATH, "//*[text()='确定']")
    # 点击保存
    business_process_dw31 = (By.XPATH, "//*[text()='保存']")
    # 点击取消
    business_process_dw311 = (By.XPATH, "//div[@aria-label='提示']//span[text()='取消']")

    def test_action_hard(self, username, password, value1, value2, value3, value4, value5, value6,
                         value7, value11):
        login = LoginPage(self.driver)  # 登录
        login.login_erp(username, password)  # 输入用户名、密码

        sleep(1)
        logger.info('点击“商务流程”')
        self.click(ActionItemHard.business_process)  # 点击“商务流程”
        logger.info('点击“执行项目”')
        self.click(ActionItemHard.business_process_action_item)  # 点击“执行项目”
        sleep(1)
        logger.info('点击“新增”')
        self.click(ActionItemHard.business_process_sy)  # 点击“新增”
        logger.info('输入项目名称')
        self.send_ks(ActionItemHard.business_process_dw, value1)  # 输入项目名称
        logger.info('点击所属事业部')
        self.click(ActionItemHard.business_process_syb)  # 点击所属事业部
        logger.info('点击选择硬装')
        self.click(ActionItemHard.business_process_syb1)  # 选择硬装
        logger.info('点击省/市')
        self.click(ActionItemHard.business_process_dw1)  # 点击省/市
        logger.info('选择省/市')
        self.click_index(ActionItemHard.business_process_dw2, 0)  # 选择省/市
        logger.info('点击区域')
        self.click(ActionItemHard.business_process_dw3)  # 点击区域
        sleep(1)
        logger.info('选择区域')
        self.click_index(ActionItemHard.business_process_dw4, 0)  # 选择区域
        logger.info('输入详细地址')
        self.send_ks(ActionItemHard.business_process_dw5, value2)  # 输入详细地址
        logger.info('点击客户来源')
        self.click(ActionItemHard.business_process_dw7)  # 点击客户来源
        sleep(1)
        logger.info('选择客户来源')
        self.click_index(ActionItemHard.business_process_dw8, 0)  # 选择客户来源
        logger.info('点击公司软装')
        self.click(ActionItemHard.business_process_dw9)  # 点击公司软装
        sleep(1)
        logger.info('选择是否公司软装')
        self.click_index(ActionItemHard.business_process_dw10, 0)  # 选择是否公司软装
        logger.info('输入设计风格')
        self.send_ks(ActionItemHard.business_process_dw11, value3)  # 输入设计风格
        a = value11
        if a == 1:
            logger.info('点击合同收到时间')
            self.click(ActionItemHard.business_process_dw200)  # 点击合同收到时间
            logger.info('选择合同收到时间')
            self.click(ActionItemHard.business_process_dw2001)  # 选择合同收到时间
        else:
            pass
        logger.info('点击预计完成时间')
        self.click(ActionItemHard.business_process_dw21)
        sleep(0.5)
        logger.info('选择预计完成时间')
        self.click(ActionItemHard.business_process_dw211)
        logger.info('点击施工图时间')
        self.click(ActionItemHard.business_process_dw23)
        sleep(1)
        logger.info('选择施工图时间')
        self.click(ActionItemHard.business_process_dw231)
        logger.info('点击地产/非地产')
        self.click(ActionItemHard.business_process_real_estate)
        logger.info('选择地产/非地产')
        self.click_index(ActionItemHard.business_process_choose_estate, 0)
        logger.info('输入SAP编码')
        self.send_ks(ActionItemHard.business_process_dw24, value4)  # 输入SAP编码
        if a == 1:
            logger.info('点击合同文本时间')
            self.click(ActionItemHard.business_process_dw20)  # 点击合同文本时间
            logger.info('选择合同文本时间')
            self.click(ActionItemHard.business_process_dw201)  # 选择合同文本时间
        else:
            pass
        logger.info('点击预计签订时间')
        self.click(ActionItemHard.business_process_dw22)
        sleep(1)
        logger.info('选择预计签订时间')
        self.click(ActionItemHard.business_process_dw221)
        logger.info('点击法人主体')
        self.click(ActionItemHard.business_process_dw19)
        logger.info('选择法人主体')
        self.click(ActionItemHard.business_process_dw191)
        logger.info('填写合作记录')
        self.send_ks(ActionItemHard.business_process_dw33, value5)  # 填写合作记录
        logger.info('点击商务总监')
        self.click(ActionItemHard.business_process_dw25)
        logger.info('输入总监名字查找')
        self.send_ks(ActionItemHard.business_process_dw251, value6)  # 输入查找总监姓名
        logger.info('点击“查找”按钮')
        self.click(ActionItemHard.business_process_dw252)  # 点击查询按钮
        logger.info('选择搜索到的第一个人员')
        self.click(ActionItemHard.business_process_dw253)  # 选择搜索到的第一个人员
        logger.info('点击确定按钮')
        self.click(ActionItemHard.business_process_dw254)  # 点击确定按钮
        logger.info('点击商务经理')
        self.click(ActionItemHard.business_process_dw26)  # 选择一个商务经理
        sleep(1)
        logger.info('选择列表中第一个人员')
        self.click(ActionItemHard.business_process_dw261)  # 选择列表中第一个人员
        logger.info('点击确定按钮')
        self.click(ActionItemHard.business_process_dw262)  # 点击确定按钮
        logger.info('选择一个结算人员')
        self.click(ActionItemHard.business_process_dw27)  # 选择一个结算人员
        sleep(1)
        logger.info('选择列表中第一个人员')
        self.click(ActionItemHard.business_process_dw271)  # 选择列表中第一个人员
        logger.info('点击确定按钮')
        self.click(ActionItemHard.business_process_dw272)  # 点击确定按钮
        logger.info('点击商务进度')
        self.click(ActionItemHard.business_process_dw28)  # 点击商务进度
        sleep(1)
        logger.info('选择商务进度')
        self.click_index(ActionItemHard.business_process_dw281, 1)  # 选择商务进度
        logger.info('点击是否补充协议')
        self.click(ActionItemHard.business_process_dw29)  # 点击是否补充协议
        sleep(0.5)
        logger.info('选择是否补充协议')
        self.click_index(ActionItemHard.business_process_dw291, 1)  # 选择是否补充协议
        logger.info('点击甲方信息')
        self.click(ActionItemHard.business_process_dw30)  # 点击甲方信息
        logger.info('点击签约甲方')
        self.click(ActionItemHard.business_process_dw301)  # 点击签约甲方
        logger.info('输入客户编号')
        self.send_ks(ActionItemHard.business_process_dw303, value7)  # 输入客户编号
        logger.info('点击查询按钮')
        self.click(ActionItemHard.business_process_dw304)  # 点击查询按钮
        sleep(1)
        logger.info('选择第一条')
        self.click(ActionItemHard.business_process_dw305)  # 选择第一条
        logger.info('点击确定按钮')
        self.click(ActionItemHard.business_process_dw306)  # 点击确定按钮
        logger.info('点击保存')
        # self.click(ActionItemSoft.business_process_dw31)  # 点击保存
