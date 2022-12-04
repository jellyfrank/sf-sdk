[![Build Status](https://travis-ci.org/block-cat/sf-sdk.svg?branch=master)](https://travis-ci.org/block-cat/sf-sdk)
[![Coverage Status](https://coveralls.io/repos/github/block-cat/sf-sdk/badge.svg?branch=master)](https://coveralls.io/github/block-cat/sf-sdk?branch=master)
[![PYPI](https://img.shields.io/pypi/v/sf-sdk)](https://pypi.org/project/sf-sdk/)

# 顺丰 Python SDK

基于顺丰官网开放平台2.0 API开发的Python SDK

版本：2.0.0.2

## 功能概述

目前已经开发完成的接口列表:

* 下订单接口
* 订单确认/取消接口-速运类API
* 订单结果查询接口
* 路由查询接口接口-速运类API
* 订单筛选接口-速运类API

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
sender = ContactInfo("北京市昌平区回龙观天慧园",company="测试公司",mobile="18512345678")
receiver = ContactInfo("北京市海淀区新中关大厦A座",company="新东方",mobile="18511223344",contactType=1)
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