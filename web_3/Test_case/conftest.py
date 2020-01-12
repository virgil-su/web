"""
coding:utf-8
file: conftest.py
@author: virgil
@contact: XXXX@163.com
@time: 2020-01-04 16:40
@desc:
"""
import pytest
from selenium import webdriver
from Datas.all_datas import Login_datas, Loan_datas, Recharge_datas
from Page.login_page import Login_page
from Page.home_page import Home_page
from Page.admin_page import Admin_page
from Page.invest_page import Invest_page
from Page.recharge_page import Recharge_page
from Page.extract_page import Extract_page


@pytest.fixture
def start_end():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


# 登陆前置后置
@pytest.fixture('function')
def login_start_end(start_end):
    start_end.get(Login_datas.login_url)
    Lp = Login_page(start_end)
    Hp = Home_page(start_end)
    yield start_end, Lp, Hp


# 投资前置后置
@pytest.fixture
def invest_start_end(start_end):
    Ap = Admin_page(start_end)
    Ap.add_loan(Loan_datas.loan_datas)
    start_end.get(Loan_datas.home_url)
    Inp = Invest_page(start_end)
    yield start_end, Inp


# 充值与提现前置后置
@pytest.fixture
def recharge_extract(start_end):
    start_end.get(Recharge_datas.url)
    Home_page(start_end).home_login_user()
    Login_page(start_end).login_input_user(Login_datas.normal_login['user'], Login_datas.normal_login['pwd'])
    Home_page(start_end).home_user_click()
    assert start_end.current_url == Recharge_datas.user_url
    Rp = Recharge_page(start_end)
    Ep = Extract_page(start_end)
    yield Rp, Ep, start_end
