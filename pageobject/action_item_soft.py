# _*_ coding: utf-8 _*_
# @Time    : 2021/5/19 0019 22:13
# @Author  : Mr_Li
# @FileName: action_item_soft.py
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from time import sleep
from base.base_util import logger
from pageobject.login_page import LoginPage
import traceback

logger.info('---执行项目新增--软装---')


class ActionItemSoft(BasePage):
    """执行项目新增--软装"""

    business_process = (By.XPATH, "//span[text()='商務流程']")
    business_process_action_item = (By.XPATH, "//span[text()='執行項目']")
    # 点击清空按钮
    business_process_action_item3 = (By.XPATH, "//div[@span='8']//button[contains(@class,'el')][3]")
    # 点击新增按钮
    business_process_sy = (By.XPATH, "//div[@span='8']//button[contains(@class,'el')][5]")
    # 输入新增项目名称
    business_process_dw = (By.XPATH, "//input[@placeholder='城市+地产+项目名称+硬装设计/软装采购']")
    # 所属事业部：默认软装
    business_process_sssyb = (By.XPATH, "//div[3]/div/div/div/div/div/input[@placeholder='请选择']")
    # 所属事业部：硬装
    business_process_sssyb1 = (By.XPATH, "//span[text()='硬装']")
    # 项目地址省市选择
    business_process_dw1 = (
    By.XPATH, "//div[2]/div/div[1]/div[2]/div[1]//div[1]/div/div/div/div/div[1]/input[@placeholder='请选择']")
    # 项目地址选河北省
    business_process_dw2 = (By.XPATH, "//div[@x-placement='bottom-start']//span[text()='河北省']")
    # 项目地址市区选择
    business_process_dw3 = (By.XPATH, "//form/div[1]//div[2]//div[2]/div[1]//div[2]//div[1]/input")
    # 项目地址选择张家口市
    business_process_dw4 = (By.XPATH, "//div[@x-placement='bottom-start']//span[text()='张家口市']")
    business_process_dw5 = (By.XPATH, "//input[@placeholder='请输入详细地址信息']")
    # 输入合同金额
    business_process_dw6 = (By.XPATH, "//input[@placeholder='请输入合同金额']")
    # 选择客户来源
    business_process_dw7 = (By.XPATH, "//form/div[1]//div[2]/div/div[1]/div[3]/div[1]//input")
    # 客户来源：网上了解（微博、微信公众号）
    business_process_dw8 = (By.XPATH, "//div[@x-placement='bottom-start']//span[text()='网上了解（微博、微信公众号）']")
    # 客户来源：考察过相关项目慕名而来
    business_process_dw81 = (By.XPATH, "//div[@x-placement='bottom-start']//span[text()='考察过相关项目慕名而来']")
    # 是否公司硬装
    business_process_dw9 = (By.XPATH, "//form//div[2]//div[1]/div[3]/div[2]//div/input")
    # 是否公司硬装：是
    business_process_dw10 = (By.XPATH, "//div[@x-placement='bottom-start']//span[text()='是']")
    # 硬装设计公司
    business_process_dw101 = (By.XPATH, "//input[@placeholder='请输入硬装设计公司']")
    # 请输入整体设计风格
    business_process_dw11 = (By.XPATH, "//input[@placeholder='请输入整体设计风格']")
    # 请输入甲方喜好
    business_process_dw12 = (By.XPATH, "//input[@placeholder='请输入甲方喜好']")
    # 请输入其他需求
    business_process_dw13 = (By.XPATH, "//input[@placeholder='请输入其他需求']")
    # 是否有清单模板
    business_process_dw14 = (By.XPATH, "//form/div[1]//div[2]//div[1]/div[5]/div[1]//input[@placeholder='请选择']")
    # 是否是否有清单模板：“是”选项
    business_process_dw15 = (By.XPATH, "//div[@x-placement='bottom-start']//span[text()='是']")
    # 是否是否有清单模板：“否”选项
    business_process_dw151 = (By.XPATH, "//div[@x-placement='bottom-start']//span[text()='否']")
    # 硬装方案满意
    business_process_dw16 = (By.XPATH, "//form/div[1]//div[2]//div[1]/div[5]/div[2]//input")
    # 硬装方案满意选择框
    business_process_dw17 = (By.XPATH, "//form//div[5]/div[2]//input")
    # 硬装方案满意:"是"
    business_process_dw18 = (By.XPATH, "//div[@x-placement='bottom-start']//span[text()='是']")
    # 硬装方案满意:"否"
    business_process_dw181 = (By.XPATH, "//div[@x-placement='bottom-start']//span[text()='否']")
    # 法人主体选择框
    business_process_dw19 = (By.XPATH, "//form//div[5]/div[3]//input")
    # 法人主体：'矩阵纵横设计股份有限公司'
    business_process_dw191 = (By.XPATH, "//li[contains(text(),'矩阵纵横设计股份有限公司')][1]")
    # 法人主体：'矩阵纵横设计股份有限公司'
    business_process_dw192 = (By.XPATH, "//li[contains(text(),'深圳市释相艺术文化传播有限公司')][1]")
    # 矩阵纵横设计股份有限公司成都分公司
    business_process_dw193 = (By.XPATH, "//li[contains(text(),'矩阵纵横设计股份有限公司成都分公司')][1]")
    # 矩阵纵横（上海）设计咨询有限公司
    business_process_dw194 = (By.XPATH, "//li[contains(text(),'矩阵纵横（上海）设计咨询有限公司')][1]")
    # 合同收到时间
    business_process_received_the_contract = (By.XPATH, "//input[@placeholder='请选择合同收到时间']")
    # 请选择合同收到时间：今天
    business_process_received_the_contract_today = (By.XPATH, "//button[text()='今天']")

    # 请选择合同签订时间
    business_process_dw20 = (By.XPATH, "//input[@placeholder='请选择合同签订时间']")
    # 请选择合同签订时间：今天
    business_process_dw201 = (By.XPATH, "//button[text()='今天']")
    # 请选择项目开始时间
    business_process_dw21 = (By.XPATH, "//input[@placeholder='请选择项目开始时间']")
    # 请选择项目开始时间：昨天
    business_process_dw211 = (By.XPATH, "//div[@x-placement='bottom-end']//button[text()='昨天']")
    # 请选择预计完成时间
    business_process_dw22 = (By.XPATH, "//input[@placeholder='请选择预计完成时间']")
    # 请选择预计完成时间：今天
    business_process_dw221 = (By.XPATH, "//div[@x-placement='bottom-end']//button[text()='今天']")
    # 请选择回标/摆场时间
    business_process_dw23 = (By.XPATH, "//input[@placeholder='请选择回标/摆场时间']")
    # 请选择回标/摆场时间：今天
    business_process_dw231 = (By.XPATH, "//div[@x-placement='top-end']//button[text()='今天']")
    # 地产/非地产项目
    business_process_whether_real_estate = (By.XPATH, "//*[contains(text(),'地产/非地产项目：')]"
                                                      "//parent::div//input[@placeholder='请选择']")
    # 是地产
    business_process_whether_real_estate_yes = (By.XPATH, "//li[1][contains(text(),'地产')]")
    # 非地产项目
    business_process_whether_real_estate_no = (By.XPATH, "//li[contains(text(),'非地产')]")
    # 预计签订时间
    business_process_dw32 = (By.XPATH, "//input[@placeholder='请选择预计签订时间']")
    # 选择预计签订时间
    business_process_dw321 = (By.XPATH, "//div[@x-placement='top-end']//button[text()='今天']")
    # 请输入SAP编码
    business_process_dw24 = (By.XPATH, "//input[@placeholder='请输入SAP编码']")
    # 合同文本时间
    business_process_contract_text_time = (By.XPATH, "//input[@placeholder='请选择合同文本时间']")
    # 选择合同文本时间：今天
    business_process_contract_text_time_today = (By.XPATH, "//div[@x-placement='top-end']//button[text()='今天']")
    # 输入合作记录
    business_process_dw33 = (By.XPATH, "//textarea[@placeholder='请填写合作记录']")
    # 填写软装质保周期
    business_process_soft_expiration_date = (By.XPATH, "//*[contains(text(),'软装质保周期：')]"
                                                       "//parent::div//input[@type='number']")
    # 选择一个商务总监
    business_process_dw25 = (By.XPATH, "//input[@placeholder='选择一个商务总监']")
    # 点击搜索框输入搜索人名：郑鸿晖
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
    # 选择商务进度
    business_process_dw28 = (By.XPATH, "//*[contains(text(),'商务进度：')]//parent::div//input")
    # 商务进度：已收方案深化阶段-尾款
    business_process_dw281 = (By.XPATH, "//div[@x-placement='top-start']//li//span[text()='已收委托函/中标通知书']")
    # 是否补充协议
    business_process_dw29 = (By.XPATH, "//*[contains(text(),'是否补充协议：')]//parent::div//input")
    # 是补充协议
    business_process_dw291 = (By.XPATH, "//li[contains(@class,'hover')]//span[text()='是']")
    # 不是补充协议
    business_process_dw292 = (By.XPATH, "//div[@x-placement='top-start']//span[text()='否']")
    # 点击甲方信息
    business_process_dw30 = (By.XPATH, "//div[contains(text(),'甲方信息')]")
    # 点击签约甲方
    business_process_dw301 = (By.XPATH, "//*[contains(text(),'签约甲方：')]//parent::div//input[@placeholder='请选择']")
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
    business_process_dw311 = (By.XPATH, "//div[@aria-label='提示']//span[text()='取消']")

    def test_action_soft(self, username, password, value1, value2, value3, value4, value5, value6,
                         value7, value8, value9, value10, value11):
        login = LoginPage(self.driver)  # 登录
        login.login_erp(username, password)  # 输入用户名、密码

        sleep(1)
        # self.click(ActionItemSoft.business_process_dw311)
        logger.info('点击“商务流程”')
        self.click(ActionItemSoft.business_process)  # 点击“商务流程”
        logger.info('点击“执行项目”')
        self.click(ActionItemSoft.business_process_action_item)  # 点击“执行项目”
        sleep(1)
        logger.info('点击“新增”按钮')
        self.click(ActionItemSoft.business_process_sy)  # 点击“新增”
        logger.info('输入项目名称')
        self.send_ks(ActionItemSoft.business_process_dw, value1)  # 输入项目名称
        logger.info('点击省/市')
        self.click(ActionItemSoft.business_process_dw1)  # 点击省/市
        sleep(1)
        logger.info('选择省/市')
        self.click(ActionItemSoft.business_process_dw2)  # 选择省/市
        logger.info('点击区域')
        self.click(ActionItemSoft.business_process_dw3)  # 点击区域
        sleep(1)
        logger.info('选择区域')
        self.click(ActionItemSoft.business_process_dw4)  # 选择区域
        logger.info('输入详细地址')
        self.send_ks(ActionItemSoft.business_process_dw5, value2)  # 输入详细地址
        logger.info('点击客户来源')
        self.click(ActionItemSoft.business_process_dw7)  # 点击客户来源
        sleep(1)
        logger.info('选择客户来源')
        self.click(ActionItemSoft.business_process_dw81)  # 选择客户来源
        logger.info('点击公司硬装')
        self.click(ActionItemSoft.business_process_dw9)  # 点击公司硬装
        sleep(1)
        logger.info('选择是否公司硬装')
        self.click(ActionItemSoft.business_process_dw10)  # 选择是否公司硬装
        logger.info('输入设计风格')
        self.send_ks(ActionItemSoft.business_process_dw11, value3)  # 输入设计风格
        logger.info('输入甲方喜好')
        self.send_ks(ActionItemSoft.business_process_dw12, value4)  # 输入甲方喜好
        logger.info('输入其它需求')
        self.send_ks(ActionItemSoft.business_process_dw13, value5)  # 输入其它需求
        logger.info('点击清单模板')
        self.click(ActionItemSoft.business_process_dw14)  # 点击清单模板
        logger.info('选择清单模板:"是"选项')
        self.click(ActionItemSoft.business_process_dw15)  # 选择清单模板:"是"选项
        logger.info('硬装方案满意')
        self.click(ActionItemSoft.business_process_dw17)  # 硬装方案满意
        sleep(1)
        logger.info('硬装方案满意：是')
        self.click(ActionItemSoft.business_process_dw18)
        logger.info('选择法人主体')
        self.click(ActionItemSoft.business_process_dw19)  # 法人主体
        logger.info('法人主体：矩阵纵横设计股份有限公司')
        self.click(ActionItemSoft.business_process_dw192)
        # logger.info('合同收到时间：')
        # self.click(ActionItemSoft.business_process_received_the_contract)  # 合同收到时间
        # logger.info('选择：合同收到时间：')
        # self.click(ActionItemSoft.business_process_received_the_contract_today)
        logger.info('项目开始时间')
        self.click(ActionItemSoft.business_process_dw21)  # 项目开始时间
        sleep(1)
        logger.info('选择：项目开始时间：')
        self.click(ActionItemSoft.business_process_dw211)
        logger.info('预计完成时间')
        self.click(ActionItemSoft.business_process_dw22)  # 预计完成时间
        sleep(1)
        logger.info('选择：预计完成时间：')
        self.click(ActionItemSoft.business_process_dw221)
        logger.info('回标/摆场时间：')
        self.click(ActionItemSoft.business_process_dw23)  # 回标/摆场时间
        sleep(1)
        logger.info('选择：回标/摆场时间：')
        self.click(ActionItemSoft.business_process_dw231)
        logger.info('地产/非地产项目')
        self.click(ActionItemSoft.business_process_whether_real_estate)  # 地产/非地产项目
        sleep(1)
        logger.info('选择：地产/非地产项目：是')
        self.click(ActionItemSoft.business_process_whether_real_estate_yes)
        logger.info('预计签订时间')
        self.click(ActionItemSoft.business_process_dw32)  # 预计签订时间
        sleep(1)
        logger.info('选择：预计签订时间：')
        self.click(ActionItemSoft.business_process_dw321)
        logger.info('输入SAP编码')
        self.send_ks(ActionItemSoft.business_process_dw24, value6)  # SAP编码
        # logger.info('合同文本时间')
        # self.click(ActionItemSoft.business_process_contract_text_time)  # 合同文本时间
        # sleep(1)
        # logger.info('选择：合同文本时间：')
        # self.click(ActionItemSoft.business_process_contract_text_time_today)
        logger.info('填写合作记录')
        self.send_ks(ActionItemSoft.business_process_dw33, value7)  # 合作记录
        list1 = [value8]
        for i in list1:
            if i == 1:
                logger.info('填写：软装质保周期')
                self.send_ks(ActionItemSoft.business_process_soft_expiration_date, value9)  # 软装质保周期
            else:
                pass
        logger.info('点击商务总监')
        self.click(ActionItemSoft.business_process_dw25)  # 点击商务总监
        logger.info('输入搜索的总监名字')
        self.send_ks(ActionItemSoft.business_process_dw251, value10)  # 输入搜索的总监姓名
        sleep(1)
        logger.info('点击查询按钮')
        self.click(ActionItemSoft.business_process_dw252)  # 点击查询按钮
        logger.info('选择搜索到的第一个人员')
        self.click(ActionItemSoft.business_process_dw253)  # 选择搜索到的第一个人员
        logger.info('点击确定按钮')
        self.click(ActionItemSoft.business_process_dw254)  # 点击确定按钮
        logger.info('点击商务经理')
        self.click(ActionItemSoft.business_process_dw26)  # 选择一个商务经理
        sleep(1)
        logger.info('选择列表中第一个人员')
        self.click(ActionItemSoft.business_process_dw261)  # 选择列表中第一个人员
        logger.info('点击确定按钮')
        self.click(ActionItemSoft.business_process_dw262)  # 点击确定按钮
        logger.info('选择一个结算人员')
        self.click(ActionItemSoft.business_process_dw27)  # 选择一个结算人员
        sleep(1)
        logger.info('选择列表中第一个人员')
        self.click(ActionItemSoft.business_process_dw271)  # 选择列表中第一个人员
        logger.info('点击确定按钮')
        self.click(ActionItemSoft.business_process_dw272)  # 点击确定按钮
        logger.info('选择商务进度')
        self.click(ActionItemSoft.business_process_dw28)  # 选择商务进度
        logger.info('已收委托函/中标通知书')
        self.click(ActionItemSoft.business_process_dw281)  # 已收委托函/中标通知书
        logger.info('是否补充协议')
        self.click(ActionItemSoft.business_process_dw29)  # 是否补充协议
        sleep(1)
        logger.info('是否补充协议：否')
        self.click(ActionItemSoft.business_process_dw292)  # 是否补充协议:否
        logger.info('点击甲方信息')
        self.click(ActionItemSoft.business_process_dw30)  # 点击甲方信息
        logger.info('点击签约甲方')
        self.click(ActionItemSoft.business_process_dw301)  # 点击签约甲方
        logger.info('输入客户编号')
        self.send_ks(ActionItemSoft.business_process_dw302, value11)  # 输入客户编号
        logger.info('点击查询按钮')
        self.click(ActionItemSoft.business_process_dw304)  # 点击查询按钮
        sleep(1)
        logger.info('选择第一条')
        self.click(ActionItemSoft.business_process_dw305)  # 选择第一条
        logger.info('点击确定按钮')
        self.click(ActionItemSoft.business_process_dw306)  # 点击确定按钮
        logger.info('点击保存')
        # self.click(ActionItemSoft.business_process_dw31)  # 点击保存


