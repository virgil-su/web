"""
coding:utf-8
file: xpath.py
@author: virgil
@contact: XXXX@163.com
@time: 2019-12-30 18:01
@desc:
"""

from selenium.webdriver.common.by import By


# 登陆页面元素
class Login_xpath:
    # 用户名输入
    user_name = (By.XPATH, '//input[@name="phone"]')
    # 用户密码输入
    user_pwd = (By.XPATH, '//input[@name="password"]')
    # 记住用户名
    record_user = (By.XPATH, '//input[@name="remember_me"]')
    # 找回密码
    retrieve_pwd = (By.XPATH, '//label[@class="right"]//a')
    # 注册
    register_user = (By.XPATH, '//div[@class="text-center"]//a')
    # 登陆按钮
    button_login = (By.XPATH, '//button')
    # 验证码
    vcode = (By.XPATH, '//input[@name="vcode"]')
    # 用户密码错误
    er_user_info = (By.XPATH, '//div[@class="layui-layer-content"]')
    # 用户输入有误
    er_user = (By.XPATH, '//div[@class="form-error-info"]')


# 主页面元素
class Home_xpath:
    # 用户退出按钮
    user_quit = (By.XPATH, '//span//a[text()="退出"]')
    # 用户昵称
    user_name = (By.XPATH, '//a[contains(text(),"我的帐户")]')
    # 登陆按钮
    user_login = (By.XPATH, '//a[text()="登录"]')
    # 首个投标金额文本
    loan_money = (By.XPATH, '//div[@class="b-unit"][1]//div[text()="借款金额"]/following-sibling::div')
    # 首个投标抢标
    home_bid = (By.XPATH, '//div[@class="b-unit"][1]//div//a')


# 投资
class Invest_xpath:
    # 输入框用户金币
    user_old_amount = (By.XPATH, '//div[@class="clearfix left"]//input')
    # 剩余投标金币
    residue_loan_amount = (By.XPATH, '//span[@class="mo_span4"]')
    # 借款总金币
    loan_amount = (By.XPATH, '//span[@class="mo_span2"]')
    # 投标按钮
    bid_button = (By.XPATH, '//button[@class="btn btn-special height_style"]')
    # 全投
    total_invest = (By.XPATH, '//input[@class="set-all"]')
    # 个人中心用户可用金额
    user_new_amount = (By.XPATH, '//li[@class="color_sub"]')
    # 投资成功查看激活
    invest_success = (By.XPATH, '//div[@id="layui-layer1"]//button')
    # 超出范围错误窗口
    invest_err_wins = (By.XPATH, '//div[@class="text-center"]')


# 找回密码页面元素
class Retrieve_pwd_xpath:
    # 标题
    retrieve_title = (By.XPATH, '//div[text()="找回密码"]')


# 注册用户页面元素
class Register_user_xpath:
    # 标题
    register_title = (By.XPATH, '//div[text()="注册"]')
    # 提示文本:服务协议
    register_SLA = (By.XPATH, '//a[text()="服务协议"]')


# 管理系统元素
class Admin_xpath:
    # 管理员账号密码
    admin_user = (By.XPATH, '//input[@name="admin_name"]')
    admin_pwd = (By.XPATH, '//input[@name="admin_pwd"]')
    # 验证码
    admin_code = (By.XPATH, '//input[@name="code"]')
    admin_button = (By.XPATH, '//p//button')
    loan_ifram = (By.XPATH, '//iframe[@id="mainFrame"]')
    # 分类:借款管理
    loan_admin = (By.XPATH, '//div[@id="_easyui_tree_15"]//span[@class="tree-title"]')
    # 加标
    loan_add_loan = (By.XPATH, '//a[@id="add"]//span[@class="l-btn-text"]')
    # 借款人
    loan_user = (By.XPATH, '//input[@id="RegName"]/following-sibling::span//input[@type="text"]')
    # 借款标题
    loan_title = (By.XPATH, '//td//input[@name="Title"]')
    # 利息
    loan_interest = (By.XPATH, '//td//input[@name="LoanRate"]')
    # 期限
    loan_limit_time = (By.XPATH, '//td//input[@name="LoanTerm"]')
    # 借款数量
    loan_number = (By.XPATH, '//td//input[@name="Amount"]')
    # 竞标天数
    loan_contend_time = (By.XPATH, '//td//input[@name="BiddingDays"]')
    # 选择借款用户
    loan_user_choose = (By.XPATH, '//tr[@id="datagrid-row-r2-2-0"]//div[text()="13800000000"]')
    # 风控评估
    loan_risk_assess = (By.XPATH, '//span[text()="风控评测"]')
    # 风险等级
    loan_risk_leve = (By.XPATH, '//td//input[@name="EvaluAmount"]')
    # 项目录入
    loan_project_info = (By.XPATH, '//span[text()="项目录入"]')
    # 户籍
    loan_native_place = (By.XPATH, '//input[@name="Native"]')
    # 职业
    loan_profession = (By.XPATH, '//input[@name="Profession"]')
    # 年龄
    loan_age = (By.XPATH, '//input[@name="Age"]')
    # 提交
    loan_submit = (By.XPATH, '//a[@id="add_do"]')
    # 选择借款时间审核
    loan_time = (By.XPATH, '//tr[@id="datagrid-row-r1-2-0"]//td[@field="CreateTime"]//div')
    # 审核
    loan_examine = (By.XPATH, '//a[@id="check"]//span[@class="l-btn-text"]')
    # 审核通过
    loan_examine_pass = (By.XPATH, '//span[text()="审核通过"]/ancestor::a')
    # 再次审核通过
    loan_examine_pass1 = (By.XPATH, '//span[text()="审核记录"]/ancestor::a')


# 充值
class Recharge_xpath:
    # 充值按钮
    button_recharge = (By.XPATH, '//button[@class="btn1"]')
    # 金额输入
    recharge_amount = (By.XPATH, '//input[@name="num"]')
    # 提示窗口
    err_win = (By.XPATH, '//div[@class="layui-layer-content"]')
    # 提示信息
    err_info = (By.XPATH, '//div[@class="form-error-info"]')
    # 下一步
    button = (By.XPATH, '//button')
    # 获取下一步新窗口文本
    text = (By.XPATH, '//body')


# 提现
class Extract_xpath:
    # 提现按钮
    button_extract = (By.XPATH, '//button[@class="btn2"]')
    # 提现输入
    extract_amount = (By.XPATH, '//input[@name="money"]')
    # 验证码输入
    code = (By.XPATH, '//input[@name="verify"]')
    # 下一步
    button = (By.XPATH, '//button')
    # 错误提示窗口
    err_wins = (By.XPATH, '//div[@class="layui-layer-content"]')
    # 提现成功
    extract_su = (By.XPATH, '//div[text()="提现成功"]')
    # 返回首页
    back_home = (By.XPATH, '//div[@class="reg-form"]//a')
    # 金币错误提示信息
    amount_err_info = (By.XPATH, '//div[@class="col-sm-9"]//div[@class="form-error-info"]')
    # 验证错误提示信息
    code_err_info = (By.XPATH, '//div[@class="col-sm-7 has-error"]//div[@class="form-error-info"]')
    # 个人用户最新可用金额
    user_new_amount = (By.XPATH, '//li[@class="color_sub"]')
