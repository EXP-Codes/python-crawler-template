#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : EXP
# -----------------------------------------------

import argparse
import sys
from pypdm.dbc._sqlite import SqliteDBC
from src.core.demo_crawler import DemoCrawler
from src import config
from src.core import pager
from color_log.clog import log


def args() :
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        prog='Python 爬虫开发模板',
        description='使用此模板可以快速搭建一个爬虫框架', 
        epilog='\r\n'.join([
            '示例: ', 
            '  单机连续帧识别模式：python main.py', 
            '  单机连续帧模式：python main.py -m alone -f', 
            '  单机截屏识别模式：python main.py -m alone', 
            '  联机模式：python main.py -m duplex -r ai', 
            '  联机模式：python main.py -m duplex -r ctrl', 
            '',
            '（单机模式只支持【无边框全屏】或【窗口】，联机模式只支持【无边框全屏】或【全屏】模式）'
        ])
    )
    parser.add_argument('-p', '--pages', dest='pages', type=int, default=10, help='爬取页数')
    parser.add_argument('-z', '--zone', dest='zone', type=str, default='china', help='爬取地区')
    return parser.parse_args()



def main(args) :
    log.info('+++++++++++++++++++++++++++++++++++++++')
    options = {
        # 爬虫参数，按需替换
        # ... ...
        'pages': args.pages, 
        'zone': args.zone
    }
    crawlers = [ 
        DemoCrawler(options=options), 
        # ... ... 其他爬虫的实现类
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
    sdbc = SqliteDBC(options=config.settings.database)
    sdbc.conn()
    sdbc.exec_script(config.settings.base['sqlpath'])
    sdbc.close()



if __name__ == "__main__" :
    try :
        init()
        main(args())
    except :
        log.error('未知异常')