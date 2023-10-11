#!/usr/bin/python3
# @Time    : 2022-12-12
# @Author  : Kevin Kong (kfx2007@163.com)

MAPPING = {
    "Hong Kong":"香港",
    "Macau":"澳门"
}

class Address(object):

    def __init__(self,province=None,city=None,district=None,address=None,code=None):
        self.province = province
        self.city = city
        self.district = district
        self.address =address
        self.code = code

    def _convert(self,key):
        if key in MAPPING:
            return MAPPING[key]
        return key
    
    def to_dict(self):
        return {
            "province":self._convert(self.province),
            "city": self._convert(self.city),
            "district": self.district,
            "address": self.address,
            "code": self.code
        }