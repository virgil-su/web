"""
coding:utf-8
file: base_page.py
@author: virgil
@contact: XXXX@163.com
@time: 2020-01-03 21:40
@desc:
"""
import datetime
import os
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Commons.log import log
from Commons.Path import img_path

class Base_page:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 等待元素
    def wait(self, xpath, page_name, timeout=10, poll_frequency=0.5):
        try:
            log.info('等待{}页面中元素{}出现'.format(page_name, xpath))
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(xpath))
        except:
            log.exception('{}页面中元素: {}不可见或不存在'.format(page_name, xpath))
            page_name = page_name + '元素:{}不可见或不存在'.format(xpath)
            self._save_img(page_name)

    # 截图页面
    def _save_img(self, page_name):
        try:
            log.info('截图报错页面{}'.format(page_name))
            time_end = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            self.driver.save_screenshot(os.path.join(img_path, page_name + time_end + '.png'))
        except:
            log.exception('{}页面截图失败'.format(page_name))

    # 获取元素对象
    def get_element_obj(self, xpath, page_name, timeout=10, poll_frequency=0.5):
        self.wait(xpath, page_name, timeout, poll_frequency)
        try:
            log.info('{}页面-获取元素对象: {}'.format(page_name, xpath))
            return self.driver.find_element(*xpath)
        except:
            log.exception('{}页面-元素对象: {}获取失败'.format(page_name, xpath))
            page_name = page_name + '元素对象:{}获取失败'.format(xpath)
            self._save_img(page_name)

    # 获取元素属性值
    def get_element_vlaue(self, xpath, page_name, class_name, timeout=10, poll_frequency=0.5):
        em = self.get_element_obj(xpath, page_name, timeout, poll_frequency)
        try:
            log.info('{}页面-元素对象: {}获取属性{}值'.format(page_name, xpath, class_name))
            text=em.get_attribute(class_name)
            return text
        except:
            log.exception('{}页面-元素对象: {}获取属性{}值失败'.format(page_name, xpath, class_name))
            page_name = page_name + '元素对象:{}获取属性{}值失败'.format(xpath, class_name)
            self._save_img(page_name)

    # 获取属性文本信息
    def get_element_text(self, xpath, page_name, timeout=10, poll_frequency=0.5):
        em = self.get_element_obj(xpath, page_name, timeout, poll_frequency)
        try:
            log.info('{}页面-元素对象: {}获取文本'.format(page_name, xpath))
            return em.text
        except:
            log.exception('{}页面-元素对象: {}获取文本值失败'.format(page_name, xpath))
            page_name = page_name + '{}获取文本值失败'.format(xpath)
            self._save_img(page_name)

    # 元素点击操作
    def operate_click(self, xpath, page_name, timeout=10, poll_frequency=0.5):
        em = self.get_element_obj(xpath, page_name, timeout, poll_frequency)
        try:
            log.info('{}页面-元素: {}操作点击'.format(page_name, xpath))
            em.click()
        except:
            log.exception('{}页面-元素: {}操作点击失败'.format(page_name, xpath))
            page_name = page_name + '元素:{}操作点击失败'
            self._save_img(page_name)

    # 元素输入操作
    def operate_send_key(self, xpath, page_name, content, timeout=10, poll_frequency=0.5):
        em = self.get_element_obj(xpath, page_name, timeout, poll_frequency)
        try:
            log.info('{}页面-元素: {}输入内容{}'.format(page_name, xpath, content))
            em.send_keys(content)
        except:
            log.exception('{}页面-元素: {}输入内容失败'.format(page_name, xpath))
            page_name = page_name + '元素:{}输入内容{}失败'.format(xpath, content)
            self._save_img(page_name)

    # 切换ifram
    def operate_switch_ifram(self, xpath, page_name):
        em=self.get_element_obj(xpath,page_name)
        try:
            log.info('{}页面-元素: {}切换ifram'.format(page_name, xpath))
            self.driver.switch_to.frame(em)
        except:
            log.exception('{}页面-元素: {}切换ifram失败'.format(page_name, xpath))
            page_name = page_name + '{}切换ifram失败'.format(page_name, xpath)
            self._save_img(page_name)

    # 切换到初始ifram
    def operate_default_ifram(self, xpath, page_name):
        self.wait(xpath, page_name)
        try:
            log.info('{}页面-元素: {}切换初始ifram'.format(page_name, xpath))
            self.driver.switch_to.default_content()
        except:
            log.exception('{}页面-元素: {}切换初始ifram失败'.format(page_name, xpath))
            page_name = page_name + '{}切换初始ifram失败'.format(page_name, xpath)
            self._save_img(page_name)

    # 获取浏览器所有窗口
    def get_all_windows(self, page_name):
        try:
            log.info('获取浏览器所有窗口对象')
            wins = self.driver.window_handles
            return wins
        except:
            log.exception('{}-获取浏览器窗口对象失败'.format(page_name))
            page_name = page_name + '-获取浏览器窗口对象失败'
            self._save_img(page_name)

    # 切换浏览器窗口
    def operate_switch_wins(self, page_name):
        wins = self.get_all_windows(page_name)
        try:
            log.info('切换到{}窗口')
            self.driver.switch_to.window(wins[-1])
        except:
            log.exception('切换到{}窗口失败'.format(page_name))
            page_name = '切换到{}窗口失败'.format(page_name)
            self._save_img(page_name)

    # 获取选项框是否勾选
    def get_element_selected(self, xpath, page_name):
        em = self.get_element_obj(xpath, page_name)
        try:
            log.info('判断元素是否勾选;是返回true,否则flase')
            return em.is_selected()
        except:
            log.exception('判断元素是否勾选失败')
            page_name = page_name + '判断元素是否勾选失败'
            self._save_img(page_name)
