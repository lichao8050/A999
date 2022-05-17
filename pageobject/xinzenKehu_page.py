# _*_ coding: utf-8 _*_
# @Time    : 2021/5/13 0013 23:06
# @Author  : LiChao
# @FileName: xinzenKehu_page.py
from time import sleep

from selenium.webdriver.common.by import By

from base.base_page import BasePage
from pageobject.login_page import LoginPage


class XinZenKeHu(BasePage):
    # 页面元素
    cmr_gl = (By.XPATH, "//span[text()='CRM管理']")
    cmr_kh = (By.XPATH, "//span[text()='我的客戶']")
    cmr_xzkh = (By.XPATH, "//button/span[contains(text(),'新增')]")
    xz_jtmc = (By.XPATH, "//input[@placeholder='举例：龙湖、旭辉（不加地区/地产/集团等字眼）']")
    xz_khdw = (By.XPATH, "//input[@placeholder='请输入客户单位']")
    jz_qy = (By.XPATH, "/html/body/section/div/section/"
                       "section/main/div/div[2]/div/form/div[1]"
                       "/div[3]/div/div/div/div/div[1]/div"
                       "/div/div/div/div/input")
    jz_qy1 = (By.XPATH, "/html/body/section/div/section/section/main/"
                        "div/div[2]/div/form/div[1]/div[3]/div/div/"
                        "div/div/div[1]/div/div/div/div/div[2]/div[1]/div[1]/ul/li[15]")
    jz_qy2 = (By.XPATH, "/html/body/section/div/section/"
                        "section/main/div/div[2]/div/form/div[1]/"
                        "div[3]/div/div/div/div/div[2]/"
                        "div/div/div/div/div[1]/input")
    jz_qy3 = (By.XPATH, "/html/body/section/div/section/section/main/div/div[2]/div/form/"
                        "div[1]/div[3]/div/div/div/div/div[2]/div/div/div/div/div[2]"
                        "/div[1]/div[1]/ul/li[1]")
    qy_fzr = (By.XPATH, "//input[@placeholder='选择一个区域负责人']")
    cz_fzr = (By.XPATH, "/html/body/section/div/section/section/main/"
                        "div/div[2]/div/form/div[1]/div[4]/div[1]/div/"
                        "div/div/div[2]/div/div[2]/div[1]/form/div/div[1]/"
                        "div/div/div/div/input")
    dj_qd1  = (By.XPATH, "/html/body/section/div/section/section/main/div/"
                        "div[2]/div/form/div[1]/div[4]/div[1]/div/div/div/"
                        "div[2]/div/div[2]/div[1]/form/div/div[2]/div/div/button[1]")
    xz_kh  = (By.XPATH, "/html/body/section/div/section/section/main/div/div[2]/"
                       "div/form/div[1]/div[4]/div[1]/div/div/div/div[2]/"
                       "div/div[2]/div[2]/div/div[1]/div[4]/"
                       "div[2]/table/tbody/tr/td[1]/div")
    dj_qd2 = (By.XPATH, "/html/body/section/div/section/section/main/div/div[2]/"
                        "div/form/div[1]/div[4]/div[1]/div/div/div/div[2]/"
                        "div/div[3]/div/button[1]")

    dj_zwf = (By.XPATH, "/html/body/section/div/section/section/main/"
                        "div/div[2]/div/form/div[1]/div[4]/div[1]/div/"
                        "div/div/div[2]/div/div[2]/div[2]/div/div[1]/"
                        "div[4]/div[2]/table/tbody/tr[9]/td[3]/div")
    dj_qd = (By.XPATH, "/html/body/section/div/section/section/main/div/"
                       "div[2]/div/form/div[1]/div[4]/div[1]/div/div"
                       "/div/div[2]/div/div[3]/div/button[1]")
    kh_xz = (By.XPATH, "/html/body/section/div/section/section/main/div/"
                       "div[2]/div/form/div[1]/div[5]/div[1]/"
                       "div/div/div/div/div[1]/input")
    kh_xz1 = (By.XPATH, "/html/body/div[3]/div[1]/div[1]/ul/li[1]")
    kh_dj = (By.XPATH, "/html/body/section/div/section/section/"
                       "main/div/div[2]/div/form/div[1]/div[5]/"
                       "div[2]/div/div/div/div/div[1]/input")
    kh_dj1 = (By.XPATH, "/html/body/div[4]/div[1]/div[1]/ul/li[1]")
    bz_xx = (By.XPATH, "//textarea[@placeholder='请填写客户信息备注']")
    tx_lxrxm = (By.XPATH, "//input[@placeholder='请填写联系人姓名'][1]")
    tx_lxdh = (By.XPATH, "//input[@placeholder='请填写联系电话'][1]")
    tx_lxdz = (By.XPATH, "//input[@placeholder='请填写联系地址'][1]")
    xz_lxrnx = (By.XPATH, "/html/body/section/div/section/section/"
                          "main/div/div[2]/div/form/div[3]/div[2]/div/"
                          "div/div[2]/div/div/div/div/div[3]/table/tbody/"
                          "tr/td[7]/div/div/div/div[1]/input")
    xz_lxrnx1 = (By.XPATH, "/html/body/div[5]/div[1]/div[1]/ul/li[1]")
    tx_lxrzw = (By.XPATH, "//input[@placeholder='请填写职位'][1]")
    ym_bc = (By.XPATH, "/html/body/section/div/section/section"
                       "/main/div/div[2]/div/div/div/button[1]")

    def test_xz_kh(self,username,password,jtmc,khdw,qyfzr):

        dl = LoginPage(self.driver)
        dl.logine_erp(username, password)

        self.click(XinZenKeHu.cmr_gl)
        self.click(XinZenKeHu.cmr_kh)
        self.click(XinZenKeHu.cmr_xzkh)
        self.send_ks(XinZenKeHu.xz_jtmc, jtmc)
        self.send_ks(XinZenKeHu.xz_khdw, khdw)
        self.click(XinZenKeHu.jz_qy)
        sleep(1)
        self.click(XinZenKeHu.jz_qy1)
        self.click(XinZenKeHu.jz_qy2)
        sleep(1)
        self.click(XinZenKeHu.jz_qy3)
        self.click(XinZenKeHu.qy_fzr)
        # sleep(1)
        self.send_ks(XinZenKeHu.cz_fzr,qyfzr)
        # sleep(3)
        self.click(XinZenKeHu.dj_qd1)
        # sleep(3)
        self.click(XinZenKeHu.xz_kh)
        self.click(XinZenKeHu.dj_qd2)


        # self.click(XinZenKeHu.dj_zwf)
        # self.click(XinZenKeHu.dj_qd)
        sleep(1)
        self.click(XinZenKeHu.kh_xz)
        self.click(XinZenKeHu.kh_xz1)
        self.click(XinZenKeHu.kh_dj)
        sleep(1)
        self.click(XinZenKeHu.kh_dj1)
        self.send_ks(XinZenKeHu.bz_xx, "这是用于测试的一段备注文字！@")
        self.send_ks(XinZenKeHu.tx_lxrxm, "张三1")
        self.send_ks(XinZenKeHu.tx_lxdh, 13333333333)
        self.send_ks(XinZenKeHu.tx_lxdz, "深圳市福宝建设北路1101号")
        self.click(XinZenKeHu.xz_lxrnx)
        sleep(1)
        self.click(XinZenKeHu.xz_lxrnx1)
        self.send_ks(XinZenKeHu.tx_lxrzw, "某某某项目总监")
        self.click(XinZenKeHu.ym_bc)
