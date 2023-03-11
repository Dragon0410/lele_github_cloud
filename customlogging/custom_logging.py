#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Crate Time: 2023/3/4 21:27
# Author: 93207

import os
import yaml
import logging
import datetime
import logging.handlers
import logging.config


class CustomLogging(object):
    def __init__(self, config_path):
        self.log_name = None
        if os.path.exists(config_path):
            print(f"{config_path} 不存在")
            return

        self.config = self.read_log_config_yaml(config_path)
        logging.config.dictConfig(self.config)
        self.log = logging.getLogger(self.log_name)

    def read_log_config_yaml(self, config_path):
        with open(config_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        config_log_path = data['handlers']['file']['filename']
        self.log_name = ''.join(self.config['loggers'].keys())

        houzhui_name = os.path.splitext(config_log_path)[1]
        print("不是常规的日志文件：", houzhui_name)
        if houzhui_name:  # 有文件后缀
            if not os.path.exists(config_log_path):
                # 不存在此文件，就创建空文件
                create_file_handler = open(config_log_path, 'w', encoding='utf-8')
                create_file_handler.close()
            data['handlers']['file']['filename'] = config_log_path
            return data
        # 没有文件后缀，就是目录
        if not os.path.exists(config_log_path):
            if not os.path.exists(config_log_path):
                os.makedirs(config_log_path, exist_ok=True)
            current_datetime = datetime.datetime.now().strftime("%Y%m%d%H%M")
            log_filename = f"{config_log_path}/{self.log_name}_{current_datetime}.log"
            data['handlers']['file']['filename'] = log_filename
        return data


def main():
    config_log_path = "log_config.yaml"
    cl = CustomLogging(config_log_path)
    cl.log.debug("DEBUG")
    cl.log.info("INFO")


if __name__ == "__main__":
    main()
