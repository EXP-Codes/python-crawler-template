#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------
# DAO: t_crawler
# -------------------------------

from ..bean.t_crawler import TCrawler
from pypdm.dao._base import BaseDao


class TCrawlerDao(BaseDao) :
    TABLE_NAME = 't_crawler'
    SQL_COUNT = 'select count(1) from t_crawler'
    SQL_TRUNCATE = 'truncate table t_crawler'
    SQL_INSERT = 'insert into t_crawler(i_num, s_name, s_url) values(?, ?, ?)'
    SQL_DELETE = 'delete from t_crawler where 1 = 1 '
    SQL_UPDATE = 'update t_crawler set i_num = ?, s_name = ?, s_url = ? where 1 = 1 '
    SQL_SELECT = 'select i_id, i_num, s_name, s_url from t_crawler where 1 = 1 '

    def __init__(self) :
        BaseDao.__init__(self)

    def _to_bean(self, row) :
        bean = None
        if row:
            bean = TCrawler()
            bean.id = self._to_val(row, 0)
            bean.num = self._to_val(row, 1)
            bean.name = self._to_val(row, 2)
            bean.url = self._to_val(row, 3)
        return bean
