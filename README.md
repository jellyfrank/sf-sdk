[![Build Status](https://travis-ci.org/block-cat/sf-sdk.svg?branch=master)](https://travis-ci.org/block-cat/sf-sdk)
[![Coverage Status](https://coveralls.io/repos/github/block-cat/sf-sdk/badge.svg?branch=master)](https://coveralls.io/github/block-cat/sf-sdk?branch=master)

# 顺丰 Python SDK

官方SDK只是一个demo，而且数据格式为XML，处理起来并不方便，因此起了这个项目并将数据格式调整为了json格式。

## 使用说明

### 安装

```python
pip install sf-sdk
```
使用
```python
from sf.api import SF

sf = SF("clientcode","checkword")

sf.order.create_order(clientid,..)

```

## changelog

* [0.1.0] 修复路由查询结果中包含数组类型的数据格式错误
* [0.0.6] 新增路由查询接口
* [0.0.3] 新增确定/取消订单接口

python2 的同学请使用0.0.9 版本
  