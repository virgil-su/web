"""
coding:utf-8
file: main.py
@author: virgil
@contact: XXXX@163.com
@time: 2020-01-07 14:10
@desc:
"""

import pytest

pytest.main(['-s',
             '-v',
             '-m', 'smoke',
             '--html=Reports/reports/test.html',
             '--reruns', '2',
             '--reruns-delay', '5',
             '--alluredir=Reports/allure'])
