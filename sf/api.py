#!/usr/bin/python3
# @Time    : 2019-08-21
# @Author  : Kevin Kong (kfx2007@163.com)

from sf.comm import Comm
from sf.order import Order
from sf.order import Sheet

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
