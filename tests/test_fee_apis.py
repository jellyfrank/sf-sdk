#!/usr/bin/python3

import unittest
from unittest.mock import Mock

from sf.order.order import Order


class TestFeeApiPayloads(unittest.TestCase):

    def setUp(self):
        self.order = Order()
        self.order.post = Mock(return_value={"success": True})

    def test_recommend_products_payload(self):
        result = self.order.recommend_products(
            srcProvince="香港",
            srcCity="香港",
            destProvince="澳门",
            destCity="澳门",
            sendTime="2026-09-04 12:00:00",
            weight=1,
            paymentTerms="1",
            srcAddress="香港葵涌永建路",
            destAddress="澳门半岛南湾大马路",
            monthlyCard="test-monthly-card",
            commodityNameList=["文件"],
        )

        self.assertEqual(result, {"success": True})
        self.order.post.assert_called_once_with(
            "EXP_RECE_PSDS_PRODUCT_RECOMMEND",
            {
                "srcProvince": "香港",
                "srcCity": "香港",
                "destProvince": "澳门",
                "destCity": "澳门",
                "sendTime": "2026-09-04 12:00:00",
                "weight": 1,
                "paymentTerms": "1",
                "srcAddress": "香港葵涌永建路",
                "destAddress": "澳门半岛南湾大马路",
                "monthlyCard": "test-monthly-card",
                "commodityNameList": ["文件"],
            },
        )

    def test_estimate_total_fee_payload(self):
        sender = {
            "country": "HK",
            "postCode": "999077",
            "address": "Kwai Chung",
        }
        receiver = {
            "country": "MO",
            "postCode": "999078",
            "address": "Macau Peninsula",
        }

        result = self.order.estimate_total_fee(
            customerCode="test-customer",
            interProductCode="INT0001",
            senderInfo=sender,
            receiverInfo=receiver,
            parcelQuantity=1,
            parcelTotalWeight=1,
            declaredCurrency="HKD",
        )

        self.assertEqual(result, {"success": True})
        self.order.post.assert_called_once_with(
            "COM_RECE_IUOP_ESTIMATE_FEE",
            {
                "customerCode": "test-customer",
                "interProductCode": "INT0001",
                "senderInfo": sender,
                "receiverInfo": receiver,
                "parcelQuantity": 1,
                "parcelTotalWeight": 1,
                "declaredCurrency": "HKD",
            },
        )

    def test_query_waybill_fee_payload(self):
        result = self.order.query_waybill_fee(
            trackingType=2,
            trackingNum="SF1234567890",
            bizTemplateCode="test-template",
        )

        self.assertEqual(result, {"success": True})
        self.order.post.assert_called_once_with(
            "EXP_RECE_QUERY_SFWAYBILL",
            {
                "trackingType": "2",
                "trackingNum": "SF1234567890",
                "bizTemplateCode": "test-template",
            },
        )


if __name__ == "__main__":
    unittest.main()
