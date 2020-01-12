"""
coding:utf-8
file: all_datas.py
@author: virgil
@contact: XXXX@163.com
@time: 2019-12-30 17:21
@desc:
"""


# 登陆页面用例数据
class Login_datas:
    login_url = 'http://120.78.128.25:8765/Index/login.html'
    # 正常登陆
    normal_login = {"user": "13760246701", "pwd": "python", 'url': 'http://120.78.128.25:8765/Index/index'}
    # 记住用户
    record_user = [
        {"user": "13760246701", "pwd": "python", 'class': 'value', 'record': True, 'user_name': '13760246701'},
        {"user": "13760246701", "pwd": "python", 'class': 'value', 'record': False, 'user_name': ''}]
    # 用户名或密码输入有误
    er_login = [{"user": "13760246701", "pwd": "111111111", 'Tips': '帐号或密码错误!'},
                {"user": "13760246111", "pwd": "python", 'Tips': '此账号没有经过授权，请联系管理员!'}]
    # 用户名或密码输入不规范
    er_login2 = [{"user": "", "pwd": "", 'Tips': '请输入手机号'}, {"user": "", "pwd": "python", 'Tips': '请输入手机号'},
                 {"user": "13760246701", "pwd": "", 'Tips': '请输入密码'},
                 {"user": "137602467011", "pwd": "python", 'Tips': '请输入正确的手机号'},
                 {"user": "1376024670", "pwd": "python", 'Tips': '请输入正确的手机号'}]
    # 找回密码
    retrieve_pwd = {'url': 'http://120.78.128.25:8765/Index/find_pwd.html'}
    # 注册
    register_user = {'url': 'http://120.78.128.25:8765/Index/reg.html'}


# 创建借款表单
class Loan_datas:
    home_url = 'http://120.78.128.25:8765/Index/index'
    loan_datas = {'user': '13800000000',
                  'title': '约么',
                  'interest': '10',
                  'limit_time': '2',
                  'loan_number': '1000000',
                  'contend_time': '1',
                  'level': '1',
                  'native_place': '广东',
                  'profession': '养猪',
                  'age': '18',
                  'admin_user': 'lemon7',
                  'admin_pwd': 'lemonbest',
                  'code': 'hapi',
                  'url': 'http://120.78.128.25:8765/Admin/Index/login.html'}


class Invest_data:
    invest_er2 = [{'amount': '7000000', 'tips': '购买标的金额不能大于标总金额'},
                  {'amount': '20000000', 'tips': '投标金额大于可用金额'},
                  {'amount': '-10', 'tips': '请正确填写投标金额'},
                  {'amount': '0', 'tips': '请正确填写投标金额'}, ]
    invest_er1 = [{'amount': '1', 'tips': '请输入10的整数倍'},
                  {'amount': '0.1', 'tips': '请输入10的整数倍'},
                  {'amount': '99', 'tips': '请输入10的整数倍'},
                  {'amount': 'ASDF', 'tips': '请输入10的整数倍'}, ]
    invest = {'amount': '500000.0', 'class_name': 'data-amount'}


class Recharge_datas:
    url = 'http://120.78.128.25:8765/Index/index.html'
    user_url = 'http://120.78.128.25:8765/Member/index.html'
    recharge_url = 'http://120.78.128.25:8765/Member/recharge'
    normal = [{'amount': '100', 'tips': '支付接口已经关闭或者维护中,请稍后再试'},
              {'amount': '500', 'tips': '支付接口已经关闭或者维护中,请稍后再试'}]
    unusual = [{'amount': '-10', 'tips': '充值金额不能小于100'},
               {'amount': '0.1', 'tips': '充值金额不能小于100'},
               {'amount': '1', 'tips': '充值金额不能小于100'},
               {'amount': '50', 'tips': '充值金额不能小于100'}]
    not_normal = [{'amount': 'asdf', 'tips': '充值金额只能包含数字'},
                  {'amount': 'ads100', 'tips': '充值金额只能包含数字'},
                  {'amount': '阿斯蒂芬', 'tips': '充值金额只能包含数字'},
                  {'amount': '!@#%$%^*(()||', 'tips': '充值金额只能包含数字'},
                  {'amount': '', 'tips': '请输入充值金额'}]


class Extract_datas:
    url = 'http://120.78.128.25:8765/Member/withdraw'
    normal = [{'amount': '1', 'code': 'hapi',
               'url': 'http://120.78.128.25:8765/Member/withdraw_success.html?[object%20Object]', 'tips': '提现成功',
               'tips1': '提现申请成功'},
              {'amount': '0.1', 'code': 'hapi',
               'url': 'http://120.78.128.25:8765/Member/withdraw_success.html?[object%20Object]', 'tips': '提现成功',
               'tips1': '提现申请成功'},
              {'amount': '100', 'code': 'hapi',
               'url': 'http://120.78.128.25:8765/Member/withdraw_success.html?[object%20Object]', 'tips': '提现成功',
               'tips1': '提现申请成功'},
              {'amount': '0.12', 'code': 'hapi',
               'url': 'http://120.78.128.25:8765/Member/withdraw_success.html?[object%20Object]', 'tips': '提现成功',
               'tips1': '提现申请成功'}, ]
    unusual = [{'amount': 'asdf.', 'code': '123456', 'tips': '提现金额只能是数字，最多包含两位小数点', 'tips1': '请输入4位短信验证码'},
               {'amount': '0.123', 'code': '123', 'tips': '提现金额只能是数字，最多包含两位小数点', 'tips1': '请输入4位短信验证码'},
               {'amount': '-10', 'code': '', 'tips': '提现金额只能是数字，最多包含两位小数点', 'tips1': '请输入短信验证码'},
               {'amount': '', 'code': 'hapi', 'tips': '请输入提现金额', 'tips1': ''}]
    not_normal = [{'amount': '0', 'code': 'hapi', 'tips': '参数缺失'},
                  {'amount': '1000000000', 'code': 'hapi', 'tips': '提现金额不可大于可提现额度'},
                  {'amount': '1000', 'code': '1234', 'tips': '短信验证码超时，请重新获取'}, ]
