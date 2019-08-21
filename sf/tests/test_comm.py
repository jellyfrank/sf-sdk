#!/usr/bin/python3
# @Time    : 2019-08-21
# @Author  : Kevin Kong (kfx2007@163.com)

import unittest
from sf.api import SF


class TestComm(unittest.TestCase):

    def test_verifycode(self):
        """测试校验码"""
        sf = SF("QXH", "yxGvL9y1bJj9mRy9rIjZVBK4nokAwxrf")
        print(sf.comm.gen_verifycode(None))

    def test_xmldata(self):
        """测试报文生成格式"""
        sf = SF("QXH", "yxGvL9y1bJj9mRy9rIjZVBK4nokAwxrf")
        data = {
            "service": "服务名",
            "clientcode": "顾客编码",
            "data": {
                "Order":{
                    "orderid":"TEST20180410001",
                    "Cargo":{
                        "name":"手机"
                    }
                }
            }
        }

        print(sf.comm.gen_xmldata(data))


if __name__ == "__main__":
    unittest.main()
