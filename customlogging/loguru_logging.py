#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: king
# create: 2023/2/24 下午9:59

import os
import datetime
import sys

from loguru import logger


class LoguruLogger():
    def __init__(self, log_name='logs', log_path="logs", log_level='DEBUG',
                 log_format=None, log_rotation="500MB", log_retention="7 days",
                 log_encoding='utf-8'):

        if not os.path.exists(log_path):
            os.makedirs(log_path)

        if not log_format:
            log_format = "{time:YYYY-MM-DD HH:mm:ss} [{level}] From {file}({line}): {message}"

        now_time_string = datetime.datetime.now().strftime("%Y%m%d")
        debug_log_file = os.path.join(log_path,
                                      f"debug_{log_name}_{now_time_string}.log")
        error_log_file = os.path.join(log_path,
                                      f"error_{log_name}_{now_time_string}.log")
        info_log_file = os.path.join(log_path,
                                     f"info_{log_name}_{now_time_string}.log")
        self.logger = logger
        self.logger.remove()
        self.logger.add(debug_log_file,
                        level=log_level,
                        format=log_format,
                        filter=lambda x: x['level'].name == "DEBUG",
                        rotation=log_rotation,
                        retention=log_retention,
                        enqueue=True,
                        backtrace=True,
                        encoding=log_encoding)

        self.logger.add(info_log_file,
                        level=log_level,
                        format=log_format,
                        filter=lambda x: x['level'].name == "INFO",
                        rotation=log_rotation,
                        retention=log_retention,
                        enqueue=True,
                        backtrace=True,
                        encoding=log_encoding)

        self.logger.add(error_log_file,
                        level=log_level,
                        format=log_format,
                        filter=lambda x: x['level'].name not in ["DEBUG",
                                                                 "INFO"],
                        rotation=log_rotation,
                        retention=log_retention,
                        enqueue=True,
                        backtrace=True,
                        encoding=log_encoding)

        self.logger.add(sys.stderr,
                        level='INFO',
                        format="{time:YYYY-MM-DD HH:mm:ss} [{level}]: {message}",
                        )


def main():
    ll = LoguruLogger()
    ll.logger.info("测试")
    ll.logger.debug("debg")
    ll.logger.error('cuowu')
    ll.logger.critical('无法私服')


if __name__ == "__main__":
    main()
