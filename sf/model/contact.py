#!/usr/bin/python3
# @Time    : 2022-12-03
# @Author  : Kevin Kong (kfx2007@163.com)

from copy import copy

class ContactInfo(object):

    def __init__(self, address, conuntry='CN', contactType=2, company=None, contact=None, mobile=None, zoneCode=None, province=None, city=None, postCode=None, email=None, taxNo=None):
        self.address = address
        self.conuntry = conuntry
        self.contactType = contactType
        self.company = company
        self.contact = contact
        self.mobile = mobile
        self.zoneCode = zoneCode
        self.province = province
        self.city = city
        self.postCode = postCode
        self.email = email
        self.taxNo = taxNo

    def to_dict(self):
        res = {
            "address":self.address,
            "conuntry":self.conuntry,
            "contactType":self.contactType,
            "company":self.company,
            "contact":self.contact,
            "mobile":self.mobile,
            "zoneCode":self.zoneCode,
            "province":self.province,
            "city":self.city,
            "postCode":self.postCode,
            "email":self.email,
            "taxNo":self.taxNo,
        }

        copy_data = copy(res)
        for k, v in copy_data.items():
            if v is None:
                res.pop(k)
        return res