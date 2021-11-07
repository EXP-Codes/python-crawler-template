#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : EXP
# -----------------------------------------------


import hashlib
from src.cfg import env


class CacheInfo:

    def __init__(self):
        self.id = 0
        self.num = 0
        self.name = ''
        self.url = ''


    def is_vaild(self):
        return not not self.name


    def MD5(self):
        if not self.md5:
            data = '%s%s%s' % (self.num, self.name, self.url)
            self.md5 = hashlib.md5(data.encode(encoding=env.CHARSET)).hexdigest()
        return self.md5


    def to_html(self):
        return '<br/>'.join([
            "<br/>==============================================",
            "[<b>编号</b>] <font color='blue'>%s</font>" % self.num,
            "[<b>名称</b>] %s" % self.name,
            "[<b>图片</b>] %s" % self.url
        ])


    def __str__(self):
        return self.__repr__()


    def __repr__(self):
        return '\n'.join([
            "\n==============================================",
            "[ 编号 ] %s" % self.num,
            "[ 名称 ] %s" % self.name,
            "[ 图片 ] %s" % self.url
        ])

