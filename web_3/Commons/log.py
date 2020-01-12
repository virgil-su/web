"""
coding:utf-8
file: log.py
@author: virgil
@contact: XXXX@163.com
@time: 2020-01-03 20:59
@desc:
"""
import logging
import os
from Commons.Path import log_path


class Log:
    @classmethod
    def logs(cls, log_name=None, file_name=None):
        if log_name is None:
            log_name = 'virgil'
        if file_name is None:
            file_name = 'ui_test.log'
        format_str = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(name)s:%(levelname)s: %(message)s'
        log_format = logging.Formatter(format_str)
        log = logging.getLogger(log_name)
        log.setLevel('DEBUG')
        output = logging.StreamHandler()
        output.setLevel('INFO')
        output.setFormatter(log_format)
        log.addHandler(output)
        output_file = logging.FileHandler(os.path.join(log_path, file_name), 'w', encoding='utf8')
        output_file.setLevel('INFO')
        output_file.setFormatter(log_format)
        log.addHandler(output_file)
        return log


log = Log.logs()

if __name__ == '__main__':
    log.info('年后')
