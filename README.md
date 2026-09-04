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
