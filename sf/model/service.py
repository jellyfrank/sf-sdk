#!/usr/bin/python3
# @Time    : 2022-12-03
# @Author  : Kevin Kong (kfx2007@163.com)

from copy import copy

class Service(object):

    def __init__(self, name, value=None, value1=None, value2=None, value3=None, value4=None):
        self.name = name
        self.value = value
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
        self.value4 = value4

    def to_dict(self):
        res = {
            "name": name,
            "value": value,
            "value1": value1,
            "value2": value2,
            "value3": value3,
            "value4": value4,
        }

        copy_data = copy(res)
        for k, v in copy_data.items():
            if v is None:
                res.pop(k)
        return res