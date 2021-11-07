#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : EXP
# -----------------------------------------------

import sys
from pypdm.dbc._sqlite import SqliteDBC
from src.core.demo_crawler import DemoCrawler
from src.cfg import env
from src.core import pager
from src.utils import log


def help_info() :
    return '''
-h           查看帮助信息
-p <pages>   爬取页数，默认 10
-z <zone>    指定爬取地区
'''


def main(is_help, pages, zone) :
    if is_help :
        log.info(help_info())
        return

    log.info('+++++++++++++++++++++++++++++++++++++++')
    options = {
        'pages': pages, 
        'zone': zone
    }
    crawlers = [ 
        DemoCrawler(options=options), 
        # .... 其他爬虫的实现类
    ]

    all_cache_datas = []
    for crawler in crawlers:
        cache_datas = crawler.crawl()
        if cache_datas:
            all_cache_datas.extend(cache_datas)

    if all_cache_datas:
        pager.to_page(all_cache_datas)
    log.info('---------------------------------------')



def init() :
    log.init()
    sdbc = SqliteDBC(env.DB_PATH)
    sdbc.exec_script(env.SQL_PATH)


def sys_args(sys_args) :
    is_help = False
    pages = 10
    zone = 'CN'

    idx = 1
    size = len(sys_args)
    while idx < size :
        try :
            if sys_args[idx] == '-h' or sys_args[idx] == '--help' :
                is_help = True
                break

            elif sys_args[idx] == '-p' or sys_args[idx] == '--pages' :
                idx += 1
                pages = int(sys_args[idx])

            elif sys_args[idx] == '-z' or sys_args[idx] == '--zone' :
                idx += 1
                zone = sys_args[idx]
        except :
            pass
        idx += 1
    return is_help, pages, zone



if __name__ == "__main__" :
    init()
    try :
        main(*sys_args(sys.argv))
    except :
        log.error('未知异常')