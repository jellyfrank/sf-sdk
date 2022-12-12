#!/usr/bin/python3
# @Time    : 2019-08-21
# @Author  : Kevin Kong (kfx2007@163.com)

import unittest
from sf.api import SF
from sf.model.contact import ContactInfo
from sf.model.cargo import CargoDetail
from sf.model.address import Address
from autils import randomstr
import pytest


class TestOrder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sf = SF("QXH", "yxGvL9y1bJj9mRy9rIjZVBK4nokAwxrf", True, 'en')
        cls.order_no = randomstr.generate_digits(12)
        cls.mail_no = None

    def _create_order(self):
        contacts = []
        sender = ContactInfo("北京市昌平区回龙观天慧园",company="测试公司",mobile="18512345678")
        receiver = ContactInfo("北京市海淀区新中关大厦A座",company="新东方",mobile="18511223344",contactType=1)
        contacts.append(sender)
        contacts.append(receiver)
        cargo_detail = CargoDetail("测试货物")
        return self.sf.order.create_order(self.order_no, contacts,[cargo_detail])

    def test_1_create_order(self):
        """测试下单"""
        res = self._create_order()
        self.assertEqual(res["success"], True, res)

    def test_2_get_order(self):
        """测试订单查询接口"""
        res = self.sf.order.get_order(self.order_no)
        self.assertEqual(res["success"], True, res)

    def test_99_cancel_order(self):
        """测试取消订单"""
        res = self.sf.order.confirm_order(self.order_no, dealType=2)
        self.assertEqual(res["success"], True, res)

    def test_4_get_router(self):
        """测试路由信息"""
        #{'apiErrorMsg': '', 'apiResponseID': '000184DB8E57803FE6AA43A0CAC24D3F', 
        # 'apiResultCode': 'A1000', 'apiResultData': 
        # '{"success":true,"errorCode":"S0000","errorMsg":null,
        # "msgData":{"routeResps":
        # [{"mailNo":"066106553309","routes":[{"acceptAddress":"深圳市","acceptTime":"2022-12-04 13:14:09","remark":"顺丰速运 已收取快件","opCode":"50"
        # }]}]}}'}
        # 只有先下单 才能拿得到路由信息 否则是空
        contacts = []
        sender = ContactInfo("北京市昌平区回龙观天慧园",company="测试公司",mobile="18512345678")
        receiver = ContactInfo("北京市海淀区新中关大厦A座",company="新东方",mobile="18511223344",contactType=1)
        contacts.append(sender)
        contacts.append(receiver)
        cargo_detail = CargoDetail("测试货物")
        self.sf.order.create_order(randomstr.generate(12), contacts,[cargo_detail])
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

    def test_6_print(self):
        """"测试电子面单"""
        # [{'areaNo': 1, 'pageNo': 1, 'seqNo': 1, '
        #  token': 'AUTH_tkv12_f146d1855480549d262b5c46ab0ab597ff20a97d9d0db45c16bedeb4fabd112b012deadd477ee524b1d690ce01baa3cdffbb125a6ccf69b73778dba2eb5157eb73744dffd1a1bbe5c4390bfb93ce4c3e9197d359c3ace1b33151306bc9e831ab67720381919951fc04fd23bb349f18cda712e03cdb9961c933bba7d6177fa548e4a43f0933ce2b32089181f98d7c23a786969366c357d7da3f10ac20f099e909e8a27d9f175808a32056e0c85df11786d9c10d75656ea37df97b385c9c79c546', 
        # 'url': 'https://eos-scp-core-shenzhen-futian1-oss.sf-express.com:443/v1.2/AUTH_EOS-SCP-CORE/print-file-sbox/QXH_e45c4058-6972-4605-9182-e337814f5dff_SF7444462031543_fm_150_standard_QXH_1_1_1.pdf', 
        # 'waybillNo': 'SF7444462031543'}]
        res = self.sf.order.get_order(self.order_no)
        print('+++++++++++++++++++')
        print(res)
        documents = [
            {
                "masterWaybillNo": res['msgData']['waybillNoInfoList'][0]['waybillNo'],
            }
        ]
        res = self.sf.sheet.sync_print(f"fm_150_standard_QXH",documents)
        self.assertTrue(len(res[0]), res)

    def test_7_get_express_types(self):
        res = SF.get_express_types()
        self.assertTrue(len(res), res)

    def test_8_get_custom_templates(self):
        res = self.sf.sheet.get_custom_templates("")

    def test_9_query_delivery(self):
        src_address = Address("北京市","北京市","昌平区","回龙观大街")
        dest_address = Address("山东省","青岛市","市北区","万达广场")
        res = self.sf.order.query_delivery(1,src_address, dest_address)
        self.assertTrue(res['success'],res)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestOrder("test_0_access_token"))
    suite.addTest(TestOrder("test_1_create_order"))
    suite.addTest(TestOrder("test_2_get_order"))
    suite.addTest(TestOrder("test_4_get_router"))
    suite.addTest(TestOrder("test_5_can_deliver"))
    suite.addTest(TestOrder("test_6_print"))
    suite.addTest(TestOrder("test_99_cancel_order"))
    suite.addTest(TestOrder("test_7_get_express_types"))
    suite.addTest(TestOrder("test_8_get_custom_templates"))
    suite.addTest(TestOrder("test_9_query_delivery"))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
