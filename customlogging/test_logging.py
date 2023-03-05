#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Crate Time: 2023/3/4 23:27
# Author: 93207


import logging
import logging.config
import os.path

import yaml
import datetime


#
# logconfig_dict = {
#     "version": 1,
#     "formatters": {
#         "default": {
#             "format": "%(asctime)s %(filename)s %(lineno)s %(levelname)s %(message)s"
#         },
#         'plain': {
#             "format": "%(message)s"
#         }
#     },
#
#     "handlers": {
#         "console": {
#             "class": "logging.StreamHandler",
#             "level": "INFO",
#             "formatter": "plain"
#         },
#         "file": {
#             "class": "logging.FileHandler",
#             "level": 20,
#             "filename": "./log.log",
#             "formatter": "default"
#         }
#     },
#     "loggers": {
#         "console_logger": {
#             "handlers": ["console", 'file'],
#             "level": "INFO",
#             "propagate": False
#         },
#         "file_logger": {
#             "handlers": ["file"],
#             "level": "DEBUG",
#             "propagate": False
#         }
#     },
#     "disable_existing_loggers": False
#
# }

def read_yaml_file(file_path):
    """
    :Author: 93207
    :CrateTime: 2023/3/5 21:55
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        current_time = datetime.datetime.now().strftime("%Y%m%d%H%M")
        log_name = list(data['loggers'].keys())[0]
        product_dir = os.path.dirname(data['handlers']['file']['filename'])
        log_file_path = f"{product_dir}/{log_name}_{current_time}.log"
        data['handlers']['file']['filename'] = log_file_path
    return data


from rich import print

logger_config_data = read_yaml_file("log_config.yaml")
print(logger_config_data)
logging.config.dictConfig(logger_config_data)
logger = logging.getLogger("process_logger")
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
