"""
coding:utf-8
file: login_page.py
@author: virgil
@contact: XXXX@163.com
@time: 2020-01-03 23:23
@desc:
"""
from Commons.base_page import Base_page
from Commons.xpath import Login_xpath
import time


class Login_page(Base_page):
    # 输入用户密码并登陆
    def login_input_user(self, user, pwd):
        self.operate_send_key(Login_xpath.user_name, '输入用户名--登陆', user)
        time.sleep(1)
        self.operate_send_key(Login_xpath.user_pwd, '输入密码--登陆', pwd)
        time.sleep(1)
        self.operate_click(Login_xpath.button_login, '点击登陆--登陆')
        time.sleep(1)

    # 进入找回密码页面
    def login_retrieve_pwd(self):
        self.operate_click(Login_xpath.retrieve_pwd, '找回密码--登陆')
        time.sleep(3)

    # 进入注册密码页面
    def login_register_user(self):
        self.operate_click(Login_xpath.register_user, '注册用户--登陆')
        time.sleep(3)

    # 记住用户名选择
    def login_record_user(self, record=True):
        if record is False:
            if self.get_element_selected(Login_xpath.record_user, '记住密码--登陆'):
                self.operate_click(Login_xpath.record_user, '取消记住用户--登陆')
        if record:
            if self.get_element_selected(Login_xpath.record_user, '记住密码--登陆') is False:
                self.operate_click(Login_xpath.record_user, '记住用户--登陆')
        time.sleep(3)

    # 获取输入格式错误的提示
    def login_input_er(self):
        text = self.get_element_text(Login_xpath.er_user, '输入格式错误--登陆')
        time.sleep(2)
        return text

    # 获取用户或密码错误的提示
    def login_er(self):
        text = self.get_element_text(Login_xpath.er_user_info, '用户或密码错误--登陆')
        return text

    # 获取用户输入元素属性值
    def login_user_vlaue(self, class_name):
        text = self.get_element_vlaue(Login_xpath.user_name, '获取用户账号值--登陆', class_name)
        time.sleep(3)
        return text
