#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------
# PDM: t_crawler
# -------------------------------

class TCrawler :
    table_name = 't_crawler'
    i_id = "i_id"
    i_num = "i_num"
    s_name = "s_name"
    s_url = "s_url"


    def __init__(self) :
        self.id = None
        self.num = None
        self.name = None
        self.url = None


    def params(self) :
        return (
            self.num,
            self.name,
            self.url,
        )


    def __repr__(self) :
        return '\n'.join(
            (
                '%s: {' % self.table_name,
                "    %s = %s" % (self.i_id, self.id),
                "    %s = %s" % (self.i_num, self.num),
                "    %s = %s" % (self.s_name, self.name),
                "    %s = %s" % (self.s_url, self.url),
                '}\n'
            )
        )
