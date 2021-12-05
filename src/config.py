#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : EXP
# -----------------------------------------------

import os
import yaml
PRJ_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


SQL_PATH = '%s/script/crawler-create.sql' % PRJ_DIR
SETTINGS_PATH = '%s/config/settings.yml' % PRJ_DIR


class Config :

    def __init__(self, settings_path) -> None:
        with open(settings_path, 'r') as file:
            self.settings = yaml.safe_load(file.read())
            self.base = self.settings.get('base')
            self.charset = self.base.get('charset')
            self.database = self.settings.get('database')


settings = Config(SETTINGS_PATH)