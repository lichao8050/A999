# _*_ coding: utf-8 _*_
# @Time    : 2021/9/6 10:23
# @Author  : Mr_Li
# @FileName: stamp_service_other_business_documents.py
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from time import sleep
from pageobject.login_page import LoginPage
from base.base_util import logger

logger.info('用印审批--商务类其它文件')


class OtherBusinessDocuments(BasePage):
    """用印审批--商务类其它文件"""

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
    stamp_service_user_center = (By.XPATH, "//div[contains(@class,'is-success')]//input[@placeholder='请选择']")
    # 用印单位1(选择对应账号下的对应单位)
    stamp_service_user_center1 = (By.XPATH, "//span[text()='Matrix lab']")
    # 紧急程度  1、2(普通（需3天内审批完成）)  3、4(紧急（需2天内审批完成）)  5(特急（需1天内审批完成）)
    stamp_service_emergency_degree = (By.XPATH, "//form//div[2]//span[5]")
    # 文件类型
    stamp_service_file_type = (By.XPATH, "//form//div[5]//input[@placeholder='请选择']")

    # 文件类型：5、劳动关系证明文件
    stamp_service_labor_relations = (By.XPATH, "//li[contains(text(),'5、劳动关系证明文件')]")
    # 是否涉及劳动报酬证明：是
    stamp_service_labor_relations_yes = (By.XPATH, "//form//div[5]/div[2]//span[text()='是']")
    # 是否涉及劳动报酬证明：否
    stamp_service_labor_relations_no = (By.XPATH, "//form//div[5]/div[2]//span[text()='否']")
    # 文件明细
    stamp_service_labor_relations_file = (By.XPATH, "//form//div[9]/div[1]//input")
    # 文件明细：在职证明 收入证明 签证证明
    stamp_service_labor_relations_file1 = (By.XPATH, "//span[text()='在职证明']")
    # 收件单位全称
    stamp_service_labor_relations_file_inbox = (By.XPATH, "//form//div[9]/div[2]//input")

    # 印章类型 ：公章 合同专用章 财务专用章 法人名章 总经理亲笔签名 董事长亲笔签名 电子章
    stamp_service_seal_type = (By.XPATH, "//input[@class='el-select__input is-medium']")
    # 点击印章：公章 合同专用章 财务专用章 法人名章 总经理亲笔签名 董事长亲笔签名 电子章
    stamp_service_seal_type_choose = (By.XPATH, "//span[text()='公章']")
    # 印章公司
    stamp_service_seal_company = (By.XPATH, "//form//div[12]//div[1]/input[@placeholder='请选择']")
    # 选择印章公司：1、矩阵纵横设计股份有限公司 2、矩阵纵横设计股份有限公司成都分公司 3、深圳市矩阵鸣翠设计有限公司 4、深圳市释相艺术文化传播有限公司
    # 5、深圳市香蕉酱艺术传播有限公司 6、矩阵设计（北京）有限公司 7、矩阵纵横（上海）设计咨询有限公司 8、香港矩阵国际设计有限公司
    # 9、深圳矩阵纵横设计有限公司 10、深圳市合纵连横设计有限公司
    stamp_service_seal_company_choose = (By.XPATH, "//li[contains(text(),'1、矩阵纵横设计股份有限公司')]")
    # 文件份数
    stamp_service_file_attachments = (By.XPATH, "//input[@placeholder='请输入数字']")
    # 情况说明
    stamp_service_presentation = (By.XPATH, "//textarea[@placeholder='月薪收入xxx 元，用于申请房贷/车贷/签证等']")
    # 上传附件
    stamp_service_accessory = (By.XPATH, "//input[@name='file']")

    def test_other_business_documents(self, username, password, value1, value2, value3, value4, value5):
        login = LoginPage(self.driver)  # 登录
        login.login_erp(username, password)  # 输入用户名、密码

        sleep(1)
        logger.info('点击合同管理')
        self.click(OtherBusinessDocuments.contract_administration)
        logger.info('点击用印管理')
        self.click(OtherBusinessDocuments.using_management)
        logger.info('点击用印审批')
        self.click(OtherBusinessDocuments.stamp_service)
        sleep(1)
        # 选择用印单位
        logger.info('点击选择用印单位')
        self.click(OtherBusinessDocuments.stamp_service_user_center)
        logger.info('选择登录用户对应的用印单位')
        self.click(OtherBusinessDocuments.stamp_service_user_center1)
        # 选择紧急程度
        logger.info('选择用印紧急程度')
        self.click(OtherBusinessDocuments.stamp_service_emergency_degree)
        # 选择文件类型
        logger.info('点击文件类型')
        self.click(OtherBusinessDocuments.stamp_service_file_type)
        # 点击选择文件类型5、劳动关系证明文件
        sleep(1)
        logger.info('点击选择文件类型5、劳动关系证明文件')
        self.click(OtherBusinessDocuments.stamp_service_labor_relations)
        logger.info('输入用印事由名称')
        self.send_ks(OtherBusinessDocuments.stamp_service_cause, value1)
        sleep(1)
        logger.info('点击文件明细')
        self.click(OtherBusinessDocuments.stamp_service_labor_relations_file)
        logger.info('选择在职证明')
        self.click(OtherBusinessDocuments.stamp_service_labor_relations_file1)
        sleep(1)
        logger.info('输入收件单位全称')
        self.send_ks(OtherBusinessDocuments.stamp_service_labor_relations_file_inbox, value2)

        logger.info('选择印章类型')
        self.click(OtherBusinessDocuments.stamp_service_seal_type)
        logger.info('选择印章类型：公章')
        self.click(OtherBusinessDocuments.stamp_service_seal_type_choose)
        logger.info('点击印章公司')
        self.click(OtherBusinessDocuments.stamp_service_seal_company)
        logger.info('选择印章公司：1、矩阵纵横设计股份有限公司')
        self.click(OtherBusinessDocuments.stamp_service_seal_company_choose)
        logger.info('输入文件份数')
        self.send_ks(OtherBusinessDocuments.stamp_service_file_attachments, value3)
        logger.info('输入文件用途说明')
        self.send_ks(OtherBusinessDocuments.stamp_service_presentation, value4)
        logger.info('上传文件')
        self.send_ks(OtherBusinessDocuments.stamp_service_accessory, value5)
        sleep(3)
        logger.info('点击提交审批按钮')
        self.click(OtherBusinessDocuments.submit_stamp_service)
        sleep(1)
        logger.info('点击键盘确定“回车键”')
        self.jp_qd()
