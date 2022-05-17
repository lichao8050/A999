# _*_ coding: utf-8 _*_
# @Time    : 2021/5/19 0019 22:13
# @Author  : LiChao
# @FileName: yyshenpi_swht_page.py
from pywinauto.keyboard import send_keys
from pywinauto.mouse import click
from selenium.webdriver.common.by import By

from base.base_page import BasePage

from time import sleep

from pageobject.login_page import LoginPage


class ActionItem(BasePage):
    """页面元素"""
    sw_lc = (By.XPATH, "//*[@id='1260220714821226498']/div/span")
    yy_gl = (By.XPATH, "//span[text()='商務流程']")
    yy_sp = (By.XPATH, "//span[text()='執行項目']")
    yy_sy = (By.XPATH, "/html/body/section/div/section/section/main/div/div[2]/"
                       "div/div[3]/div/div[1]/form/div[2]/div[2]/div/div/button[4]")

    yy_dw = (By.XPATH, "//input[@placeholder='城市+地产+项目名称+硬装设计/软装采购']")
    yy_dw1 = (By.XPATH, "/html/body/section/div/section/section/main/div/div[2]/div/"
                        "form/div[1]/div/div/div/div[2]/div/div[1]/div[2]/div[1]"
                        "/div/div/div/div/div/div[1]/div/div/div/div/div[1]/input")
    yy_dw2 = (By.XPATH, "/html/body/section/div/section/section/main/div/div[2]/div/"
                        "form/div[1]/div/div/div/div[2]/div/div[1]/div[2]/div[1]/div/"
                        "div/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[1]/ul/li[4]")
    yy_dw3 = (By.XPATH, "/html/body/section/div/section/section/main/div/div[2]/div/"
                        "form/div[1]/div/div/div/div[2]/div/div[1]/div[2]/div[1]/"
                        "div/div/div/div/div/div[2]/div/div/div/div/div[1]/input")
    yy_dw4 = (By.XPATH, "/html/body/section/div/section/section/main/div/div[2]/div/"
                        "form/div[1]/div/div/div/div[2]/div/div[1]/div[2]/div[1]/div/"
                        "div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div[1]/ul/li[4]")
    yy_dw5 = (By.XPATH, "//input[@placeholder='请输入详细地址信息']")
    yy_dw6 = (By.XPATH, "//input[@placeholder='请输入合同金额']")
    yy_dw7 = (By.XPATH, "/html/body/section/div/section/section/main/div/div[2]/div/form/"
                        "div[1]/div/div/div/div[2]/div/div[1]/div[3]/div[1]/div/div/div/div/div/input")
    yy_dw8 = (By.XPATH, "/html/body/div[4]/div[1]/div[1]/ul/li[3]")
    yy_dw9 = (By.XPATH, "/html/body/section/div/section/section/main/div/div[2]/div/form/"
                        "div[1]/div/div/div/div[2]/div/div[1]/div[3]/div[2]/div/div/div/div/div/input")
    yy_dw10 = (By.XPATH, "/html/body/div[5]/div[1]/div[1]/ul/li[1]")
    yy_dw11 = (By.XPATH, "//input[@placeholder='请输入整体设计风格']")
    yy_dw12 = (By.XPATH, "//input[@placeholder='请输入甲方喜好']")
    yy_dw13 = (By.XPATH, "//input[@placeholder='请输入其他需求']")
    yy_dw14 = (By.XPATH, "/html/body/section/div/section/section/main/div"
                         "/div[2]/div/form/div[1]/div/div/div/div[2]/div"
                         "/div[1]/div[5]/div[1]/div/div/div/div/div/input")
    yy_dw15 = (By.XPATH, "/html/body/div[5]/div[1]/div[1]/ul/li[1]/span")
    yy_dw151 = (By.XPATH, "/html/body/div[7]/div[1]/div[1]/ul/li[1]")
    yy_dw152 = (By.XPATH, "/html/body/div[6]/div[1]/div[1]/ul/li[1]")
    yy_dw16 = (By.XPATH, "/html/body/section/div/section/section/main/div/div[2]/div/form/div[1]/"
                         "div/div/div/div[2]/div/div[1]/div[5]/div[2]/div/div/div/div/div/input")
    yy_dw17 = (By.XPATH, "/html/body/section/div/section/section/main/div/div[2]"
                         "/div/form/div[1]/div/div/div/div[2]/div/div[1]/div[5]/div[2]/div/div/div/div/div/input")
    yy_dw18 = (By.XPATH, "/html/body/div[7]/div[1]/div[1]/ul/li[1]/span")

    yy_dw19 = (By.XPATH, "/html/body/section/div/section/section/main/div"
                         "/div[2]/div/form/div[1]/div/div/div/div[2]/div"
                         "/div[1]/div[5]/div[3]/div/div/div/div[1]/input")

    yy_dw190 = (By.XPATH, "/html/body/div[1]/div[1]/div[1]/ul/li[1]")
    yy_dw191 = (By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[2]")
    yy_dw192 = (By.XPATH, "/html/body/div[3]/div[1]/div[1]/ul/li[2]")
    yy_dw193 = (By.XPATH, "/html/body/div[4]/div[1]/div[1]/ul/li[2]")
    yy_dw194 = (By.XPATH, "/html/body/div[5]/div[1]/div[1]/ul/li[2]")
    yy_dw195 = (By.XPATH, "/html/body/div[6]/div[1]/div[1]/ul/li[2]")
    yy_dw196 = (By.XPATH, "/html/body/div[7]/div[1]/div[1]/ul/li[2]")
    yy_dw197 = (By.XPATH, "/html/body/div[8]/div[1]/div[1]/ul/li[2]")
    yy_dw198 = (By.XPATH, "/html/body/div[9]/div[1]/div[1]/ul/li[2]")

    yy_dw20 = (By.XPATH, "//input[@placeholder='请选择合同签订时间']")
    yy_dw201 = (By.XPATH, "//button[text()='今天']")
    yy_dw21 = (By.XPATH, "//input[@placeholder='请选择项目开始时间']")
    yy_dw211 = (By.XPATH, "//div[@x-placement='top-end']//button[@aria-label='下个月']")
    yy_dw212 = (By.XPATH, "//div[@x-placement='top-end']//span[contains(text(),'15')]")
    yy_dw22 = (By.XPATH, "//input[@placeholder='请选择预计完成时间']")
    yy_dw221 = (By.XPATH, "//input[@placeholder='请选择合同签订时间']")
    yy_dw23 = (By.XPATH, "//input[@placeholder='请选择回标/摆场时间']")
    yy_dw231 = (By.XPATH, "//input[@placeholder='请选择合同签订时间']")
    yy_dw24 = (By.XPATH, "//input[@placeholder='请输入SAP编码']")

    yy_dw25 = (By.XPATH, "//input[@placeholder='选择一个商务总监']")
    yy_dw251 = (By.XPATH, "/html/body/section/div/section/section/main/"
                          "div/div[2]/div/form/div[1]/div/div/div/div[2]/div/div[2]"
                          "/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div/div[1]"
                          "/div[4]/div[2]/table/tbody/tr[3]/td[3]/div")
    yy_dw252 = (By.XPATH, "/html/body/section/div/section/section/main/div"
                          "/div[2]/div/form/div[1]/div/div/div/div[2]/div"
                          "/div[2]/div[2]/div/div/div/div[2]/div/div[3]/div/button[1]")

    yy_dw26 = (By.XPATH, "//input[@placeholder='选择一个商务经理']")
    yy_dw261 = (By.XPATH, "/html/body/section/div/section/section/main/div/div[2]/div"
                          "/form/div[1]/div/div/div/div[2]/div/div[2]/div[3]/div/div/div/div[2]"
                          "/div/div[2]/div[2]/div/div[1]/div[4]/div[2]/table/tbody/tr[2]/td[3]/div")
    yy_dw262 = (By.XPATH, "/html/body/section/div/section/section/main/div/div[2]/div/form/div[1]"
                          "/div/div/div/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div/div[3]/div/button[1]")
    yy_dw27 = (By.XPATH, "//input[@placeholder='选择一个合约负责人']")
    yy_dw271 = (By.XPATH, "/html/body/section/div/section/section/main/div/div[2]/div/form/div[1]/div"
                          "/div/div/div[2]/div/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[2]/div/"
                          "div[1]/div[4]/div[2]/table/tbody/tr[4]/td[3]/div")
    yy_dw272 = (By.XPATH, "/html/body/section/div/section/section/main/div/div[2]/div/form/div[1]"
                          "/div/div/div/div[2]/div/div[3]/div[1]/div/div/div/div[2]/div/div[3]/div/button[1]")

    yy_dw28 = (By.XPATH, "/html/body/section/div/section/section/main/div/div[2]/div/"
                         "form/div[1]/div/div/div/div[2]/div/div[3]/div[2]/div/div/div/div/div[1]/input")

    yy_dw281 = (By.XPATH, "/html/body/div[13]/div[1]/div[1]/ul/li[1]")

    yy_dw29 = (By.XPATH, "/html/body/section/div/section/section/main/div/div[2]/div/form/div[1]"
                         "/div/div/div/div[2]/div/div[4]/div/div/div/div/div/div/input")

    yy_dw291 = (By.XPATH, "/html/body/div[14]/div[1]/div[1]/ul/li[2]")

    yy_dw30 = (
    By.XPATH, "/html/body/section/div/section/section/main/div/div[2]/div/form/div[2]/div/div/div/div[1]/div")

    yy_dw301 = (By.XPATH, "/html/body/section/div/section/section/main/div/div[2]"
                          "/div/form/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div/div[2]/div/div/div[1]/div/div/input")
    yy_dw3011 = (By.XPATH,
                 "/html/body/div[15]/div/div[2]/div[2]/div/div[1]/div[4]/div[2]/table/tbody/tr[6]/td[1]/div/label/span[1]/span")
    # # 输入搜索客户单位名称
    # yy_dw302 = (By.XPATH, "//input[@placeholder='请输入客户名称']")
    # # 尝试点击搜索客户单位搜索按钮1
    # yy_dw303 = (By.XPATH, "/html/body/div[14]/div/div[2]/div[1]/form/div[2]/div/div/div/button[1]")
    # # 尝试点击搜索客户单位搜索按钮2
    # yy_dw3031 = (By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/form/div[2]/div/div/div/button[1]")
    # yy_dw3032 = (By.XPATH, "/html/body/div[4]/div/div[2]/div[1]/form/div[2]/div/div/div/button[1]")
    # # 尝试选择搜索选项1
    # yy_dw304 = (By.XPATH, "/html/body/div[3]/div/div[2]/div[2]/div/div[1]/div[4]/div[2]/table/tbody/tr/td[1]/div/label/span[1]/span")
    # # 尝试选择搜索选项2
    # yy_dw3041 = (By.XPATH,"/html/body/div[4]/div/div[2]/div[2]/div/div[1]/div[4]/div[2]/table/tbody/tr/td[1]/div/label/span[1]/span")
    # 搜索后点击确定
    yy_dw305 = (By.XPATH, "//*[text()='确定']")
    # 点击保存
    yy_dw36 = (By.XPATH, "//*[text()='保存']")

    def test_action_item(self, username, password, value1, value2, value3, value4, value5, value6,
                         value7, value8, value9, value10, value11, value12, value13):
        # 登录
        dl = LoginPage(self.driver)
        dl.logine_erp(username, password)

        sleep(1)
        # 点击“商务流程”
        self.click(ActionItem.yy_gl)
        # 点击“执行项目”
        self.click(ActionItem.yy_sp)
        sleep(1)
        # 点击“新增”
        self.click(ActionItem.yy_sy)
        sleep(2)
        self.click(ActionItem.yy_dw20)
        sleep(2)
        self.click(ActionItem.yy_dw201)
        self.click(ActionItem.yy_dw21)
        sleep(2)
        self.click(ActionItem.yy_dw211)
        sleep(2)
        self.click(ActionItem.yy_dw212)
        # self.click(ActionItem.yy_dw22)
        # self.click(ActionItem.yy_sy221)
        # self.click(ActionItem.yy_dw23)
        # self.click(ActionItem.yy_sy231)

        # # 输入项目名称
        # self.send_ks(ActionItem.yy_dw,value1)
        # # 点击省/市
        # self.click(ActionItem.yy_dw1)
        # sleep(1)
        # # 选择省/市
        # self.click(ActionItem.yy_dw2)
        # # 点击区域
        # self.click(ActionItem.yy_dw3)
        # sleep(1)
        # # 选择区域
        # self.click(ActionItem.yy_dw4)
        # # 输入详细地址
        # self.send_ks(ActionItem.yy_dw5,value2)
        # # 清空金额
        # self.clear_sz(ActionItem.yy_dw6)
        # # 输入金额
        # self.send_ks(ActionItem.yy_dw6,value3)
        # # 点击客户来源
        # self.click(ActionItem.yy_dw7)
        # sleep(1)
        # # 选择客户来源
        # self.click(ActionItem.yy_dw8)
        # # 点击公司硬装
        # self.click(ActionItem.yy_dw9)
        # sleep(1)
        # # 选择是否公司硬装
        # self.click(ActionItem.yy_dw10)
        # # 输入设计风格
        # self.send_ks(ActionItem.yy_dw11, value4)
        # # 输入甲方喜好
        # self.send_ks(ActionItem.yy_dw12, value5)
        # # 输入其它需求
        # self.send_ks(ActionItem.yy_dw13, value6)
        # # 点击清单模板
        # self.click(ActionItem.yy_dw14)
        # sleep(1)
        # # 选择清单模板
        # try:
        #         self.click(ActionItem.yy_dw15)
        # except:
        #         print("未找到元素")
        # try:
        #         self.click(ActionItem.yy_dw151)
        # except:
        #         print("未找到元素")
        # try:
        #         self.click(ActionItem.yy_dw152)
        # except:
        #         print("未找到元素")
        # sleep(1)
        # self.click(ActionItem.yy_dw16)
        # sleep(1)
        # self.click(ActionItem.yy_dw17)
        # self.click(ActionItem.yy_dw18)
        # self.click(ActionItem.yy_dw19)
        # try:
        #     self.click(ActionItem.yy_dw193)
        # except:
        #     print("未找到元素")
        # try:
        #     self.click(ActionItem.yy_dw196)
        # except:
        #     print("未找到元素")
        # try:
        #     self.click(ActionItem.yy_dw197)
        # except:
        #     print("未找到元素")
        # self.send_ks(ActionItem.yy_dw20,value7)
        # self.click(ActionItem.yy_dw21)
        # self.send_ks(ActionItem.yy_dw21,value8)
        # self.click(ActionItem.yy_dw22)
        # self.send_ks(ActionItem.yy_dw22,value9)
        # self.click(ActionItem.yy_dw23)
        # self.send_ks(ActionItem.yy_dw23,value10)
        # self.click(ActionItem.yy_dw24)
        # self.send_ks(ActionItem.yy_dw24,value11)
        # self.click(ActionItem.yy_dw25)
        # sleep(1)
        # self.click(ActionItem.yy_dw251)
        # self.click(ActionItem.yy_dw252)
        # self.click(ActionItem.yy_dw26)
        # sleep(1)
        # self.click(ActionItem.yy_dw261)
        # self.click(ActionItem.yy_dw262)
        # self.click(ActionItem.yy_dw27)
        # sleep(1)
        # self.click(ActionItem.yy_dw271)
        # self.click(ActionItem.yy_dw272)
        # self.click(ActionItem.yy_dw28)
        # self.click(ActionItem.yy_dw281)
        # self.click(ActionItem.yy_dw29)
        # self.click(ActionItem.yy_dw291)
        # self.click(ActionItem.yy_dw30)
        # self.click(ActionItem.yy_dw301)
        # self.click(ActionItem.yy_dw3011)
        # self.click(ActionItem.yy_dw305)
        # self.click(ActionItem.yy_dw36)
