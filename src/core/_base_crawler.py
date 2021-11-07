#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : EXP
# @Time   : 2020/4/25 22:17
# @File   : _base_crawler.py
# -----------------------------------------------

import os
from abc import ABCMeta, abstractmethod     # python不存在抽象类的概念， 需要引入abc模块实现
from src.cfg import env
from src.utils import log
from pypdm.dbc._sqlite import SqliteDBC
from src.bean.t_crawler import TCrawler
from src.dao.t_crawler import TCrawlerDao



class BaseCrawler:

    __metaclass__ = ABCMeta # 定义为抽象类

    def __init__(self, timeout=60, charset=env.CHARSET, options={}):
        self.timeout = timeout or 60
        self.charset = charset or env.CHARSET
        self.options = options


    @abstractmethod
    def NAME_CH(self):
        return '未知'


    @abstractmethod
    def NAME_EN(self):
        return 'unknow'


    @abstractmethod
    def HOME_PAGE(self):
        return 'https://exp-blog.com'


    def CACHE_PATH(self):
        return '%s/cache/%s.dat' % (env.PRJ_DIR, self.NAME_EN())


    def headers(self):
        return {
            'Accept' : '*/*',
            'Accept-Encoding' : 'gzip, deflate',
            'Accept-Language' : 'zh-CN,zh;q=0.9',
            'Connection' : 'keep-alive',
            'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
        }


    def crawl(self):
        log.info('<<<<<<<<<<<<<<<<<<')
        log.info('正在爬取 [%s] ...' % self.NAME_CH())

        try:
            cache_datas = self.crawl_data()
        except:
            cache_datas = []
            log.error('爬取 [%s]' % self.NAME_CH())

        # 数据入库
        dao = TCrawlerDao()
        sdbc = SqliteDBC(env.DB_PATH)
        sdbc.conn()
        for cache in cache_datas:
            self.to_db(sdbc, dao, cache)
        sdbc.close()

        log.info('得到 [%s] 数据 [%s] 条' % (self.NAME_CH(), len(cache_datas)))
        log.info('>>>>>>>>>>>>>>>>>>')
        return cache_datas


    @abstractmethod
    def crawl_data(self):
        # 爬取最新的数据（由子类爬虫实现）
        # TODO: in sub class
        return []       # cache_datas


    def to_db(self, sdbc, dao, cache):
        bean = TCrawler()
        bean.id = cache.id
        bean.num = cache.num
        bean.name = cache.name
        bean.url = cache.url
        dao.insert(sdbc, bean)
