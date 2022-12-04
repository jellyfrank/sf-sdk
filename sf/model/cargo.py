#!/usr/bin/python3
# @Time    : 2022-12-03
# @Author  : Kevin Kong (kfx2007@163.com)

from copy import copy

class CargoDetail(object):

    def __init__(self, name, count=None, unit=None, weight=None, amount=None, currency=None, sourceArea=None, **kwargs):
        """
        货物信息

        param count: Number(5)	条件	货物数量 跨境件报关需要填写
        param unit: String(30)	条件	货物单位，如：个、台、本， 跨境件报关需要填写
        param weight: Number(16,3)	条件	订单货物单位重量，包含子母件， 单位千克，精确到小数点后3位 跨境件报关需要填写
        param amount: Number(17,3)	条件	货物单价，精确到小数点后3位， 跨境件报关需要填写
        param currency: String(5)	条件	货物单价的币别： 参照附录《国际件币别表》
        param sourceArea: String(5)	条件	原产地国别， 跨境件报关需要填写
        param productRecordNo: String(18)	否	货物产品国检备案编号
        param goodPrepardNo: String(100)	否	商品海关备案号
        param taxNo: String(100)	否	商品行邮税号
        param hsCode: String(100)	否	海关编码
        param goodsCode: String(60)	否	商品编号
        param brand: String(60)	否	货物品牌
        param specifications:String(60)	否	货物规格型号
        param manufacturer:String(100)	否	生产厂家
        param shipmentWeight:Double (16,3)	否	托寄物毛重
        param length:Double (16,3)	否	托寄物长
        param width:Double (16,3)	否	托寄物宽
        param height:Double (16,3)	否	托寄物高
        param volume:Double (16,2)	否	托寄物体积
        param cargoDeclaredValue:Double (16,5)	否	托寄物声明价值（杭州口岸必填）
        param declaredValueDeclaredCurrency	String(5)	否	托寄物声明价值币别（杭州口岸必填）
        param cargoId:String(60)	否	货物id（逆向物流）
        param intelligentInspection	Number(1):否	智能验货标识(1-是,0-否) （逆向物流）
        param snCode:String(4000)	否	货物标识码（逆向物流）
        param stateBarCode: String(50)	否	国条码
        """
        self.name = name
        self.count = count
        self.unit = unit
        self.weight = weight
        self.amount = amount
        self.currency = currency
        self.sourceArea = sourceArea
        self.productRecordNo = kwargs.get('productRecordNo',None)
        self.goodPrepardNo = kwargs.get('goodPrepardNo',None)
        self.taxNo = kwargs.get('taxNo',None)
        self.hsCode = kwargs.get('hsCode',None)
        self.goodsCode = kwargs.get('goodsCode',None)
        self.brand = kwargs.get('brand',None)
        self.specifications = kwargs.get('specifications',None)
        self.manufacturer = kwargs.get('manufacturer',None)
        self.shipmentWeight = kwargs.get('shipmentWeight',None)
        self.length = kwargs.get('length',None)
        self.width = kwargs.get('width',None)
        self.height = kwargs.get('height',None)
        self.volume = kwargs.get('valume',None)
        self.cargoDeclaredValue = kwargs.get('cargoDeclaredValue',None)
        self.declaredValueDeclaredCurrency = kwargs.get('declaredValueDeclaredCurrency',None)
        self.cargoId = kwargs.get('cargoId',None)
        self.intelligentInspection = kwargs.get('intelligentInspection',None)
        self.snCode = kwargs.get('snCode',None)
        self.stateBarCode = kwargs.get('stateBarCode',None)

    def to_dict(self):
        res = {
            "name": self.name,
            "count": self.count,
            "unit": self.unit,
            "weight": self.weight,
            "amount": self.amount,
            "currency": self.currency,
            "sourceArea": self.sourceArea,
            "productRecordNo": self.productRecordNo,
            "goodPrepardNo": self.goodPrepardNo,
            "taxNo": self.taxNo,
            "hsCode": self.hsCode,
            "goodsCode": self.goodsCode,
            "brand": self.brand,
            "specifications": self.specifications,
            "manufacturer": self.manufacturer,
            "shipmentWeight": self.shipmentWeight,
            "length": self.length,
            "width": self.width,
            "height": self.height,
            "volume": self.volume,
            "cargoDeclaredValue": self.cargoDeclaredValue,
            "declaredValueDeclaredCurrency": self.declaredValueDeclaredCurrency,
            "cargoId": self.cargoId,
            "intelligentInspection": self.intelligentInspection,
            "snCode": self.snCode,
            "stateBarCode": self.stateBarCode
        }
        copy_data = copy(res)
        for k, v in copy_data.items():
            if v is None:
                res.pop(k)
        return res
