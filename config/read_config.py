#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Crate Time: 2023/3/2 19:55
# Author: 93207
# Describe: 重写字符串拼接方法，使 Yaml 配置文件像 Python 的 字符串类型的 join 函数方法，支持对字符串和变量的拼接

import yaml
from rich import print


def join(loader, node):
    seq = loader.construct_sequence(node)
    return ' '.join([str(i) for i in seq])


yaml.add_constructor('!join', join)


def read_yaml_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = yaml.unsafe_load(f)
    return data


def main():
    file_path = "config.yaml"
    configData = read_yaml_file(file_path)
    print(configData)

    # import string
    # a = string.Template("${s1} ${s2}").safe_substitute(s1="wang", s2="lele")
    # print(a)
    # a = lambda x: "3" + "4"
    # print(a(3))


if __name__ == "__main__":
    main()
