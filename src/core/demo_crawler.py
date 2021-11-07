#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : EXP
# -----------------------------------------------
# 爬虫示例
# -----------------------------------------------

import requests
import json
from bs4 import BeautifulSoup
from src.core._base_crawler import BaseCrawler
from src.bean.cache_info import CacheInfo
from src.utils import log


class DemoCrawler(BaseCrawler):

    def __init__(self, options):
        BaseCrawler.__init__(self, options=options)
        self.name_ch = '爬虫示例'
        self.name_en = 'demo'
        self.home_page = 'https://exp-blog.com'


    def NAME_CH(self):
        return self.name_ch


    def NAME_EN(self):
        return self.name_en


    def HOME_PAGE(self):
        return self.home_page


    def crawl_data(self):
        response = requests.get(
            self.home_page,
            headers = self.headers(),
            params = self.options,
            timeout = self.timeout
        )

        cache_datas = []
        if response.status_code == 200:
            response.encoding = response.apparent_encoding

            # FIXME: 默认二选一，解析 json
            json_text = response.text
            json_obj = json.loads(json_text)
            items = json_obj.get('items')
            for item in items :
                cache = self.to_cache(item)
                cache_datas.append(cache)
                # log.debug(cache)

            # FIXME: 默认二选一，解析 html
            html_text = response.text
            soup = BeautifulSoup(html_text, "html.parser")
            items = soup.find_all(class_="items")
            for item in items :
                cache = self.to_cache(item)
                cache_datas.append(cache)
                # log.debug(cache)
        else:
            log.warn('获取 [%s] 数据失败： [HTTP Error %i]' % (self.NAME_CH(), response.status_code))
        return cache_datas


    def to_cache(self, item):
        cache = CacheInfo()
        # FIXME: 把数据格式化到缓存
        return cache

