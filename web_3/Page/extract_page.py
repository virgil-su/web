"""
coding:utf-8
file: extract_page.py
@author: virgil
@contact: XXXX@163.com
@time: 2020-01-05 17:14
@desc:
"""
import time
from Commons.base_page import Base_page
from Commons.xpath import Extract_xpath, Home_xpath


class Extract_page(Base_page):
    # 进入提现页面
    def extract_click(self):
        self.operate_click(Extract_xpath.button_extract, '进入提现页面--个人')

    # 输入提现金额
    def extract_amount(self, datas):
        self.operate_send_key(Extract_xpath.extract_amount, '输入提现金额--提现', datas)

    # 输入验证码信息
    def send_key_code(self, datas):
        self.operate_send_key(Extract_xpath.code, '输入验证码--提现', datas)
        self.operate_click(Extract_xpath.button, '确认提现--提现')
        time.sleep(2)

    # 提现成功
    def get_extract_su(self):
        text = self.get_element_text(Extract_xpath.extract_su, '提现成功提示--提现成功')
        time.sleep(2)
        self.operate_click(Extract_xpath.back_home, '返回主页--提现成功')
        self.operate_click(Home_xpath.user_name, '进入个人中心--主页')
        return text

    # 获取个人中心金额
    def get_user_amount(self):
        text = self.get_element_text(Extract_xpath.user_new_amount, '获取最新用户金额--个人')
        text = float(text.split('元')[0])
        return text

    # 获取错误弹窗文本内容
    def get_er_wins(self):
        text = self.get_element_text(Extract_xpath.err_wins, '获取错误提示弹窗文本--提现')
        return text

    # 获取错误提示文本
    def get_er_info(self):
        text = self.get_element_text(Extract_xpath.amount_err_info, '获取金币错误提示文本--提现')
        text1 = self.get_element_text(Extract_xpath.code_err_info, '获取验证码错误提示文本--提现')
        return text, text1
