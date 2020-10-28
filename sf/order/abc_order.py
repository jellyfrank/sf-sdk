#!/usr/bin/python3
# @Time    : 2020-10-28
# @Author  : Kevin Kong (kfx2007@163.com)

# Abstract Order

from sf.comm import Comm
from .order import Order
from .new_order import NewOrder


class OrderFactory(object):

    def __get__(self,instance,owner):
        if instance.version == "1.0":
            order = Order()
        if instance.version == "2.0":
            order = NewOrder()
        
        order._clientcode = instance.clientcode
        order._checkword = instance.checkword
        order._sandbox = instance.sandbox
        order._version = instance.version
        return order
