#!/usr/bin/python3

import unittest
from copy import deepcopy
from unittest.mock import Mock

from sf.order.order import Order


class TestFeeApiPayloads(unittest.TestCase):

    def setUp(self):
        self.order = Order()
        self.order.post = Mock(return_value={"success": True})

    def _call_fee_api(self, method):
        if method == 'recommend_products':
            return self.order.recommend_products(
                '香港', '香港', '澳门', '澳门',
                '2026-09-04 12:00:00', 1, '1', 'Sender street', 'Receiver street',
            )
        if method == 'estimate_total_fee':
            return self.order.estimate_total_fee(
                'test-customer', 'INT0001', {'country': 'HK'}, {'country': 'MO'},
            )
        return self.order.query_waybill_fee(2, 'SF1234567890')

    def test_fee_responses_preserve_total_currency_and_fee_details(self):
        # Synthetic contract fixtures, not evidence of live account permission
        # or actual SF tariffs. The SDK must not add fuel a second time.
        cases = {
            'recommend_products': {'productList': [{
                'totalFee': 47, 'currency': 'HKD',
                'serviceFeeList': [{'serviceCode': 'IN15', 'serviceFee': 13}],
            }]},
            'estimate_total_fee': {
                'totalFee': 47, 'currency': 'HKD',
                'feeInfoList': [{'name': '燃油附加费', 'amount': 13}],
            },
            'query_waybill_fee': {
                'waybillFeeList': [{'feeType': '14', 'fee': 13}],
            },
        }
        for method, data in cases.items():
            with self.subTest(method=method):
                response = {'success': True, 'msgData': data}
                self.order.post.return_value = response
                self.assertIs(self._call_fee_api(method), response)

    def test_business_errors_are_returned_without_fabricating_a_price(self):
        for method in ('recommend_products', 'estimate_total_fee', 'query_waybill_fee'):
            with self.subTest(method=method):
                response = {'success': False, 'errorMsg': '无对应服务权限'}
                self.order.post.return_value = response
                self.assertIs(self._call_fee_api(method), response)

    def test_transport_and_permission_exceptions_propagate(self):
        for method in ('recommend_products', 'estimate_total_fee', 'query_waybill_fee'):
            for error in (TimeoutError('request timed out'), Exception('无对应服务权限')):
                with self.subTest(method=method, error=str(error)):
                    self.order.post.side_effect = error
                    with self.assertRaises(type(error)) as raised:
                        self._call_fee_api(method)
                    self.assertIs(raised.exception, error)

    def test_waybill_query_supports_order_number_and_optional_fields(self):
        for tracking_type in (1, '1', 2, '2'):
            with self.subTest(tracking_type=tracking_type):
                self.order.post.reset_mock()
                self.order.query_waybill_fee(
                    tracking_type, 'test-reference', extensionField='test-value',
                )
                self.order.post.assert_called_once_with('EXP_RECE_QUERY_SFWAYBILL', {
                    'trackingType': str(tracking_type),
                    'trackingNum': 'test-reference',
                    'bizTemplateCode': None,
                    'extensionField': 'test-value',
                })

    def test_estimate_fee_keeps_nested_optional_data_unchanged(self):
        options = {
            'paymentInfo': {'payMethod': '1'},
            'customsInfo': {'declaredValue': 480, 'declaredCurrency': 'HKD'},
            'addServiceInfoList': [],
            'parcelTotalWeight': 0.5,
        }
        before = deepcopy(options)
        self.order.estimate_total_fee('test', 'INT0001', {}, {}, **options)
        self.assertEqual(options, before)
        payload = self.order.post.call_args[0][1]
        for key, value in options.items():
            self.assertEqual(payload[key], value)

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
