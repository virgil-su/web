"""
coding:utf-8
file: Path.py
@author: virgil
@contact: XXXX@163.com
@time: 2020-01-03 20:53
@desc:
"""
import os

# 工程目录
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 日志输出路径
log_path = os.path.join(path, 'Reports')
# 测试报告输出路径
reports_path = os.path.join(log_path, 'reports')
# 错误截图路径
img_path = os.path.join(log_path, 'img')
# 测试案例路径
case_path = os.path.join(path, 'Test_case')
