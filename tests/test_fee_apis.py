#!/usr/bin/python3
"""Live, read-only fee API tests. Configure credentials and payloads via env."""

import json
import os
import unittest

from sf.api import SF


class TestFeeApis(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        environment = os.environ.get('SF_ENVIRONMENT', 'sandbox').lower()
        if environment not in ('sandbox', 'production'):
            raise ValueError('SF_ENVIRONMENT must be sandbox or production')
        prefix = 'SF_' + environment.upper()
        client_code = os.environ.get(prefix + '_CLIENT_CODE')
        checkword = os.environ.get(prefix + '_CHECKWORD')
        if not client_code or not checkword:
            raise unittest.SkipTest(
                'Set {}_CLIENT_CODE and {}_CHECKWORD'.format(prefix, prefix)
            )
        cls.sf = SF(client_code, checkword, sandbox=environment == 'sandbox',
                    language=os.environ.get('SF_LANGUAGE', 'zh-CN'))

    def _payload(self, variable):
        raw = os.environ.get(variable)
        if not raw:
            self.skipTest('Set ' + variable + ' to a JSON request object')
        try:
            payload = json.loads(raw)
        except ValueError:
            self.fail(variable + ' must contain valid JSON')
        self.assertIsInstance(payload, dict, variable + ' must be a JSON object')
        return payload

    def _data(self, result):
        self.assertIsInstance(result, dict)
        self.assertTrue(result.get('success'), '{}: {}'.format(
            result.get('errorCode', ''), result.get('errorMsg', 'API failed')))
        data = result.get('msgData')
        self.assertTrue(data, 'API succeeded but returned no fee data')
        return data

    def test_recommend_products(self):
        data = self._data(self.sf.order.recommend_products(
            **self._payload('SF_RECOMMEND_PRODUCTS_JSON')))
        products = data.get('productList') or []
        self.assertTrue(products, 'No available products returned')
        for product in products:
            self.assertIsNotNone(product.get('totalFee'), 'Missing totalFee')
            self.assertTrue(product.get('currency'), 'Missing currency')
            print('Product quote:', json.dumps({
                'expressType': product.get('expressType'),
                'totalFee': product['totalFee'],
                'currency': product['currency'],
                'fuelFees': [{k: fee.get(k) for k in ('serviceCode', 'serviceFee')}
                             for fee in product.get('serviceFeeList', []) or []
                             if fee.get('serviceCode') == 'IN15'],
            }, ensure_ascii=False), flush=True)
        if os.environ.get('SF_EXPECT_FUEL_FEE') == '1':
            self.assertTrue(any(
                fee.get('serviceCode') == 'IN15'
                for product in products
                for fee in product.get('serviceFeeList', []) or []
            ), 'No IN15 fuel surcharge returned for this route')

    def test_estimate_total_fee(self):
        data = self._data(self.sf.order.estimate_total_fee(
            **self._payload('SF_ESTIMATE_TOTAL_FEE_JSON')))
        self.assertIsNotNone(data.get('totalFee'), 'Missing totalFee')
        self.assertTrue(data.get('currency'), 'Missing currency')
        print('Estimated fee:', json.dumps({
            'totalFee': data['totalFee'], 'currency': data['currency'],
            'feeDetailCount': len(data.get('feeInfoList') or []),
        }, ensure_ascii=False), flush=True)

    def test_query_waybill_fee(self):
        # Requires an existing account-owned order/waybill; never creates one.
        data = self._data(self.sf.order.query_waybill_fee(
            **self._payload('SF_QUERY_WAYBILL_FEE_JSON')))
        print('Waybill fee query: non-empty response received', flush=True)
        self.assertIsInstance(data, (dict, list))


if __name__ == '__main__':
    unittest.main()
