# _*_ coding: utf-8 _*_
# @Time    : 2021/9/6 10:15
# @Author  : Mr_Li
# @FileName: stamp_service_labor_contract.py
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from time import sleep
from pageobject.login_page import LoginPage
from base.base_util import logger

logger.info('用印审批--劳动合同')


class LaborContract(BasePage):
    """劳动合同--用印审批"""

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

    # 文件类型：4、劳动合同
    stamp_service_labor_contract = (By.XPATH, "//li[contains(text(),'4、劳动合同')]")
    # 点击选择交易对方
    stamp_service_adverse = (By.XPATH, "//span[text()='+点击选择']")
    # 输入查询交易对方
    stamp_service_adverse_input = (By.XPATH, "//input[@placeholder='姓名']")
    # 点击查询按钮
    stamp_service_adverse_select = (By.XPATH, "//span[text()='查询']")
    # 选择查询到的交易对方
    stamp_service_adverse_select_choose = (By.XPATH, "//div[@sortable='sortable']//div[2]//span[contains(text(),'选择')]")
    # 点击确定按钮
    stamp_service_adverse_select_choose_yes = (By.XPATH, "//span[text()='确定']")
    # 公司模板：是
    stamp_service_corporate_yes = (By.XPATH, "//span[text()='是公司模板']")
    # 公司模板：否
    stamp_service_corporate_no = (By.XPATH, "//span[text()='非公司模板']")

    # 印章类型 ：公章 合同专用章 财务专用章 法人名章 总经理亲笔签名 董事长亲笔签名 电子章
    stamp_service_seal_type = (By.XPATH, "//input[@class='el-select__input is-medium']")
    # 点击印章：公章 合同专用章 财务专用章 法人名章 总经理亲笔签名 董事长亲笔签名 电子章
    stamp_service_seal_type_choose = (By.XPATH, "//span[text()='公章']")
    # 印章公司
    stamp_service_seal_company = (By.XPATH, "//form//div[11]/div[2]//div[1]/input")
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

    def test_labor_contract(self, username, password, value1, value2, value3, value4, value5):
        login = LoginPage(self.driver)  # 登录
        login.login_erp(username, password)  # 输入用户名、密码

        sleep(1)
        logger.info('点击合同管理')
        self.click(LaborContract.contract_administration)
        logger.info('点击用印管理')
        self.click(LaborContract.using_management)
        logger.info('点击用印审批')
        self.click(LaborContract.stamp_service)
        sleep(1)
        # 选择用印单位
        logger.info('点击选择用印单位')
        self.click(LaborContract.stamp_service_user_center)
        logger.info('选择登录用户对应的用印单位')
        self.click(LaborContract.stamp_service_user_center1)
        # 选择紧急程度
        logger.info('选择用印紧急程度')
        self.click(LaborContract.stamp_service_emergency_degree)
        # 选择文件类型
        logger.info('点击文件类型')
        self.click(LaborContract.stamp_service_file_type)
        # 点击选择文件类型1.采购类合同
        sleep(1)
        logger.info('点击选择文件类型4、劳动合同')
        self.click(LaborContract.stamp_service_labor_contract)
        logger.info('输入用印事由名称')
        self.send_ks(LaborContract.stamp_service_cause, value1)
        sleep(1)
        logger.info('点击交易对方')
        self.click(LaborContract.stamp_service_adverse)
        logger.info('输入需要查找的用户')
        self.send_ks(LaborContract.stamp_service_adverse_input, value2)
        logger.info('点击查找按钮')
        self.click(LaborContract.stamp_service_adverse_select)
        sleep(1)
        logger.info('选择查找到的用户')
        self.click(LaborContract.stamp_service_adverse_select_choose)
        logger.info('点击确定按钮')
        self.click(LaborContract.stamp_service_adverse_select_choose_yes)

        logger.info('选择印章类型')
        self.click(LaborContract.stamp_service_seal_type)
        logger.info('选择印章类型：公章')
        self.click(LaborContract.stamp_service_seal_type_choose)
        logger.info('点击印章公司')
        self.click(LaborContract.stamp_service_seal_company)
        logger.info('选择印章公司：1、矩阵纵横设计股份有限公司')
        self.click(LaborContract.stamp_service_seal_company_choose)
        logger.info('输入文件份数')
        self.send_ks(LaborContract.stamp_service_file_attachments, value3)
        logger.info('输入情况说明')
        self.send_ks(LaborContract.stamp_service_presentation, value4)
        logger.info('上传文件')
        self.send_ks(LaborContract.stamp_service_accessory, value5)
        sleep(1)
        logger.info('点击提交审批按钮')
        self.click(LaborContract.submit_stamp_service)
        sleep(1)
        logger.info('点击键盘确定“回车键”')
        self.jp_qd()
