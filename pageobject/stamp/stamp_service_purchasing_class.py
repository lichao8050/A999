# _*_ coding: utf-8 _*_
# @Time    : 2021/5/19 0019 22:36
# @Author  : Mr_Li
# @FileName: using_approval_purchasing_class
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from time import sleep
from pageobject.login_page import LoginPage
from base.base_util import logger

logger.info('用印审批--采购类合同')


class PurchasingClass(BasePage):
    """用印审批--采购类合同"""

    # 合同管理
    contract_administration = (By.XPATH, "//li[@id='1260220714821226498']//span[text()='合同管理']")
    # 用印管理
    using_management = (By.XPATH, "//span[text()='用印管理']")
    # 用印审批
    stamp_service = (By.XPATH, "//span[text()='用印审批']")
    # 提交审批
    submit_stamp_service = (By.XPATH, "//span[contains(text(),'提交审批')]")
    # 审批流程图
    stamp_service_flow_chart = (By.XPATH, "//span[text()='审批流程图']")
    # 清空
    stamp_service_clear = (By.XPATH, "//span[text()='清空']")
    # 暂存
    stamp_service_staging = (By.XPATH, "//span[text()='暂存']")
    # 草稿箱
    stamp_service_drafts = (By.XPATH, "//span[text()='草稿箱']")
    # 用印事由
    stamp_service_cause = (By.XPATH, "//input[@placeholder='例如：XX公司与XX公司签订XX万元XX合同']")
    # 用印单位
    stamp_service_dw = (By.XPATH, "//div[contains(@class,'is-success')]//input[@placeholder='请选择']")
    # 用印单位1(选择对应账号下的对应单位)
    stamp_service_dw1 = (By.XPATH, "//span[text()='供应链事业部']")
    # 紧急程度  1、2(普通（需3天内审批完成）)  3、4(紧急（需2天内审批完成）)  5(特急（需1天内审批完成）)
    stamp_service_jjcd = (By.XPATH, "//div[@aria-valuenow='5']")
    stamp_service_jjcd1 = (By.XPATH, "//form//div[2]//span[5]")
    # 文件类型
    stamp_service_file_type = (By.XPATH, "//form//div[5]//input[@placeholder='请选择']")

    # 文件类型:1、采购类合同   2、采购框架协议  3、采购合同(模板)   4、采购合同(非模板)
    stamp_service_file_cgl = (By.XPATH, "//li[contains(text(),'4、采购合同(非模板)')]")
    # 是否项目采购:是
    stamp_service_cgl_yes = (By.XPATH, "//form//div[5]/div[2]//span[text()='是']")
    # 是否项目采购:否
    stamp_service_cgl_no = (By.XPATH, "//form//div[5]/div[2]//span[text()='否']")
    # 交易对方
    stamp_service_jydf = (By.XPATH, "//div[@class='card_i']//input[@placeholder='请输入']")
    # 选择交易对方：北京邮电大学
    stamp_service_choose_jydf = (By.XPATH, "//li[contains(text(),'北京邮电大学')]")
    # 采购金额:输入采购金额
    stamp_service_input_cgje = (By.XPATH, "//input[@placeholder='请输入采购金额']")
    # 增加一条按钮
    stamp_service_add_button = (By.XPATH, "//i[@class='el-icon-circle-plus-outline icon1']")
    # 删除一条按钮
    stamp_service_del_button = (By.XPATH, "//i[@class='el-icon-delete icon2']")
    # 项目名称：输入；20210830测试20万元项目101期
    stamp_service_xmmc = (By.XPATH, "//form//div[7]/div[1]//input")
    # 点击20210830测试20万元项目101期
    stamp_service_dj_xmmc = (By.XPATH, "//li[contains(text(),'20210830测试20万元项目101期')]")
    # 新增按钮
    stamp_service_dj_newbutton = (By.XPATH, "//button[@type='button']//span[contains(text(),'新增')]")
    # 详情按钮
    stamp_service_dj_readbutton = (By.XPATH, "//button[@type='button']//span[contains(text(),'详情')]")
    # SAP编码：输入：Y20210818
    stamp_service_sap_input = (By.XPATH, "//form//div[7]/div[2]//input")
    # SAP编码点击：Y20210818
    stamp_service_sap_choose = (By.XPATH, "//span[text()='Y20210818']")
    # 公司模板：是
    stamp_service_gsmb_yes = (By.XPATH, "//span[text()='是公司模板']")
    # 公司模板：否
    stamp_service_gsmb_no = (By.XPATH, "//span[text()='非公司模板']")
    # 是否经营类：是
    stamp_service_sfjyl_yes = (By.XPATH, "//form//div[10]/div[2]//span[text()='是']")
    # 是否经营类：否
    stamp_service_sfjyl_no = (By.XPATH, "//form//div[10]/div[2]//span[text()='否']")
    # 是否关联方：是
    stamp_service_sfglf_yes = (By.XPATH, "//form//div[11]//span[text()='是']")
    # 是否关联方：否
    stamp_service_sfglf_no = (By.XPATH, "//form//div[11]//span[text()='否']")

    # 印章类型 ：公章 合同专用章 财务专用章 法人名章 总经理亲笔签名 董事长亲笔签名 电子章
    stamp_service_yzlx = (By.XPATH, "//input[@class='el-select__input is-medium']")
    # 点击印章：公章 合同专用章 财务专用章 法人名章 总经理亲笔签名 董事长亲笔签名 电子章
    stamp_service_yzlx_choose = (By.XPATH, "//span[text()='公章']")
    # 印章公司
    stamp_service_yzgs = (By.XPATH, "//form//div[13]/div[2]//input[@placeholder='请选择']")
    # 选择印章公司：1、矩阵纵横设计股份有限公司 2、矩阵纵横设计股份有限公司成都分公司 3、深圳市矩阵鸣翠设计有限公司 4、深圳市释相艺术文化传播有限公司
    # 5、深圳市香蕉酱艺术传播有限公司 6、矩阵设计（北京）有限公司 7、矩阵纵横（上海）设计咨询有限公司 8、香港矩阵国际设计有限公司
    # 9、深圳矩阵纵横设计有限公司 10、深圳市合纵连横设计有限公司
    stamp_service_yzgs_choose = (By.XPATH, "//li[contains(text(),'1、矩阵纵横设计股份有限公司')]")
    # 文件份数
    stamp_service_wjfs = (By.XPATH, "//input[@placeholder='请输入数字']")
    # 情况说明
    stamp_service_qksm = (By.XPATH, "//textarea[@placeholder='请输入']")
    # 上传附件
    stamp_service_scfj = (By.XPATH, "//input[@name='file']")

    def test_purchasing_class(self, username, password, value1, value2, value3, value4, value5, value6, value7, ):
        login = LoginPage(self.driver)  # 登录
        login.login_erp(username, password)  # 输入用户名、密码

        sleep(1)
        logger.info('点击合同管理')
        self.click(PurchasingClass.contract_administration)
        logger.info('点击用印管理')
        self.click(PurchasingClass.using_management)
        logger.info('点击用印审批')
        self.click(PurchasingClass.stamp_service)
        sleep(1)
        # 选择用印单位
        logger.info('点击选择用印单位')
        self.click(PurchasingClass.stamp_service_dw)
        logger.info('选择登录用户对应的用印单位')
        self.click(PurchasingClass.stamp_service_dw1)
        # 选择紧急程度
        logger.info('选择用印紧急程度')
        self.click(PurchasingClass.stamp_service_jjcd1)
        # 选择文件类型
        logger.info('点击文件类型')
        self.click(PurchasingClass.stamp_service_file_type)
        # 点击选择文件类型1.采购类合同
        logger.info('点击选择文件类型1.采购类合同')
        self.click(PurchasingClass.stamp_service_file_cgl)
        logger.info('输入用印事由名称')
        self.send_ks(PurchasingClass.stamp_service_cause, value1)
        logger.info('输入交易对方')
        self.send_ks(PurchasingClass.stamp_service_jydf, value2)
        logger.info('选中输入的交易对方')
        self.click(PurchasingClass.stamp_service_choose_jydf)
        logger.info('输入采购金额')
        self.send_ks(PurchasingClass.stamp_service_input_cgje, value3)
        logger.info('输入项目名称')
        self.send_ks(PurchasingClass.stamp_service_xmmc, value4)
        logger.info('选中输入的项目名称')
        self.click(PurchasingClass.stamp_service_dj_xmmc)
        logger.info('是否关联方选择：是')
        self.click(PurchasingClass.stamp_service_sfglf_yes)
        logger.info('点击印章类型')
        self.click(PurchasingClass.stamp_service_yzlx)
        logger.info('选择印章类型：公章')
        self.click(PurchasingClass.stamp_service_yzlx_choose)
        logger.info('点击印章公司')
        self.click(PurchasingClass.stamp_service_yzgs)
        logger.info('选择印章公司：1、矩阵纵横设计股份有限公司')
        self.click(PurchasingClass.stamp_service_yzgs_choose)
        logger.info('输入文件份数')
        self.send_ks(PurchasingClass.stamp_service_wjfs, value5)
        logger.info('输入情况说明')
        self.send_ks(PurchasingClass.stamp_service_qksm, value6)
        logger.info('上传文件')
        self.send_ks(PurchasingClass.stamp_service_scfj, value7)
        sleep(3)
        logger.info('鼠标向上滚动')
        self.mouse_wheel_up()
        logger.info('点击提交审批按钮')
        self.click(PurchasingClass.submit_stamp_service)
        sleep(1)
        self.jp_qd()
