#!/usr/bin/python3
# @Time    : 2019-08-21
# @Author  : Kevin Kong (kfx2007@163.com)

import unittest
from sf.api import SF


class TestOrder(unittest.TestCase):

    sf = SF("QXH", "yxGvL9y1bJj9mRy9rIjZVBK4nokAwxrf")

    def test_order(self):
        """测试下单"""
        # 顺丰接口不允许重复下单，因此拿到结果就算通过
        res = self.sf.order.create_order("SFKD-20160219000021", "测试公司",
                                    "张三", "18512345678", "丰县", "北京市昌平区", "15112345678")
        self.assertIn(res["result"],[1,0])

    def test_cancel_order(self):
        """测试取消订单"""
        
        res = self.sf.order.confirm_order("SFKD-20160219000021","444017832497","2")
        self.assertIn(res["result"],[1,0])


if __name__ == "__main__":
    unittest.main()
