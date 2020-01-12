"""
coding:utf-8
file: test_4_recharge.py
@author: virgil
@contact: XXXX@163.com
@time: 2020-01-05 17:25
@desc:
"""
import pytest
from Datas.all_datas import Recharge_datas

@pytest.fixture()
def user_recharge(recharge_extract):
    # 进入充值页面
    recharge_extract[0].recharge_click()
    # 断言url
    assert recharge_extract[2].current_url == Recharge_datas.recharge_url
    yield recharge_extract


class Test_recharge:
    # 正常充值
    @pytest.mark.smoke
    def test_0_recharge_success(self, user_recharge):
        assert user_recharge[2].current_url == Recharge_datas.recharge_url
        user_recharge[0].recharge_amount(Recharge_datas.normal[0]['amount'])
        user_recharge[0].recharge_switch_wins()
        text = user_recharge[0].get_new_wins_text()
        assert text == Recharge_datas.normal[0]['tips']

    # 输入有误提示弹窗
    @pytest.mark.parametrize('datas', Recharge_datas.unusual)
    def test_1_recharge_er_info(self, user_recharge, datas):
        user_recharge[0].recharge_amount(datas['amount'])
        text = user_recharge[0].get_er_wins()
        assert text == datas['tips']

    # 输入有误提示输入内容
    @pytest.mark.parametrize('datas', Recharge_datas.not_normal)
    def test_2_recharge_er_wins(self, user_recharge, datas):
        user_recharge[0].recharge_amount(datas['amount'])
        text = user_recharge[0].get_er_tips()
        assert text == datas['tips']
