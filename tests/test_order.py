#!/usr/bin/python3
# @Time    : 2019-08-21
# @Author  : Kevin Kong (kfx2007@163.com)

import unittest
from sf.api import SF
from sf.model.contact import ContactInfo
from sf.model.cargo import CargoDetail
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
        contacts = []
        sender = ContactInfo("北京市昌平区回龙观天慧园",company="测试公司",mobile="18512345678")
        receiver = ContactInfo("北京市海淀区新中关大厦A座",company="新东方",mobile="18511223344",contactType=1)
        contacts.append(sender)
        contacts.append(receiver)
        cargo_detail = CargoDetail("测试货物")
        res = self.sf.order.create_order(self.order_no, contacts,[cargo_detail])
        self.assertEqual(res["success"], True, res)

    def test_2_get_order(self):
        """测试订单查询接口"""
        res = self.sf.order.get_order(self.order_no)
        self.assertEqual(res["success"], True, res)

    def test_3_cancel_order(self):
        """测试取消订单"""
        res = self.sf.order.confirm_order(self.order_no, dealType=2)
        self.assertEqual(res["success"], True, res)

    def test_4_get_router(self):
        """测试路由信息"""
        # 只有先下单 才能拿得到路由信息 否则是空
        contacts = []
        sender = ContactInfo("北京市昌平区回龙观天慧园",company="测试公司",mobile="18512345678")
        receiver = ContactInfo("北京市海淀区新中关大厦A座",company="新东方",mobile="18511223344",contactType=1)
        contacts.append(sender)
        contacts.append(receiver)
        cargo_detail = CargoDetail("测试货物")
        self.sf.order.create_order(self.order_no, contacts,[cargo_detail])
        res = self.sf.order.get_route_info(self.order_no)
        self.assertTrue(res['success'], res)

    def test_5_can_deliver(self):
        """是否可以收派"""
        res = self.sf.order.can_delivery(self.order_no)
        self.assertTrue(res['success'], res)

    def test_0_access_token(self):
        """测试获取AccessToken"""
        access_token = self.sf.comm.get_access_token()
        self.assertNotEqual(access_token, None)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestOrder("test_0_access_token"))
    suite.addTest(TestOrder("test_1_create_order"))
    suite.addTest(TestOrder("test_2_get_order"))
    suite.addTest(TestOrder("test_3_cancel_order"))
    suite.addTest(TestOrder("test_4_get_router"))
    suite.addTest(TestOrder("test_5_can_deliver"))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
