"""
coding:utf-8
file: test_3_extract.py
@author: virgil
@contact: XXXX@163.com
@time: 2020-01-05 18:35
@desc:
"""

import pytest
from Datas.all_datas import Extract_datas


@pytest.fixture()
def user_input(recharge_extract):
    recharge_extract[1].extract_click()
    assert user_input[2].current_url == Extract_datas.url
    yield recharge_extract


class Test_Extract:
    # 正常提现
    @pytest.mark.smoke
    @pytest.mark.usefixtures('recharge_extract')
    def test_0_extract_success(self, recharge_extract):
        old_amount = recharge_extract[1].get_user_amount()
        recharge_extract[1].extract_click()
        assert recharge_extract[2].current_url == Extract_datas.url
        recharge_extract[1].extract_amount(Extract_datas.normal[0]['amount'])
        recharge_extract[1].send_key_code(Extract_datas.normal[0]['code'])
        assert recharge_extract[2].current_url == Extract_datas.normal[0]['url']
        text = recharge_extract[1].get_extract_su()
        assert text == Extract_datas.normal[0]['tips']
        new_amount = recharge_extract[1].get_user_amount()
        assert (old_amount - new_amount) == float(Extract_datas.normal[0]['amount'])

    # 输入错误
    @pytest.mark.parametrize('datas', Extract_datas.unusual)
    def test_1_extract_er_info(self, user_input, datas):
        user_input[1].extract_amount(datas['amount'])
        user_input[1].send_key_code(datas['code'])
        text = user_input[1].get_er_info()
        assert text[0] == datas['tips']
        assert text[1] == datas['tips1']

    # 输入不规范
    @pytest.mark.parametrize('datas',Extract_datas.not_normal)
    def test_1_extract_er_wins(self, user_input,datas):
        user_input[1].extract_amount(datas['amount'])
        user_input[1].send_key_code(datas['code'])
        text = user_input[1].get_er_wins()
        assert text == datas['tips']
