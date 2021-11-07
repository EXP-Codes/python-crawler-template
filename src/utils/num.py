#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : EXP
# -----------------------------------------------



def byte_to_str(value) :
    """
    byte 转 str。
    sqlite 入库类型为 TEXT 的数据会自动转为 byte，读取时要先转回来。
    :param value: byte 值
    :return: str 字符串
    """
    if isinstance(value, bytes) :
        value = bytes.decode(value)
    return value
