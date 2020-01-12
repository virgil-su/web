"""
coding:utf-8
file: home_page.py
@author: virgil
@contact: XXXX@163.com
@time: 2020-01-04 14:32
@desc:
"""
from Commons.base_page import Base_page
from Commons.xpath import Home_xpath
import time


class Home_page(Base_page):
    # 等用户名与退出按钮出现
    def wait_element(self):
        try:
            self.wait(Home_xpath.user_name, '用户名--主页')
            self.wait(Home_xpath.user_quit, '退出按钮--主页')
            return True
        except:
            return False

    # 点击退出用户
    def home_quit_user(self):
        time.sleep(1)
        self.operate_click(Home_xpath.user_quit, '退出用户--主页')

    # 点击登陆用户
    def home_login_user(self):
        time.sleep(1)
        self.operate_click(Home_xpath.user_login, '登陆用户--主页')

    def home_user_click(self):
        time.sleep(1)
        self.operate_click(Home_xpath.user_name, '用户中心--主页')
