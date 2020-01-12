"""
coding:utf-8
file: Upload.py
@author: virgil
@contact: XXXX@163.com
@time: 2020-01-03 21:13
@desc:
"""

import win32gui, win32con


def upload(path, driver='chrome'):
    if driver == 'chrome':
        title = '打开'
    else:
        title = '打开'
    # 找到类型为#32770的窗口,标题为: title
    wins_32770 = win32gui.FindWindow('#32770', title)
    # 在#32770窗口下找到ComboBxEx32层级;
    # 参数1:查找对象; 参数2:0-查找所有同层级; 参数3:查找层级名str 参数4:层级标题
    ComboBxEx32 = win32gui.FindWindowEx(wins_32770, 0, 'ComboBoxEx32', None)
    # 在ComboBxEx32层级下找到ComboBox层级;
    ComboBox = win32gui.FindWindowEx(ComboBxEx32, 0, 'ComboBox', None)
    # 在ComboBox层级下找到Edit层级
    Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)
    # 在#32770层级下找到Button层级
    Button = win32gui.FindWindowEx(wins_32770, 0, 'Button', '打开(&O)')
    # 在Edit层级下输入内容; 参数1:层次对象 参数2:输入行为 参数4:输入内容
    win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, path)
    # 在Edit层级下输入内容; 参数1:层次对象 参数2:点击行为 参数4:点击的对象
    win32gui.SendMessage(wins_32770, win32con.WM_COMMAND, 1, Button)


if __name__ == '__main__':
    upload(r'F:\ningmengban\NMB1\1.txt')
