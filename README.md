[![Build Status](https://travis-ci.org/block-cat/sf-sdk.svg?branch=master)](https://travis-ci.org/block-cat/sf-sdk)
[![Coverage Status](https://coveralls.io/repos/github/block-cat/sf-sdk/badge.svg?branch=master)](https://coveralls.io/github/block-cat/sf-sdk?branch=master)
[![PYPI](https://img.shields.io/pypi/v/sf-sdk)](https://pypi.org/project/sf-sdk/)

# 顺丰 Python SDK

基于顺丰官网开放平台2.0 API开发的Python SDK

版本：2.1.0.0

## 功能概述

目前已经开发完成的接口列表:

* 下订单接口
* 订单确认/取消接口-速运类API
* 订单结果查询接口
* 路由查询接口接口-速运类API
* 订单筛选接口-速运类API
* 时效标准及价格查询接口-速运类API
* 产品推荐接口-速运类API
* 预估总费用接口-国际件API
* 清单运费查询接口-速运类API

其他接口正在陆续对接中...

## 安装

```python
pip install sf-sdk
```

## 使用示例

clientcode和checkword是在顺丰官网注册后得到的用户编码和校验码

```python
from sf.api import SF

sf = SF("clientcode","checkword")
sf.order.create_order(clientid,..)
```

### 下单

```python
contacts = []
sender = ContactInfo("北京市昌平区回龙观天慧园",company="测试公司",mobile="18512345678",contactType=1)
receiver = ContactInfo("北京市海淀区新中关大厦A座",company="新东方",mobile="18511223344",contactType=2)
contacts.append(sender)
contacts.append(receiver)
cargo_detail = CargoDetail("测试货物")
res = self.sf.order.create_order(self.order_no, contacts,[cargo_detail])
```

### 订单查询

```python
res = self.sf.order.get_order(self.order_no)
```

### 确认/取消订单

```python
res = self.sf.order.confirm_order(self.order_no, dealType=2)
```

### 路由信息

```python
res = self.sf.order.get_route_info(self.order_no)
```

### 判断是否可以派单

```python
res = self.sf.order.can_delivery(self.order_no)
```

### 打印电子面单

```python
res = self.sf.order.get_order(self.order_no)
documents = [
    {
        "masterWaybillNo": res['msgData']['waybillNoInfoList'][0]['waybillNo'],
    }
]
res = self.sf.sheet.sync_print(f"fm_150_standard_QXH",documents)
```

### 产品推荐与预估费用

产品推荐接口需要先开通 `EXP_RECE_PSDS_PRODUCT_RECOMMEND` 权限。返回值中的
`msgData.productList` 会包含 `totalFee`、`currency` 和 `serviceFeeList`；其中
燃油附加费的服务代码为 `IN15`。

```python
res = sf.order.recommend_products(
    srcProvince="香港",
    srcCity="香港",
    destProvince="澳门",
    destCity="澳门",
    sendTime="2026-09-04 12:00:00",
    weight=1,
    paymentTerms="1",
    srcAddress="香港葵涌永建路",
    destAddress="澳门半岛南湾大马路",
    monthlyCard="your-monthly-card",
    commodityNameList=["文件"],
)
```

国际件预估总费用接口会返回 `currency`、`totalFee` 和 `feeInfoList`，需要单独
申请对应的国际接口权限。

```python
res = sf.order.estimate_total_fee(
    customerCode="your-international-customer-code",
    interProductCode="INT0001",
    senderInfo={"country": "HK", "postCode": "999077", "address": "Kwai Chung"},
    receiverInfo={"country": "MO", "postCode": "999078", "address": "Macau"},
    parcelQuantity=1,
    parcelTotalWeight=1,
)
```

### 清单运费查询

`trackingType` 为 `1` 时按客户订单号查询，为 `2` 时按顺丰运单号查询。
返回值中的 `msgData.waybillFeeList` 是实际费用明细，燃油附加费的费用类型为
`14`。

```python
res = sf.order.query_waybill_fee(
    trackingType=2,
    trackingNum="SF1234567890",
)
```

### 沙箱联调

实时沙箱测试默认跳过。需要运行时通过环境变量提供凭据，凭据不会写入代码：

```bash
export SF_SANDBOX_CLIENT_CODE="your-client-code"
export SF_SANDBOX_CHECKWORD="your-checkword"
pytest
```

### 三个费用接口的真实测试（无 Mock）

只运行费用查询测试，不会创建或取消运单：

```bash
export SF_ENVIRONMENT=sandbox
# 凭据从本机环境或私密配置文件加载：
# SF_SANDBOX_CLIENT_CODE / SF_SANDBOX_CHECKWORD
# 生产环境改为 SF_ENVIRONMENT=production，使用：
# SF_PRODUCTION_CLIENT_CODE / SF_PRODUCTION_CHECKWORD

export SF_RECOMMEND_PRODUCTS_JSON='{"srcProvince":"香港","srcCity":"香港","destProvince":"澳门","destCity":"澳门","sendTime":"填写实际寄件时间 YYYY-MM-DD HH:MM:SS","weight":1,"paymentTerms":"1","srcAddress":"填写实际寄件地址","destAddress":"填写实际收件地址"}'
export SF_ESTIMATE_TOTAL_FEE_JSON='{"customerCode":"填写国际客户编码","interProductCode":"填写已开通产品编码","senderInfo":{"country":"HK","address":"填写实际地址"},"receiverInfo":{"country":"MO","address":"填写实际地址"},"parcelTotalWeight":1}'
export SF_QUERY_WAYBILL_FEE_JSON='{"trackingType":2,"trackingNum":"填写本账号已有运单号"}'
python3 -m unittest tests.test_fee_apis -v
```

请求 JSON 可加入接口要求的月结账号、付款信息、申报信息等字段；以上为填写模板，运行前必须替换占位值。未配置凭据时整组跳过，未配置某个 JSON 时只跳过对应接口；配置错误、未授权或接口错误会使测试失败，不会视为成功。

产品推荐测试输出总价、币种和 `IN15` 燃油费用。若测试路线预期必须返回燃油费，可设置 `SF_EXPECT_FUEL_FEE=1`，缺少该项则失败。默认不假设所有路线都有燃油费，也不固定断言总价为 47。预估总费用测试输出总价、币种和费用明细数量；清单查询使用已有运单。请勿把真实凭据或客户请求 JSON 提交到仓库。
