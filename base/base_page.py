# @time    : 2021/3/30 1:35
# @author  :Mr_Li
# _*_coding:utf-8_*_
# @FileName: base_page.py
import time

from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from pykeyboard import PyKeyboard
import win32api
import win32con
import os

import log
from base.base_util import logger


class BasePage:

    def __init__(self, driver):

        self.driver = driver

    def open_url(self, url):
        """
        打开url站点 :param url:
        """
        self.driver.get(url)

    # 定义定位元素关键字方法
    def locator_element(self, loc):
        return self.driver.find_element(*loc)

    # 定义点击
    def click(self, loc):
        self.locator_element(loc).click()

    # 定位一组元素
    def locator_elements(self, loc):
        return self.driver.find_elements(*loc)

    # 定一组义点击
    def click_index(self, loc, index):
        return self.locator_elements(loc)[index].click()

    # 截图
    def take_screenshot(self):
        """
        截图并保存在根目录下的Screenshots文件夹下  :param none:
        """
        file_path = os.path.dirname(os.getcwd()) + '/Screenshots'
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("开始截图并保存")

        except Exception as e:
            logger.error("出现异常", format(e))
    # def find_element(self, by, locator, timeout=30):
    #     """ 定位单个元素  :param by: 定位方式 eg:By.ID   :param locator: 定位表达式
    #     :param timeout: 显示等待超时时间    :return: """
    #     try:
    #         element = WebDriverWait(self.driver, timeout).\
    #             until(lambda driver: driver.find_element(by, locator))
    #     except (NoSuchElementException, TimeoutException) as e:
    #         raise e
    #     else:
    #         return element
    #
    # def find_elements(self, by, locator, timeout=30):
    #     """ 定位一组元素       :param by: 定位方式 eg:By.ID       :param locator: 定位表达式
    #     :param timeout: 显示等待超时时间        :return:        """
    #     try:
    #         elements = WebDriverWait(self.driver, timeout).\
    #             until(lambda driver: driver.find_elements(by, locator))
    #     except (NoSuchElementException, TimeoutException) as e:
    #         raise e
    #     else:
    #         return elements

    # 定义设置值
    def send_ks(self, loc, value):
        self.locator_element(loc).send_keys(value)

    # 定义进入一个框架
    def sw_to(self, frame_name):
        self.driver.switch_to.frame(frame_name)

    # 定义出框架
    def qu_to(self):
        self.driver.switch_to.default_content()

    # 定义下拉框
    def ComboBox(self, loc, value):
        xs0l = Select(self.locator_element(loc))
        xs0l.select_by_visible_text(value)

    # 定义获取文本的值
    def gt_text(self, loc):
        # 获取到值后再反馈出来用.text
        return self.locator_element(loc).text

    # 定义清空输入框
    def clear_sz(self, loc):
        self.locator_element(loc).clear()

    # 定义弹窗确定
    def alt_qd(self):
        alt = self.driver.switch_to.alert
        alt.accept()

    # 获取弹窗文字
    def alt_get(self):
        alt = self.driver.switch_to.alert

    # 定义键盘确定
    def keyboard_enter(self):

        k = PyKeyboard()
        k.press_key(k.return_key)

    # 定义断言
    def equal(self, a, b, msg):
        try:
            assert a == b
            if msg:
                print(msg)
        except AssertionError:
            print(f'断言失败:预期结果[a=b],实际结果:a={a},b={b}')

    # 定义打印日志
    def logger(self):
        logger = log.Log().Logger
        return self.logger

    # 定义鼠标滚轮滚动(向上滚动)
    def mouse_wheel_up(self):
        for i in range(1, 1500):
            win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, 1)

    # 定义鼠标滚轮滚动(向下滚动)
    def mouse_wheel1_down(self):
        for i in range(1, 1000):
            win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -1)

    def getSelectElementWithIndex(self, index_num):
        # 获取select下拉框元素---index
        select_element = Select(self.locator_element('//select'))
        # 打印已选中的文本
        print(select_element.all_selected_options[0].text)
        return select_element.select_by_index(index_num)

    def getSelectElementWithText(self, text):
        # 获取select下拉框元素----text
        select_element = Select(self.locator_element('//select'))
        # 打印已选中的文本
        print(select_element.all_selected_options[0].text)
        return select_element.select_by_visible_text(text)

    def getSelectElementWithValue(self, value):
        # 获取select下拉框元素---value
        select_element = Select(self.locator_element('select'))
        # 打印已选中的文本
        print(select_element.all_selected_options[0].text)
        return select_element.select_by_value(value)

    def get_visible_element(self, locator, timeout=20):
        """
        获取可视元素
        param loctor: By方法定位元素，如(By.XPATH, "//*[@text='照片']")
        return：返回可见元素
        """
        try:
            return WebDriverWait(self.driver, timeout).until(
                ec.visibility_of_element_located(locator)
            )
        except Exception as e:
            # 截图、日志
            Screenshots(self.driver, "获取可视元素失败").screen_shot()
            logger.error("获取可视元素失败：{}".format(e))

    def get_presence_element(self, locator, timeout=20):
        """获取存在元素"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                ec.presence_of_element_located(locator)
            )
        except Exception as e:
            Screenshots(self.driver, "获取存在元素失败").screen_shot()
            logger.error("获取存在元素失败：{}".format(e))

    def get_click_element(self, locator, timeout=20):
        """获取可点击元素"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                ec.element_to_be_clickable(locator)
            )
        except Exception as e:
            Screenshots(self.driver, "获取可点击元素失败").screen_shot()
            logger.error("可点击元素获取失败：{}".format(e))

    def getElementExistance(self, *loc):
        """通过元素xpath判断是否存在该元素,存在返回true，不存在返回false"""
        flag = True
        try:
            # 尝试寻找元素，如若没有找到则会抛出异常
            self.locator_element(loc)
        except:
            flag = False
        return flag
