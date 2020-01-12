"""
coding:utf-8
file: admin_page.py
@author: virgil
@contact: XXXX@163.com
@time: 2020-01-04 17:03
@desc:
"""
import time
import random
from Commons.base_page import Base_page
from Commons.xpath import Admin_xpath


class Admin_page(Base_page):
    # 登陆后台系统
    def admin_login(self, datas):
        self.driver.get(datas['url'])
        self.operate_send_key(Admin_xpath.admin_user, '输入管理名--后台系统', datas['admin_user'])
        time.sleep(1)
        self.operate_send_key(Admin_xpath.admin_pwd, '输入管理员密码--后台系统', datas['admin_pwd'])
        time.sleep(1)
        self.operate_send_key(Admin_xpath.admin_code, '输入验证码--后台系统', datas['code'])
        time.sleep(1)
        self.operate_click(Admin_xpath.admin_button, '登陆管理员--后台系统')

    # 进入借款管理分类
    def loan_admin(self):
        time.sleep(1)
        self.operate_click(Admin_xpath.loan_admin, '选择借款管理--后台系统')
        time.sleep(1)
        self.operate_switch_ifram(Admin_xpath.loan_ifram, '切换到借款ifram窗口--后台系统')

    # 创建标
    def create_loan(self, datas):
        time.sleep(1)
        self.operate_click(Admin_xpath.loan_add_loan, '创建加标--加标')
        time.sleep(1)
        self.operate_send_key(Admin_xpath.loan_user, '填写借款人--借款信息', datas['user'])
        time.sleep(1)
        self.operate_click(Admin_xpath.loan_user_choose, '选择用户信息--借款信息')
        time.sleep(1)
        self.operate_send_key(Admin_xpath.loan_title, '填写借款标题--借款信息', datas['title'])
        time.sleep(1)
        self.operate_send_key(Admin_xpath.loan_interest, '填写利息--借款信息', datas['interest'])
        time.sleep(1)
        self.operate_send_key(Admin_xpath.loan_limit_time, '借款期限--借款信息', datas['limit_time'])
        time.sleep(1)
        self.operate_send_key(Admin_xpath.loan_number, '借款额度--借款信息', datas['loan_number'])
        time.sleep(1)
        self.operate_send_key(Admin_xpath.loan_contend_time, '竞标期限--借款信息', datas['contend_time'])
        time.sleep(1)
        self.operate_click(Admin_xpath.loan_risk_assess, '进入风控评测')
        time.sleep(1)
        self.operate_send_key(Admin_xpath.loan_risk_leve, '填写等级--风控评测', datas['level'])
        time.sleep(1)
        self.operate_click(Admin_xpath.loan_project_info, '进入项目录入')
        time.sleep(1)
        self.operate_send_key(Admin_xpath.loan_native_place, '输入户籍--项目录入', datas['native_place'])
        time.sleep(1)
        self.operate_send_key(Admin_xpath.loan_profession, '输入职业--项目录入', datas['profession'])
        time.sleep(1)
        self.operate_send_key(Admin_xpath.loan_age, '输入年龄--项目录入', datas['age'])
        time.sleep(1)
        self.operate_click(Admin_xpath.loan_submit, '提交加标--项目录入')

    # 审核标
    def examine_loan(self):
        time.sleep(1)
        self.operate_click(Admin_xpath.loan_time, '选择借款时间')
        time.sleep(1)
        self.operate_click(Admin_xpath.loan_examine, '进入审核')
        time.sleep(1)
        self.operate_click(Admin_xpath.loan_examine_pass, '初次审核通过')
        time.sleep(1)
        self.operate_click(Admin_xpath.loan_time, '选择借款时间')
        time.sleep(1)
        self.operate_click(Admin_xpath.loan_examine, '进入审核')
        time.sleep(1)
        self.operate_click(Admin_xpath.loan_examine_pass, '再次审核通过')
        time.sleep(1)
        self.operate_click(Admin_xpath.loan_time, '选择借款时间')
        time.sleep(1)
        self.operate_click(Admin_xpath.loan_examine, '进入审核')
        time.sleep(1)
        self.operate_click(Admin_xpath.loan_examine_pass, '最后审核通过')

    @staticmethod
    def number_random():
        number = random.sample('0123456', 3)
        number = ''.join(number)
        newnumber = int(number) * 10000
        return newnumber

    def add_loan(self, datas):
        amount = self.number_random()
        datas['loan_number'] = amount
        self.admin_login(datas)
        self.loan_admin()
        self.create_loan(datas)
        self.examine_loan()
