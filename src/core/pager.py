#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : EXP
# -----------------------------------------------
# 从数据库读取最新数据生成 GitHub Pages
# -----------------------------------------------

import time
from pypdm.dbc._sqlite import SqliteDBC
from src.bean.t_crawler import TCrawler
from src.dao.t_crawler import TCrawlerDao
from src.cfg import env
from src.utils import log

HTML_HOME_PATH = '%s/docs/home.html' % env.PRJ_DIR
TPL_HOME_PATH = '%s/tpl/home.tpl' % env.PRJ_DIR
TPL_HEAD_PATH = '%s/tpl/head.tpl' % env.PRJ_DIR
TPL_TAIL_PATH = '%s/tpl/tail.tpl' % env.PRJ_DIR
TPL_TABLE_PATH = '%s/tpl/table.tpl' % env.PRJ_DIR
TPL_ROW_PATH = '%s/tpl/row.tpl' % env.PRJ_DIR


def to_page(cache=[], limit=500) :
    sdbc = SqliteDBC(env.DB_PATH)
    sdbc.conn()
    _to_page(HTML_HOME_PATH, sdbc, TCrawler.i_num, True, limit)
    # FIXME: 若有多个页面则生成多次
    sdbc.close()

    
def _to_page(savepath, sdbc, column, order, limit, condition='') :
    tpl_home, tpl_head, tpl_tail, tpl_table, tpl_row = load_tpl()
    datas = query_data(sdbc, column, order, limit, condition)
    rows = []
    for data in datas:
        row = tpl_row % {
            'img_url': data.url or '',
            'num': data.num or 0,
            'name': data.name or '',
            'data_url': data.url or ''
        }
        rows.append(row)

    table = tpl_table % {
        'rows': '\n'.join(rows)
    }

    home = tpl_home % {
        'head': tpl_head, 
        'tail': tpl_tail, 
        'datetime': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) ,
        'limit': limit, 
        'table': table
    }

    create_html(home, savepath)
    log.info('生成页面 [%s] 成功' % savepath)


def load_tpl() :
    with open(TPL_HOME_PATH, 'r', encoding=env.CHARSET) as file:
        tpl_home = file.read()

    with open(TPL_HEAD_PATH, 'r', encoding=env.CHARSET) as file:
        tpl_head = file.read()

    with open(TPL_TAIL_PATH, 'r', encoding=env.CHARSET) as file:
        tpl_tail = file.read()

    with open(TPL_TABLE_PATH, 'r', encoding=env.CHARSET) as file:
        tpl_table = file.read()

    with open(TPL_ROW_PATH, 'r', encoding=env.CHARSET) as file:
        tpl_row = file.read()

    return tpl_home, tpl_head, tpl_tail, tpl_table, tpl_row


def query_data(conn, column, order, limit, condition='') :
    dao = TCrawlerDao()
    sort_by = 'asc' if order else 'desc'
    where = " %s order by %s %s limit %i" % (condition, column, sort_by, limit)
    sql = TCrawlerDao.SQL_SELECT + where
    beans = []
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            bean = dao._to_bean(row)
            beans.append(bean)
        cursor.close()
    except:
        log.error("从表 [%s] 查询数据失败" % TCrawler.table_name)
    return beans


def create_html(data, savepath) :
    with open(savepath, 'w+', encoding=env.CHARSET) as file:
        file.write(data)


