# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals


import log_conf
import data
import conf

from sklearn import tree


def run():
    # 开始运行
    log_conf.logger.info("user_pos matching starting...")

