#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author@zhanwang.xie

import logging
from config.config import Params
import os
import time


class LogOutput:

    @classmethod
    def create_logger(cls):
        # 创建日志收集器
        log = logging.getLogger()
        # 设置info日志级别(输入)
        log.setLevel(Params.log_level)
        standard_format = '[%(asctime)s] [%(threadName)s:%(thread)d] [task_id:%(name)s] [%(filename)s:%(lineno)d] [%(levelname)s] %(message)s'
        simple_format = '[%(asctime)s] [task_id:%(name)s] [%(levelname)s]  [%(filename)s:%(lineno)d] %(message)s'
        logfile_formater = logging.Formatter(standard_format)
        console_formater = logging.Formatter(simple_format)
        # 创建日志输出渠道
        # 1. 输出到控制台
        console = logging.StreamHandler()
        # 设置控制台输出日志级别（输出）设置输出日志格式
        console.setLevel('INFO')
        console.setFormatter(console_formater)
        # 将输出渠道添加到日志收集器中
        log.addHandler(console)
        # 2. 输出到文件
        upper_path = Params.output_path + "\\log\\"
        if not os.path.exists(upper_path):
            os.makedirs(upper_path)
        time_now = time.strftime("%Y%m%d_%H%M%S")
        log_path = upper_path + 'burn_test' + '_' + time_now + ".log"
        log_file = logging.FileHandler(filename=log_path, encoding='utf-8')
        # 设置输出日志级别（输出）设置输出日志格式
        log_file.setLevel(Params.log_level)
        log_file.setFormatter(logfile_formater)
        # 将输出渠道添加到日志收集器中
        log.addHandler(log_file)
        return log
log = LogOutput().create_logger()

if __name__ == '__main__':
    log.info('test')
