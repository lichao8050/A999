# _*_ coding: utf-8 _*_
# @Time    : 2021/5/19 0019 22:36
# @Author  : Mr_Li
# @FileName: stamp_service_shop_quotation
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from time import sleep
from pageobject.login_page import LoginPage
from base.base_util import logger

logger.info('用印审批--店铺报价单')


class ShopQuotation(BasePage):
    """用印审批--店铺报价单"""

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
    stamp_service_dw1 = (By.XPATH, "//span[text()='Matrix lab']")
    # 紧急程度  1、2(普通（需3天内审批完成）)  3、4(紧急（需2天内审批完成）)  5(特急（需1天内审批完成）)
    stamp_service_jjcd = (By.XPATH, "//div[@aria-valuenow='5']")
    stamp_service_jjcd1 = (By.XPATH, "//form//div[2]//span[5]")
    # 文件类型
    stamp_service_file_type = (By.XPATH, "//form//div[5]//input[@placeholder='请选择']")

    # 文件类型：2、店铺报价单
    yy_file_dpbjd = (By.XPATH, "//li[contains(text(),'2、店铺报价单')]")
    # 涉及金额：涉及金额
    yy_dpbjd_sjje = (By.XPATH, "//span[text()='涉及金额']")
    # 涉及金额：不涉及金额
    yy_dpbjd_fsjje = (By.XPATH, "//span[text()='不涉及金额']")
    # 项目金额
    yy_dpbjd_money = (By.XPATH, "//input[@placeholder='请输入项目金额']")
    # 是否关联方：是
    yy_sfglf_yes = (By.XPATH, "//span[text()='是']")
    # 是否关联方：否
    yy_sfglf_no = (By.XPATH, "//span[text()='否']")

    # 印章类型 ：公章 合同专用章 财务专用章 法人名章 总经理亲笔签名 董事长亲笔签名 电子章
    stamp_service_yzlx = (By.XPATH, "//div[2]/input[@placeholder='请选择']")
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

    def test_shop_quotation(self, username, password, value1, value2, value3, value4, value5):
        login = LoginPage(self.driver)  # 登录
        login.login_erp(username, password)  # 输入用户名、密码

        sleep(1)
        logger.info('点击合同管理')
        self.click(ShopQuotation.contract_administration)
        logger.info('点击用印管理')
        self.click(ShopQuotation.using_management)
        logger.info('点击用印审批')
        self.click(ShopQuotation.stamp_service)
        sleep(1)
        # 选择用印单位
        logger.info('点击选择用印单位')
        self.click(ShopQuotation.stamp_service_dw)
        logger.info('选择登录用户对应的用印单位')
        self.click(ShopQuotation.stamp_service_dw1)
        # 选择紧急程度
        logger.info('选择用印紧急程度')
        self.click(ShopQuotation.stamp_service_jjcd1)
        # 选择文件类型
        logger.info('点击文件类型')
        self.click(ShopQuotation.stamp_service_file_type)
        # 点击选择文件类型1.采购类合同
        logger.info('点击选择文件类型2、店铺报价单')
        self.click(ShopQuotation.yy_file_dpbjd)
        logger.info('输入用印事由名称')
        self.send_ks(ShopQuotation.stamp_service_cause, value1)
        logger.info('点击涉及金额')
        self.click(ShopQuotation.yy_dpbjd_sjje)
        logger.info('输入项目金额')
        self.send_ks(ShopQuotation.yy_dpbjd_money, value2)
        logger.info('选择是关联方')
        self.click(ShopQuotation.yy_sfglf_yes)
        logger.info('点击印章类型')
        self.click(ShopQuotation.stamp_service_yzlx)
        logger.info('选择印章类型：公章')
        self.click(ShopQuotation.stamp_service_yzlx_choose)
        logger.info('点击印章公司')
        self.click(ShopQuotation.stamp_service_yzgs)
        logger.info('选择印章公司：1、矩阵纵横设计股份有限公司')
        self.click(ShopQuotation.stamp_service_yzgs_choose)
        logger.info('输入文件份数')
        self.send_ks(ShopQuotation.stamp_service_wjfs, value3)
        logger.info('输入情况说明')
        self.send_ks(ShopQuotation.stamp_service_qksm, value4)
        logger.info('上传文件')
        self.send_ks(ShopQuotation.stamp_service_scfj, value5)
        sleep(3)
        logger.info('点击提交审批按钮')
        self.click(ShopQuotation.submit_stamp_service)
        self.jp_qd()
