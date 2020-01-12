"""
coding:utf-8
file: test_1_login.py
@author: virgil
@contact: XXXX@163.com
@time: 2020-01-04 13:34
@desc:
"""
import time
import pytest
from Datas.all_datas import Login_datas as LD


@pytest.mark.usefixtures('login_start_end')
class Test_Login:
    # 正常登陆
    @pytest.mark.smoke
    def test_0_success(self, login_start_end):
        login_start_end[1].login_input_user(LD.normal_login['user'], LD.normal_login['pwd'])
        assert login_start_end[2].wait_element() == True
        assert login_start_end[0].current_url == LD.normal_login['url']

    # 正常进入忘记密码页面
    def test_1_retrieve_pwd(self, login_start_end):
        login_start_end[1].login_retrieve_pwd()
        assert login_start_end[0].current_url == LD.retrieve_pwd['url']

    # 正常进入注册页面
    def test_2_register_user(self, login_start_end):
        login_start_end[1].login_register_user()
        assert login_start_end[0].current_url == LD.register_user['url']

    # 不记住用户
    @pytest.mark.parametrize('datas', LD.record_user)
    def test_3_record_user(self, login_start_end, datas):
        login_start_end[1].login_record_user(datas['record'])
        login_start_end[1].login_input_user(datas['user'], datas['pwd'])
        login_start_end[2].wait_element()
        login_start_end[2].home_quit_user()
        login_start_end[2].home_login_user()
        time.sleep(3)
        text = login_start_end[1].login_user_vlaue(datas['class'])
        assert text == datas['user_name']

    # 输入错误提示
    @pytest.mark.parametrize('datas', LD.er_login2)
    def test_4_input_er(self, login_start_end, datas):
        login_start_end[1].login_input_user(datas['user'], datas['pwd'])
        text = login_start_end[1].login_input_er()
        assert text == datas['Tips']

    # 用户或者密码错误
    @pytest.mark.parametrize('datas', LD.er_login)
    def test_5_er(self, login_start_end, datas):
        login_start_end[1].login_input_user(datas['user'], datas['pwd'])
        text = login_start_end[1].login_er()
        assert text == datas['Tips']
