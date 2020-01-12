"""
coding:utf-8
file: recharge_page.py
@author: virgil
@contact: XXXX@163.com
@time: 2020-01-05 16:20
@desc:
"""
import time
from Commons.base_page import Base_page
from Commons.xpath import Recharge_xpath


class Recharge_page(Base_page):
    # 进入充值页面
    def recharge_click(self):
        time.sleep(1)
        self.operate_click(Recharge_xpath.button_recharge, '进入充值--个人中心')

    # 输入金额
    def recharge_amount(self, datas):
        time.sleep(1)
        self.operate_send_key(Recharge_xpath.recharge_amount, '输入充值金额--充值', datas)
        self.operate_click(Recharge_xpath.button, '下一步--充值')

    # 获取弹窗文本
    def get_er_wins(self):
        time.sleep(1)
        text = self.get_element_text(Recharge_xpath.err_win, '获取错误窗口文本--充值')
        return text

    # 获取提示文本
    def get_er_tips(self):
        time.sleep(1)
        text = self.get_element_text(Recharge_xpath.err_info, '获取输入提示文本--充值')
        return text

    def get_new_wins_text(self):
        return self.get_element_text(Recharge_xpath.text, '获取充值成功后文本提示')

    def recharge_switch_wins(self):
        self.operate_switch_wins('切换到最新窗口')
