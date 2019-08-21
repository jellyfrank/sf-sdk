# 顺丰第三方Python SDK

看了一下官方的sdk，怎么说呢，有点不忍直视，而且官方的通讯格式是xml用起来好像也没有那么方便，于是决定自己写一个，把接口数据和返回结果都改成了json格式。

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

目前只实现了一个下单的接口，持续更新中...