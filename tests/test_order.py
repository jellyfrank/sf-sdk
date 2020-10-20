#!/usr/bin/python3
# @Time    : 2019-08-21
# @Author  : Kevin Kong (kfx2007@163.com)

import unittest
from sf.api import SF
from autils import String
import pytest


class TestOrder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sf = SF("QXH", "yxGvL9y1bJj9mRy9rIjZVBK4nokAwxrf", True)
        cls.order_no = String.generate_digits(12)
        cls.mail_no = None

    def test_1_create_order(self):
        """测试下单"""
        res = self.sf.order.create_order(self.order_no, "测试公司",
                                         "张三", "18512345678", "丰县", "北京市昌平区", "15112345678")
        self.assertEqual(res["result"], 0, res)

    def test_2_get_order(self):
        """测试订单查询接口"""
        res = self.sf.order.get_order(self.order_no)
        self.assertEqual(res["result"], 0, res)

    def test_3_cancel_order(self):
        """测试取消订单"""
        res = self.sf.order.confirm_order(self.order_no, dealtype="2")
        self.assertEqual(res["result"], 0, res)

    def test_4_get_router(self):
        """测试路由信息"""
        # 只有先下单 才能拿得到路由信息 否则是空
        # data = self.sf.order.create_order(String.generate_digits(12), "测试公司",
        #                                   "张三", "18512345678", "丰县", "北京市昌平区", "15112345678")
        # mail_no = data["data"]["OrderResponse"]["mailno"]
        res = self.sf.order.get_route_info('444020261358')
        # 顺丰路由 节点80为签收标识
        self.assertTrue(len(res["data"]["RouteResponse"]["Route"]) > 1, res)

    def test_5_can_deliver(self):
        """是否可以收派"""
        res = self.sf.order.can_delivery("北京市昌平区回龙观新龙城2期36A号楼")
        self.assertEqual(res["result"], 0, res)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestOrder("test_1_create_order"))
    suite.addTest(TestOrder("test_2_get_order"))
    suite.addTest(TestOrder("test_3_cancel_order"))
    suite.addTest(TestOrder("test_4_get_router"))
    suite.addTest(TestOrder("test_5_can_deliver"))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
