#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : EXP
# -----------------------------------------------

import os
import erb.yml as yaml
PRJ_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)
CHARSET = 'utf-8'
SETTINGS_PATH = '%s/config/settings.yml' % PRJ_DIR


class Config :

    def __init__(self, settings_path, charset) -> None:
        with open(settings_path, 'r', encoding=charset) as file:
            self.settings = yaml.load(file.read())
            self.base = self.settings.get('base')
            self.charset = self.base.get('charset')
            self.database = self.settings.get('database')


settings = Config(SETTINGS_PATH, CHARSET)