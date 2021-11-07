#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : EXP
# -----------------------------------------------

import os
PRJ_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)
CHARSET = 'utf-8'

SQL_PATH = '%s/script/crawler-create.sql' % PRJ_DIR
DB_PATH =  '%s/data/crawler.db' % PRJ_DIR


