#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : EXP
# -----------------------------------------------
# 生成 pdm 代码
# -----------------------------------------------


from pypdm.dbc._sqlite import SqliteDBC
from pypdm.builder import build
from src.cfg import env
from src.utils import log



def main() :
    log.info('+++++++++++++++++++++++++++++++++++++++')
    build(
        dbtype = 'sqlite',
        dbname = env.DB_PATH,
        charset = env.CHARSET,
        pdm_pkg = 'src',
        table_whitelist = [],
        table_blacklist = [],
        to_log = False
    )
    log.info('---------------------------------------')



def init() :
    log.init()
    sdbc = SqliteDBC(env.DB_PATH)
    sdbc.exec_script(env.SQL_PATH)



if __name__ == "__main__" :
    init()
    try :
        main()
    except :
        log.error('生成 pdm 代码失败')