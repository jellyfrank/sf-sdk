#!/usr/bin/python3
# @Time    : 2019-08-21
# @Author  : Kevin Kong (kfx2007@163.com)

import base64
from hashlib import md5
from lxml import etree


class Comm(object):
    """封装公共请求"""

    def __get__(self, instance, owner):
        self._clientcode = instance.clientcode
        self._checkword = instance.checkword
        return self

    def gen_verifycode(self, data):
        """
        生成校验码
        参数：
        data: 传输的报文
        """
        return base64.b64encode(md5(f"{self._checkword}{data}{self._checkword}".encode("utf-8")).digest()).decode("utf-8")

    def gen_xmldata(self, data):
        """
        生成xml报文
        """
        root = etree.Element("Request")
        root.set("service", data.get("service", None))
        root.set("lang", data.get("lang", "zh-CN"))
        head = etree.Element("Head")
        head.text = data.get("clientcode", self._clientcode)
        root.append(head)
        for key, value in data["data"].items():
            # 仅支持二级嵌套
            if type(value) is dict:
                el = etree.Element(key)
                for k, v in value.items():
                    if type(v) is dict:
                        el2 = etree.Element(k)
                        for name, att in v.items():
                            el2.set(name, att)
                        el.append(el2)
                    else:
                        el.set(k, v)
                root.append(el)
        return etree.tostring(root, xml_declaration=True, encoding="UTF-8")

    def post(self,xml,verifycode):
        """
        提交请求
        """
        
