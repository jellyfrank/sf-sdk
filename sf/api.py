#!/usr/bin/python3
# @Time    : 2019-08-21
# @Author  : Kevin Kong (kfx2007@163.com)

from sf.comm import Comm
from sf.order import Order
from sf.order import Sheet
import os
import csv


class SF(object):
    """顺丰SDK"""

    def __init__(self, clientcode, checkword, sandbox=False, language='zh-CN'):
        """
        初始化方法
        """
        self.clientcode = clientcode
        self.checkword = checkword
        self.sandbox = sandbox
        self.language = language

    comm = Comm()
    order = Order()
    sheet = Sheet()

    @classmethod
    def get_express_types(cls):
        express = []
        csv_path = os.path.dirname(__file__)
        with open(os.path.join(csv_path, "data/express_type.csv")) as f:
            for row in csv.reader(f):
                express.append((row[0], row[1], row[2]))
        return express