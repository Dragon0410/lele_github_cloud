#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Crate Time: 2023/3/4 19:20
# Author: 93207

import toml


def read_toml_file(file_path):
    """
    :Author: 93207
    :CrateTime: 2023/3/4 19:20
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        data = toml.load(f)
    return data


def write_toml_file(file_path, data) -> bool:
    """
    :Author: 93207
    :CrateTime: 2023/3/4 19:21
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        toml.dump(data, f)
    return True


def main():
    pass


if __name__ == "__main__":
    main()
