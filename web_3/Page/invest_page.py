"""
coding:utf-8
file: invest_page.py
@author: virgil
@contact: XXXX@163.com
@time: 2020-01-04 19:01
@desc:
"""
import time
from Commons.base_page import Base_page
from Commons.xpath import Invest_xpath, Home_xpath, Login_xpath
from Datas.all_datas import Login_datas


class Invest_page(Base_page):
    # 登陆并投首标
    def invst_user_login(self):
        time.sleep(1)
        self.operate_click(Home_xpath.user_login, '登陆用户--主页')
        time.sleep(1)
        self.operate_send_key(Login_xpath.user_name, '输入用户名--登陆', Login_datas.normal_login['user'])
        time.sleep(1)
        self.operate_send_key(Login_xpath.user_pwd, '输入密码--登陆', Login_datas.normal_login['pwd'])
        time.sleep(1)
        self.operate_click(Login_xpath.button_login, '登陆用户--登陆')
        time.sleep(1)
        self.operate_click(Home_xpath.home_bid, '抢首标--主页')

    # 获取用户初始金币与借款总额
    def get_old_amount(self, data):
        time.sleep(1)
        user_old_amount = float(self.get_element_vlaue(Invest_xpath.user_old_amount, '获取用户未投资金币--投资', data))
        time.sleep(1)
        loan_all_amount = float(self.get_element_text(Invest_xpath.loan_amount, '获取总借款总金额--投资')) * 10000
        time.sleep(1)
        return user_old_amount, loan_all_amount

    # 获取最新得用户金额与剩余借款金额
    def get_new_amount(self):
        time.sleep(1)
        user_new_amount = self.get_element_text(Invest_xpath.user_new_amount, '获取用户最新可用金币--个人中心').split('元')
        time.sleep(1)
        user_new_amount = float(user_new_amount[0])
        time.sleep(1)
        self.driver.back()
        self.driver.refresh()
        time.sleep(1)
        loan_amount = float(self.get_element_text(Invest_xpath.residue_loan_amount, '获取剩余投资金额--投资')) * 10000
        return loan_amount, user_new_amount

    # 输入投资金额
    def invest_loan(self, data):
        time.sleep(1)
        self.operate_send_key(Invest_xpath.user_old_amount, '输入投资金额--投资', data)

    # 提交投资金额
    def invest_click(self):
        time.sleep(1)
        self.operate_click(Invest_xpath.bid_button, '点击投资')

    # 查看投资结果
    def check_invest(self):
        time.sleep(1)
        self.operate_click(Invest_xpath.invest_success, '查看投资激活')

    # 输入投资金额错误提示
    def input_er_tips(self):
        time.sleep(1)
        text = self.get_element_text(Invest_xpath.bid_button, '获取输入错误提示--投资')
        return text

    # 输入投资金额超出范围提示
    def er_wins_tips(self):
        time.sleep(1)
        text = self.get_element_text(Invest_xpath.invest_err_wins, '输入超出范围--投资')
        return text
