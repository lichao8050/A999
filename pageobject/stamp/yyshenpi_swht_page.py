# _*_ coding: utf-8 _*_
# @Time    : 2021/5/19 0019 22:13
# @Author  : Mr_Li
# @FileName: yyshenpi_swht_page.py
from pywinauto.keyboard import send_keys
from pywinauto.mouse import click
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from time import sleep
from pageobject.login_page import LoginPage


class YyShenPiSwHtPage(BasePage):
    '''商务合同-用印审批'''

    # 提交审批
    yy_sp = (By.XPATH, "//span[contains(text(),'提交审批')]")
    # 审批流程图
    yy_gl = (By.XPATH, "//span[text()='审批流程图']")
    # 清空
    yy_qk = (By.XPATH, "//span[text()='清空']")
    # 暂存
    yy_zc = (By.XPATH, "//span[text()='暂存']")
    # 草稿箱
    yy_cgx = (By.XPATH, "//span[text()='草稿箱']")
    # 用印事由
    yy_sy = (By.XPATH, "//input[@placeholder='例如：XX公司与XX公司签订XX万元XX合同']")
    # 用印单位
    yy_dw = (By.XPATH, "//div[contains(@class,'is-success')]//input[@placeholder='请选择']")
    # 用印单位1(选择对应账号下的对应单位)
    yy_dw1 = (By.XPATH, "//span[text()='Matrix lab']")
    # 紧急程度  1、2(普通（需3天内审批完成）)  3、4(紧急（需2天内审批完成）)  5(特急（需1天内审批完成）)
    yy_jjcd = (By.XPATH, "//div[@aria-valuenow='5']")
    # 文件类型
    yy_file_type = (By.XPATH, "//form//div[5]//input[@placeholder='请选择']")

    # 文件类型:1、采购类合同
    yy_file_cgl = (By.XPATH, "//li[contains(text(),'1、采购类合同')]")
    # 是否项目采购:是
    yy_cgl_yes = (By.XPATH, "//form//div[5]/div[2]//span[text()='是']")
    # 是否项目采购:否
    yy_cgl_no = (By.XPATH, "//form//div[5]/div[2]//span[text()='否']")
    # 交易对方
    yy_jydf = (By.XPATH, "//div[@class='card_i']//input[@placeholder='请输入']")
    # 选择交易对方：北京邮电大学
    yy_choose_jydf = (By.XPATH, "//li[contains(text(),'北京邮电大学')]")
    # 采购金额:输入采购金额
    yy_input_cgje = (By.XPATH, "//input[@placeholder='请输入采购金额']")
    # 增加一条按钮
    yy_add_button = (By.XPATH, "//i[@class='el-icon-circle-plus-outline icon1']")
    # 删除一条按钮
    yy_del_button = (By.XPATH, "//i[@class='el-icon-delete icon2']")
    # 项目名称：输入；20210830测试20万元项目101期
    yy_xmmc = (By.XPATH, "//form//div[7]/div[1]//input")
    # 点击20210830测试20万元项目101期
    yy_dj_xmmc = (By.XPATH, "//li[contains(text(),'20210830测试20万元项目101期')]")
    # 新增按钮
    yy_dj_newbutton = (By.XPATH, "//button[@type='button']//span[contains(text(),'新增')]")
    # 详情按钮
    yy_dj_readbutton = (By.XPATH, "//button[@type='button']//span[contains(text(),'详情')]")
    # SAP编码：输入：Y20210818
    yy_sap_input = (By.XPATH, "//form//div[7]/div[2]//input")
    # SAP编码点击：Y20210818
    yy_sap_choose = (By.XPATH, "//span[text()='Y20210818']")
    # 公司模板：是
    yy_gsmb_yes = (By.XPATH, "//span[text()='是公司模板']")
    # 公司模板：否
    yy_gsmb_no = (By.XPATH, "//span[text()='非公司模板']")
    # 是否经营类：是
    yy_sfjyl_yes = (By.XPATH, "//form//div[10]/div[2]//span[text()='是']")
    # 是否经营类：否
    yy_sfjyl_no = (By.XPATH, "//form//div[10]/div[2]//span[text()='否']")
    # 是否关联方：是
    yy_sfglf_yes = (By.XPATH, "//form//div[11]//span[text()='是']")
    # 是否关联方：否
    yy_sfglf_no = (By.XPATH, "//form//div[11]//span[text()='否']")

    # 文件类型：2、店铺报价单
    yy_file_dpbjd = (By.XPATH, "//li[contains(text(),'1、店铺报价单')]")
    # 涉及金额：涉及金额
    yy_dpbjd_sjje = (By.XPATH, "//span[text()='涉及金额']")
    # 涉及金额：不涉及金额
    yy_dpbjd_fsjje = (By.XPATH, "//span[text()='不涉及金额']")
    # 项目金额
    yy_dpbjd_money = (By.XPATH, "//input[@placeholder='请输入项目金额']")

    # 文件类型：3、商务类合同
    yy_file_swl = (By.XPATH, "//li[contains(text(),'1、商务类合同')]")
    # 付款比例
    yy_fkbl = (By.XPATH, "//form//div[8]/div[2]//input")
    # 是否包含异常条款：是
    yy_yctk_yes = (By.XPATH, "//form//div[9]/div[2]//span[text()='是']")
    # 是否包含异常条款：否
    yy_yctk_no = (By.XPATH, "//form//div[9]/div[2]//span[text()='否']")

    # 文件类型：4、劳动合同
    yy_file_ldht = (By.XPATH, "//li[contains(text(),'1、劳动合同')]")
    # 交易对方
    yy_ldht_jydf = (By.XPATH, "//span[text()='+点击选择']")
    # 选择交易对方
    yy_ldht_jydf_choose = (By.XPATH, "//div[@class='el-table__fixed']//span[contains(text(),'选择')]")
    # 输入姓名
    yy_send_name = (By.XPATH, "//input[@placeholder='姓名']")
    # 查询按钮
    yy_select_button = (By.XPATH, "//input[@placeholder='查询']")
    # 清空按钮
    yy_clear_button = (By.XPATH, "//input[@placeholder='清空']")
    # 确定按钮
    yy_confirm_button = (By.XPATH, "//span[text()='确定']")
    # 取消按钮
    yy_cancel_button = (By.XPATH, "//span[text()='取消']")

    # 文件类型：5、劳动关系证明文件
    yy_file_ldgxzm = (By.XPATH, "//li[contains(text(),'1、劳动关系证明文件')]")
    # 文件明细
    yy_file_mx = (By.XPATH, "//form//div[9]/div[1]//input")
    # 文件明细：在职证明 收入证明 签证证明
    yy_file_mx1 = (By.XPATH, "//span[text()='在职证明']")
    # 收件单位全称
    yy_file_sjdwqc = (By.XPATH, "//form//div[9]/div[2]//input")
    # 是否涉及劳动报酬证明：是
    yy_ldbczm_yes = (By.XPATH, "//form//div[5]/div[2]//span[text()='是']")
    # 是否涉及劳动报酬证明：否
    yy_ldbczm_no = (By.XPATH, "//form//div[5]/div[2]//span[text()='否']")
    # 文件用途
    yy_ldbczm_wjyt = (By.XPATH, "//textarea[@placeholder='月薪收入xxx 元，用于申请房贷/车贷/签证等']")

    # 文件类型：6、其他文件
    yy_file_qtwj = (By.XPATH, "//li[contains(text(),'1、其他文件')]")
    # 文件明细
    yy_file_qtwjmx = (
    By.XPATH, "//div[@class='el-form-item is-required el-form-item--medium']//input[@placeholder='请选择']")
    # 其它文件文件明细
    yy_file_wjmx = (By.XPATH, "//span[text()='其他']")

    # 文件类型：7、商务招投标
    yy_filec = (By.XPATH, "//li[contains(text(),'1、商务招投标')]")
    # 交易对方：可输入，可点击选择
    yy_swztb_jydf = (By.XPATH, "//div[@class='el-col el-col-8 el-col-offset-3']//input[@placeholder='请输入']")
    # 选择交易对方：采购用印测试1
    yy_swztb_choose_jydf = (By.XPATH, "//span[text()='采购用印测试1']")
    # 选择项目名称：可输入，可点击选择
    yy_swztb_choose_xmmc = (By.XPATH, "//div[@style='display: flex;']//input[@placeholder='请输入']")
    # 点击选择项目名称：采购项目新增测试3万以下
    yy_swztb_choose_xmmc1 = (By.XPATH, "//span[text()='采购项目新增测试3万以下']")

    # 文件类型：8、商务类其他文件
    yy_file_swlqtwj = (By.XPATH, "//li[contains(text(),'1、商务类其他文件')]")

    # 印章类型 ：公章 合同专用章 财务专用章 法人名章 总经理亲笔签名 董事长亲笔签名 电子章
    stamp_service_seal_type = (By.XPATH, "//form//div[13]//div[2]/input[@placeholder='请选择']")
    # 点击印章：公章 合同专用章 财务专用章 法人名章 总经理亲笔签名 董事长亲笔签名 电子章
    stamp_service_seal_type_choose = (By.XPATH, "//span[text()='公章']")
    # 印章公司
    stamp_service_seal_company = (By.XPATH, "//form//div[13]/div[2]//input[@placeholder='请选择']")
    # 选择印章公司：1、矩阵纵横设计股份有限公司 2、矩阵纵横设计股份有限公司成都分公司 3、深圳市矩阵鸣翠设计有限公司 4、深圳市释相艺术文化传播有限公司
    # 5、深圳市香蕉酱艺术传播有限公司 6、矩阵设计（北京）有限公司 7、矩阵纵横（上海）设计咨询有限公司 8、香港矩阵国际设计有限公司
    # 9、深圳矩阵纵横设计有限公司 10、深圳市合纵连横设计有限公司
    stamp_service_seal_company_choose = (By.XPATH, "//li[contains(text(),'1、矩阵纵横设计股份有限公司')]")
    # 文件份数
    stamp_service_file_attachments = (By.XPATH, "//input[@placeholder='请输入数字']")
    # 情况说明
    stamp_service_presentation = (By.XPATH, "//textarea[@placeholder='请输入']")
    # 上传附件
    stamp_service_accessory = (By.XPATH, "//input[@name='file']")

    def test_swht_yysp(self, username, password, value1, value2,
                       value3, value4, value5, value6, value7, value8, value9):
        login = LoginPage(self.driver)  # 登录
        login.login_erp(username, password)  # 输入用户名、密码

        sleep(1)
        self.click(YyShenPiSwHtPage.ht_gl)
        sleep(1)
        self.click(YyShenPiSwHtPage.yy_gl)
        self.click(YyShenPiSwHtPage.yy_sp)
        sleep(1)
        self.send_ks(YyShenPiSwHtPage.yy_sy, value1)
        self.click(YyShenPiSwHtPage.yy_dw)
        sleep(1)
        self.click(YyShenPiSwHtPage.yy_dw1)
        self.click(YyShenPiSwHtPage.jj_cd)
        self.click(YyShenPiSwHtPage.wj_lx)
        sleep(1)
        self.click(YyShenPiSwHtPage.wj_lx1)
        self.send_ks(YyShenPiSwHtPage.jy_df, '采购')
        sleep(1)
        self.click(YyShenPiSwHtPage.jy_df1)
        self.click(YyShenPiSwHtPage.xm_mc)
        sleep(1)
        self.click(YyShenPiSwHtPage.xm_mc1)
        self.send_ks(YyShenPiSwHtPage.xm_je, value2)
        self.click(YyShenPiSwHtPage.sf_gl)
        self.click(YyShenPiSwHtPage.yz_lx)
        sleep(1)
        self.click(YyShenPiSwHtPage.yz_lx1)
        self.click(YyShenPiSwHtPage.yz_gs)
        sleep(1)
        self.click(YyShenPiSwHtPage.yz_gs1)
        self.send_ks(YyShenPiSwHtPage.wj_fs, value3)
        self.send_ks(YyShenPiSwHtPage.yy_sl, value4)
        self.send_ks(YyShenPiSwHtPage.qk_sm, value5)
        sleep(1)
        self.send_ks(YyShenPiSwHtPage.wj_sc, value6)
        self.send_ks(YyShenPiSwHtPage.wj_sc, value7)
        self.send_ks(YyShenPiSwHtPage.wj_sc, value8)
        sleep(3)
        self.click(YyShenPiSwHtPage.tj_sp)
        sleep(3)
        self.jp_qd()
