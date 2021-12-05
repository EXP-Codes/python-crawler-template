#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : EXP
# -----------------------------------------------
# 生成 pdm 代码
# -----------------------------------------------


from pypdm.dbc._sqlite import SqliteDBC
from pypdm.builder import build
from src import config
from src.utils import log



def main() :
    log.info('+++++++++++++++++++++++++++++++++++++++')
    sdbc = SqliteDBC(options=config.settings.database)
    sdbc.conn()
    sdbc.exec_script(config.SQL_PATH)
    build(
        dbc = sdbc,
        pdm_pkg = 'src',
        table_whitelist = [],
        table_blacklist = [],
        to_log = False
    )
    sdbc.close()
    log.info('---------------------------------------')



if __name__ == "__main__" :
    log.init()
    try :
        main()
    except :
        log.error('生成 pdm 代码失败')