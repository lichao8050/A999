# _*_ coding: utf-8 _*_
# @Time    : 2021/9/6 10:23
# @Author  : Mr_Li
# @FileName: stamp_service_factoring_business.py
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from time import sleep
from pageobject.login_page import LoginPage
from base.base_util import logger
from pageobject.system_dictionary_list import matrix

logger.info('用印审批--保理相关文件')


class FactoringBusiness(BasePage):
    """用印审批--保理相关文件"""

    # 提交审批
    submit_factoring_business = (By.XPATH, "//span[contains(text(),'提交审批')]")
    # 审批流程图
    factoring_business_flow_chart = (By.XPATH, "//span[text()='审批流程图']")
    # 清空
    factoring_business_clear = (By.XPATH, "//span[text()='清空']")
    # 暂存
    factoring_business_staging = (By.XPATH, "//span[text()='暂存']")
    # 草稿箱
    factoring_business_drafts = (By.XPATH, "//span[text()='草稿箱']")
    # 用印事由
    factoring_business_cause = (By.XPATH, "//input[@placeholder='例如：XX公司与XX公司签订XX万元XX合同']")
    # 用印单位
    factoring_business_user_center = (By.XPATH, "//div[contains(@class,'is-success')]//input[@placeholder='请选择']")
    # 用印单位1(选择对应账号下的对应单位)
    factoring_business_user_center1 = (By.XPATH, "//span[text()='Matrix lab']")
    # 紧急程度  1、2(普通（需3天内审批完成）)  3、4(紧急（需2天内审批完成）)  5(特急（需1天内审批完成）)
    factoring_business_emergency_degree = (By.XPATH, "//form//div[2]//span[5]")
    # 文件类型
    factoring_business_file_type = (By.XPATH, "//*[contains(text(),'文件类型')]//parent::div//input[@placeholder='请选择']")

    # 文件类型：9、保理相关文件类型
    # factoring_business_labor_relations = (By.XPATH, "//li[contains(text(),'5、劳动关系证明文件')]")
    factoring_business_labor_relations = (By.XPATH, "//div[@x-placement='bottom-start']//li")
    # 输入交易对方
    factoring_business_adverse = (By.XPATH, "//*[contains(text(),'交易对方')]//parent::div//input[@placeholder='请输入']")
    # 选择交易对方：东升室内装修设计有限公司  通过输入查找
    factoring_business_choose_adverse = (By.XPATH, "//span[text()='东升室内装修设计有限公司']")
    # 项目名称输入；MKZ20210909经典项目测试101期
    factoring_business_project_name = (By.XPATH, "//*[contains(text(),'项目名称')]//parent::div//input[@placeholder='请输入']")
    # 点击MKZ20210909经典项目测试101期
    factoring_business_click_project_name = (By.XPATH, "//*[contains(text(),'项目名称')]//parent::div//li")
    # 新增按钮
    factoring_business_new_button = (By.XPATH, "//span[contains(text(),'新增')]")
    # 详情按钮
    factoring_business_detail = (By.XPATH, "//span[contains(text(),'详情')]")
    # 涉及金额：涉及金额
    factoring_business_money_involved = (By.XPATH, "//span[text()='涉及金额']")
    # 涉及金额：不涉及金额
    factoring_business_no_money_involved = (By.XPATH, "//span[text()='不涉及金额']")
    # 项目金额:输入项目金额
    factoring_business_input_money = (By.XPATH, "//input[@placeholder='请输入项目金额']")
    # 公司模板：是
    factoring_business_corporate_yes = (By.XPATH, "//span[text()='是公司模板']")
    # 公司模板：否
    factoring_business_corporate_no = (By.XPATH, "//span[text()='非公司模板']")
    # 是否关联方：是
    factoring_business_relevance_yes = (By.XPATH, "//*[contains(text(),'是否关联方')]//parent::div//span[text()='是']")
    # 是否关联方：否
    factoring_business_relevance_no = (By.XPATH, "//*[contains(text(),'是否关联方')]//parent::div//span[text()='否']")

    # 印章类型 ：公章 合同专用章 财务专用章 法人名章 总经理亲笔签名 董事长亲笔签名 电子章
    factoring_business_seal_type = (By.XPATH, "//*[contains(text(),'印章类型')]//parent::div//"
                                              "input[@class='el-select__input is-medium']")
    # 点击印章：1公章 2合同专用章 3财务专用章 4法人名章 5总经理亲笔签名 6董事长亲笔签名 7电子章
    factoring_business_seal_type_choose = (By.XPATH, "//div[@x-placement='bottom-start']//li")
    # factoring_business_seal_type_choose = (By.XPATH, "//span[text()='公章']")
    # 印章公司
    factoring_business_seal_company = (By.XPATH, "//*[contains(text(),'印章公司')]//parent::div//input")
    # 选择印章公司：1、矩阵纵横设计股份有限公司 2、矩阵纵横设计股份有限公司成都分公司 3、深圳市矩阵鸣翠设计有限公司 4、深圳市释相艺术文化传播有限公司
    # 5、深圳市香蕉酱艺术传播有限公司 6、矩阵设计（北京）有限公司 7、矩阵纵横（上海）设计咨询有限公司 8、香港矩阵国际设计有限公司
    # 9、深圳矩阵纵横设计有限公司 10、深圳市合纵连横设计有限公司
    factoring_business_seal_company_choose = (By.XPATH, "//div[@x-placement='bottom-start']//li")
    # factoring_business_seal_company_choose = (By.XPATH, "//li[contains(text(),'1、矩阵纵横设计股份有限公司')]")
    # 文件份数
    factoring_business_file_attachments = (By.XPATH, "//input[@placeholder='请输入数字']")
    # 情况说明
    factoring_business_presentation = (By.XPATH, "//*[contains(text(),'情况说明')]//parent::div//*[@placeholder='请输入']")
    # 上传附件
    factoring_business_accessory = (By.XPATH, "//input[@name='file']")

    def test_factoring_business(self, username, password, value1, value2, value3, value4, value5, value6, value7,
                                value8, value9, value10):
        login = LoginPage(self.driver)  # 登录
        login.login_erp(username, password)  # 输入用户名、密码

        sleep(1)
        logger.info('不处理消息')
        self.click(matrix.home_page_messages_no)
        sleep(1)
        logger.info('点击合同管理')
        self.click(matrix.contract_management)
        logger.info('点击用印管理')
        self.click(matrix.using_management)
        logger.info('点击用印审批')
        self.click(matrix.factoring_business)
        sleep(1)
        # 选择用印单位
        logger.info('点击选择用印单位')
        self.click(FactoringBusiness.factoring_business_user_center)
        logger.info('选择登录用户对应的用印单位')
        self.click(FactoringBusiness.factoring_business_user_center1)
        # 选择紧急程度
        logger.info('选择用印紧急程度')
        self.click(FactoringBusiness.factoring_business_emergency_degree)
        # 选择文件类型
        logger.info('点击文件类型')
        self.click(FactoringBusiness.factoring_business_file_type)
        # 点击选择文件类型9、保理相关文件类型
        sleep(1)
        logger.info('点击选择文件类型9、保理相关文件类型')
        self.click_index(FactoringBusiness.factoring_business_labor_relations, value1)
        logger.info('输入用印事由名称')
        self.send_ks(FactoringBusiness.factoring_business_cause, value2)

        logger.info('输入交易对方')
        self.send_ks(FactoringBusiness.factoring_business_adverse, value3)
        logger.info('选择：东升室内装修设计有限公司')
        self.click(FactoringBusiness.factoring_business_choose_adverse)
        logger.info('点击项目名称')
        self.click(FactoringBusiness.factoring_business_project_name)
        logger.info('选择一个项目')
        self.click_index(FactoringBusiness.factoring_business_click_project_name, value4)
        logger.info('输入项目金额')
        self.send_ks(FactoringBusiness.factoring_business_input_money, value5)

        logger.info('选择印章类型')
        self.click(FactoringBusiness.factoring_business_seal_type)
        logger.info('选择印章')
        self.click_index(FactoringBusiness.factoring_business_seal_type_choose, value6)
        logger.info('点击印章公司')
        self.click(FactoringBusiness.factoring_business_seal_company)
        logger.info('选择印章公司：1、矩阵纵横设计股份有限公司')
        self.click_index(FactoringBusiness.factoring_business_seal_company_choose, value7)
        logger.info('输入文件份数')
        self.send_ks(FactoringBusiness.factoring_business_file_attachments, value8)
        logger.info('输入文件用途说明')
        self.send_ks(FactoringBusiness.factoring_business_presentation, value9)
        logger.info('上传文件')
        self.send_ks(FactoringBusiness.factoring_business_accessory, value10)
        sleep(3)
        logger.info('点击提交审批按钮')
        self.click(FactoringBusiness.submit_factoring_business)
        sleep(1)
        # logger.info('点击键盘确定“回车键”')
        # self.jp_qd()
