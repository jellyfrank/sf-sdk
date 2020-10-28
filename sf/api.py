#!/usr/bin/python3
# @Time    : 2019-08-21
# @Author  : Kevin Kong (kfx2007@163.com)

from sf.comm import Comm
# from sf.order import Order
from sf.order.abc_order import OrderFactory


class SF(object):
    """顺丰SDK"""

    def __init__(self, clientcode, checkword, sandbox=False, version="2.0"):
        """
        初始化方法
        params:
        version: 1.0使用xml报文格式, 2.0使用json数据格式
        """
        self.clientcode = clientcode
        self.checkword = checkword
        self.sandbox = sandbox
        self.version = version

    comm = Comm()
    order = OrderFactory()
