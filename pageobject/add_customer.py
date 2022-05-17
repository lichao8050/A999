# _*_ coding: utf-8 _*_
# @Time    : 2021/5/13 0013 23:06
# @Author  : Mr_Li
# @FileName: add_customer.py
# CMR管理-我的客户-新增页面

from time import sleep
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from pageobject.login_page import LoginPage


class AddCustomer(BasePage):
    """新增客户"""

    # 页面元素
    cmr_manager = (By.XPATH, "//span[text()='CRM管理']")
    my_kh = (By.XPATH, "//span[text()='我的客戶']")
    cmr_xh = (By.XPATH, "//button/span[contains(text(),'新增')]")
    xz_mc = (By.XPATH, "//input[@placeholder='举例：龙湖、旭辉（不加地区/地产/集团等字眼）']")
    xz_dw = (By.XPATH, "//input[@placeholder='请输入客户单位']")
    jz_qy = (By.XPATH, "//form/div[1]/div[3]//div[1]/div/div/div/div/div[1]/input")
    jz_qy1 = (By.XPATH, "//span[text()='江苏省']")
    # 选择市区
    jz_qy2 = (By.XPATH, "//form/div[1]/div[3]//div[2]//input[@placeholder='请选择']")
    # 点击连云港市
    jz_qy21 = (By.XPATH, "//span[text()='连云港市']")
    qy_fzr = (By.XPATH, "//input[@placeholder='选择一个区域负责人']")
    # 用户名输入框:钟小乐
    cz_fzr = (By.XPATH, "//form/div/div[1]//input")
    # 点击查询按钮
    dj_qd1 = (By.XPATH, "//span[text()='查询']")
    # 点击搜索出来的用户
    xz_kh = (By.XPATH, "//div[@class='el-table__fixed-body-wrapper']//span[text()='钟小乐']")
    # 点击确定
    dj_qd2 = (By.XPATH, "//span[contains(text(),'确定')]")
    # 点击客户性质
    dj_zwf = (By.XPATH, "//form//div[5]/div[1]//input")
    # 选择国企非战略
    dj_qd = (By.XPATH, "//span[text()='国企非战略']")
    # 点击客户等级
    kh_xz = (By.XPATH, "//form//div[5]/div[2]//input")
    # 选择D级
    kh_xz1 = (By.XPATH, "//span[text()='D']")
    # 点击增加联系人按钮
    bz_lxr = (By.XPATH, "//i[@class='el-icon-plus']")
    # 输入纳税识别号
    bz_xx = (By.XPATH, "//input[@placeholder='请输入纳税识别号']")
    # 甲方注册电话
    bz_dh = (By.XPATH, "//input[@placeholder='请输入甲方注册电话']")
    # 开户行名称
    bz_khh = (By.XPATH, "//input[@placeholder='请输入开户行名称']")
    # 开户行账号
    bz_zh = (By.XPATH, "//input[@placeholder='请输入开户行账号']")
    # 甲方注册地址
    bz_dz = (By.XPATH, "//input[@placeholder='请输入甲方注册地址']")
    # 发票备注
    bz_bz = (By.XPATH, "//textarea[@placeholder='请填写发票备注']")
    tx_xm = (By.XPATH, "//input[@placeholder='请填写联系人姓名'][1]")
    tx_dh = (By.XPATH, "//input[@placeholder='请填写联系电话'][1]")
    tx_dz = (By.XPATH, "//input[@placeholder='请填写联系地址'][1]")
    # 联系人类型
    tx_lx = (By.XPATH, "//div[@class='el-table__body-wrapper is-scrolling-none']//input[@placeholder='请选择']")
    tx_lx1 = (By.XPATH, "//div[@x-placement='top-start']//span[text()='项目施工方联系人']")
    tx_zw = (By.XPATH, "//input[@placeholder='请填写职位'][1]")
    ym_bc = (By.XPATH, "//span[text()='保存']")

    def test_add_customer(self, username, password, value1, value2, value3, value4, value5, value6,
                          value7, value8, value9, value10, value11, value12, value13):
        login = LoginPage(self.driver)  # 登录
        login.login_erp(username, password)  # 输入用户名、密码

        self.click(AddCustomer.cmr_gl)
        self.click(AddCustomer.cmr_kh)
        self.click(AddCustomer.cmr_xh)
        self.send_ks(AddCustomer.xz_mc, value1)
        self.send_ks(AddCustomer.xz_dw, value2)
        self.click(AddCustomer.jz_qy)
        sleep(1)
        self.click(AddCustomer.jz_qy1)
        self.click(AddCustomer.jz_qy2)
        sleep(1)
        self.click(AddCustomer.jz_qy21)
        self.click(AddCustomer.qy_fzr)
        # sleep(1)
        self.send_ks(AddCustomer.cz_fzr, value3)
        sleep(1)
        self.click(AddCustomer.dj_qd1)
        self.click(AddCustomer.xz_kh)
        self.click(AddCustomer.dj_qd2)
        sleep(1)
        self.click(AddCustomer.dj_zwf)
        self.click(AddCustomer.dj_qd)
        self.click(AddCustomer.kh_xz)
        # 点击客户性质
        self.click(AddCustomer.kh_xz1)
        self.send_ks(AddCustomer.bz_xx, value4)
        self.send_ks(AddCustomer.bz_dh, value5)
        self.send_ks(AddCustomer.bz_khh, value6)
        self.send_ks(AddCustomer.bz_zh, value7)
        self.send_ks(AddCustomer.bz_dz, value8)
        self.send_ks(AddCustomer.bz_bz, value9)
        self.send_ks(AddCustomer.tx_xm, value10)
        self.send_ks(AddCustomer.tx_dh, value11)
        self.send_ks(AddCustomer.tx_dz, value12)
        self.click(AddCustomer.tx_lx)
        self.click(AddCustomer.tx_lx1)
        self.send_ks(AddCustomer.tx_zw, value13)
        self.click(AddCustomer.ym_bc)
