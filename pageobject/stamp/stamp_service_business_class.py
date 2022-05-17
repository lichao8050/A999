# _*_ coding: utf-8 _*_
# @Time    : 2021/9/6 10:11
# @Author  : Mr_Li
# @FileName: stamp_service_business_class.py
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from time import sleep
from pageobject.login_page import LoginPage
from base.base_util import logger

logger.info('用印审批--商务类合同')


class BusinessClass(BasePage):
    """用印审批--商务类合同"""

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

    # 文件类型：3、商务类合同
    stamp_service_business_contract = (By.XPATH, "//li[contains(text(),'3、商务类合同')]")
    # 付款比例
    stamp_service_payment = (By.XPATH, "//form//div[8]/div[2]//input")
    # 是否包含异常条款：是
    stamp_service_exception_yes = (By.XPATH, "//form//div[9]/div[2]//span[text()='是']")
    # 是否包含异常条款：否
    stamp_service_exception_no = (By.XPATH, "//form//div[9]/div[2]//span[text()='否']")
    # 输入交易对方
    stamp_service_adverse = (By.XPATH, "//div[@class='el-col el-col-8 el-col-offset-3']//input[@placeholder='请输入']")
    # 选择交易对方：东升室内装修设计有限公司  通过输入查找
    stamp_service_choose_adverse = (By.XPATH, "//span[text()='东升室内装修设计有限公司']")
    # 项目金额:输入项目金额
    stamp_service_input_money = (By.XPATH, "//input[@placeholder='请输入项目金额']")
    # 项目名称输入；MKZ20210909经典项目测试101期
    stamp_service_project_name = (
        By.XPATH,
        "//div[@class='el-form-item is-required is-required el-form-item--medium']//input[@placeholder='请输入']")
    # 点击MKZ20210909经典项目测试101期
    stamp_service_click_project_name = (By.XPATH, "//span[text()='MKZ20210909经典项目测试101期']")
    # 新增按钮
    stamp_service_new_button = (By.XPATH, "//span[contains(text(),'新增')]")
    # 详情按钮
    stamp_service_detail = (By.XPATH, "//span[contains(text(),'详情')]")
    # 涉及金额：涉及金额
    stamp_service_money_involved = (By.XPATH, "//span[text()='涉及金额']")
    # 涉及金额：不涉及金额
    stamp_service_no_money_involved = (By.XPATH, "//span[text()='不涉及金额']")
    # 公司模板：是
    stamp_service_corporate_yes = (By.XPATH, "//span[text()='是公司模板']")
    # 公司模板：否
    stamp_service_corporate_no = (By.XPATH, "//span[text()='非公司模板']")

    # 印章类型 ：公章 合同专用章 财务专用章 法人名章 总经理亲笔签名 董事长亲笔签名 电子章
    stamp_service_seal_type = (By.XPATH, "//input[@class='el-select__input is-medium']")
    # 点击印章：公章 合同专用章 财务专用章 法人名章 总经理亲笔签名 董事长亲笔签名 电子章
    stamp_service_seal_type_choose = (By.XPATH, "//span[text()='公章']")
    # 印章公司
    stamp_service_seal_company = (By.XPATH, "//form//div[11]/div[2]//input[@placeholder='请选择']")
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

    def test_business_class(self, username, password, value1, value2, value3, value4, value5, value6, value7, value8):
        login = LoginPage(self.driver)  # 登录
        login.login_erp(username, password)  # 输入用户名、密码

        sleep(1)
        logger.info('点击合同管理')
        self.click(BusinessClass.contract_administration)
        logger.info('点击用印管理')
        self.click(BusinessClass.using_management)
        logger.info('点击用印审批')
        self.click(BusinessClass.stamp_service)
        sleep(1)
        # 选择用印单位
        logger.info('点击选择用印单位')
        self.click(BusinessClass.stamp_service_user_center)
        logger.info('选择登录用户对应的用印单位')
        self.click(BusinessClass.stamp_service_user_center1)
        # 选择紧急程度
        logger.info('选择用印紧急程度')
        self.click(BusinessClass.stamp_service_emergency_degree)
        # 选择文件类型
        logger.info('点击文件类型')
        self.click(BusinessClass.stamp_service_file_type)
        # 点击选择文件类型1.采购类合同
        logger.info('点击选择文件类型3、商务类合同')
        self.click(BusinessClass.stamp_service_business_contract)
        logger.info('输入用印事由名称')
        self.send_ks(BusinessClass.stamp_service_cause, value1)
        sleep(1)
        logger.info('输入交易对方')
        self.send_ks(BusinessClass.stamp_service_adverse, value2)
        logger.info('点击选择输入的交易对方')
        self.click(BusinessClass.stamp_service_choose_adverse)
        logger.info('输入项目名称')
        self.send_ks(BusinessClass.stamp_service_project_name, value3)
        sleep(1)
        logger.info('点击对应项目名称')
        self.click(BusinessClass.stamp_service_click_project_name)
        logger.info('点击涉及金额')
        self.click(BusinessClass.stamp_service_money_involved)
        logger.info('输入项目金额')
        self.send_ks(BusinessClass.stamp_service_input_money, value4)
        logger.info('选择是公司模板')
        self.click(BusinessClass.stamp_service_corporate_yes)
        logger.info('输入付款比例')
        self.send_ks(BusinessClass.stamp_service_payment, value5)
        logger.info('选择印章类型')
        self.click(BusinessClass.stamp_service_seal_type)
        logger.info('选择印章类型：公章')
        self.click(BusinessClass.stamp_service_seal_type_choose)
        logger.info('点击印章公司')
        self.click(BusinessClass.stamp_service_seal_company)
        logger.info('选择印章公司：1、矩阵纵横设计股份有限公司')
        self.click(BusinessClass.stamp_service_seal_company_choose)
        logger.info('输入文件份数')
        self.send_ks(BusinessClass.stamp_service_file_attachments, value6)
        logger.info('输入情况说明')
        self.send_ks(BusinessClass.stamp_service_presentation, value7)
        logger.info('上传文件')
        self.send_ks(BusinessClass.stamp_service_accessory, value8)
        sleep(3)
        logger.info('点击提交审批按钮')
        self.click(BusinessClass.submit_stamp_service)
        self.jp_qd()
