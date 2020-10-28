#!/usr/bin/python3
# @Time    : 2020-10-28
# @Author  : Kevin Kong (kfx2007@163.com)

# 顺丰新接口单元测试

import unittest
from sf.api import SF


class TestJson(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sf = SF("QXH", "yxGvL9y1bJj9mRy9rIjZVBK4nokAwxrf", True, "2.0")

    def test_signature(self):
        """测试数字签名"""
        sf = SF("test", "fjcg5PGKaNpPSHFAZ4QsCOkV71R3zVci", True)
        data = {"language": "zh-CN", "orderId": "QIAO-20200618-004"}
        timestamp = 12312334453453
        signature = sf.comm.get_signature(data, timestamp)
        self.assertEqual(signature, "IIKJtuLVzoFTu4kHI8M8vA==", signature)

    def test_create_order(self):
        """测试下单"""
        res = self.sf.order.create_order("zh_cn")
        self.assertEqual(res['apiResultCode'], "A1000", res)
        self.assertEqual(res['apiResultCode']['success'], True, res)


if __name__ == "__main__":
    unittest.main()
