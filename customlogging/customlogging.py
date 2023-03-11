#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Crate Time: 2023/3/11 21:36
# Author: 93207

import os
import yaml
import logging
import datetime
import logging.config
from rich import print


class CustomLogging(object):
    def __init__(self, config_path):
        self.log_name = None
        if not os.path.exists(config_path):
            print(f"{config_path} 不存在")
            return
        self.config_data = self.read_yaml_config_file(config_path)
        logging.config.dictConfig(self.config_data)
        self.log = logging.getLogger(self.log_name)

    def read_yaml_config_file(self, config_path):
        """
        :Author: 93207
        :CrateTime: 2023/3/11 21:38
        """
        with open(config_path, 'r', encoding='utf-8') as f:
            ConfigData = yaml.safe_load(f)
            file_path = ConfigData['handlers']['file']['filename']
            self.log_name = ''.join(ConfigData['loggers'].keys())
            houzhui_name = os.path.splitext(file_path)[1]
            if not houzhui_name:  # 没有后缀，就是目录
                if not os.path.exists(file_path):  # 目录不存在
                    os.makedirs(file_path, exist_ok=True)
                current_datetime = datetime.datetime.now().strftime("%Y%m%d%H%M")
                log_filename = f"{file_path}/{self.log_name}_{current_datetime}.log"
                self._createfile(log_filename)
                ConfigData['handlers']['file']['filename'] = log_filename
            else:
                if not os.path.exists(file_path):
                    log_path = os.path.dirname(file_path)
                    if not os.path.exists(log_path):
                        os.makedirs(log_path, exist_ok=True)
                    self._createfile(log_path)

        return ConfigData

    def _createfile(self, filename):
        """
        :Author: 93207
        :CrateTime: 2023/3/11 22:09
        """
        with open(filename, 'w', encoding='utf-8') as f:
            pass
        return True


def main():
    path = "log_config.yaml"
    cl = CustomLogging(path)
    # cl.read_yaml_config_file(path)
    cl.log.debug("DEBUG")
    cl.log.info("INFO")


if __name__ == "__main__":
    main()
