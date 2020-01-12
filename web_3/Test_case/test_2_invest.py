"""
coding:utf-8
file: test_2_invest.py
@author: virgil
@contact: XXXX@163.com
@time: 2020-01-04 16:29
@desc:
"""

import pytest
from Datas.all_datas import Invest_data


@pytest.fixture
def login_user(invest_start_end):
    invest_start_end[1].invst_user_login()
    yield invest_start_end

class Test_invest:
    # 正常投资
    @pytest.mark.smoke
    def test_invest_success(self, login_user):
        old_amount = login_user[1].get_old_amount(Invest_data.invest['class_name'])
        user_old_amount = old_amount[0]
        loan_all_amount = old_amount[1]
        login_user[1].invest_loan(Invest_data.invest['amount'])
        login_user[1].invest_click()
        login_user[1].check_invest()
        new_amount = login_user[1].get_new_amount()
        loan_amount = new_amount[0]
        user_new_amount = new_amount[1]
        assert user_old_amount != user_new_amount
        assert (user_old_amount - user_new_amount) == (float(Invest_data.invest['amount']))
        assert loan_amount != loan_all_amount
        assert (loan_all_amount - loan_amount) == (float(Invest_data.invest['amount']))

    # 输入异常
    @pytest.mark.parametrize('datas',Invest_data.invest_er1)
    def test_invest_input(self, login_user,datas):
        login_user[1].invest_loan(datas['amount'])
        text = login_user[1].input_er_tips()
        assert text == datas['tips']

    # 输入超出
    @pytest.mark.parametrize('datas', Invest_data.invest_er2)
    def test_invest_err(self, login_user,datas):
        login_user[1].invest_loan(datas['amount'])
        login_user[1].invest_click()
        text = login_user[1].er_wins_tips()
        assert text == datas['tips']
